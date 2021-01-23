from sys import stderr
from utils import *
import psycopg2


class DataBase:
    def __init__(self, dbName, user, password, host, port, schemas):

        self.dbName = dbName
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.schemas = schemas

        self.conn = None
        self.cursor = None

    def exectue_query(self, query):

        result = None
        try:
            self.cursor.execute(query)

            if query.startswith('SELECT'):
                result = self.cursor.fetchall()

        except Exception as err:
            # if err is not None:
            # self.conn.rollback()
            stderr.write(
                f'{bcolors.OKBLUE}An error from PostgreSQL is raised: ' +
                str(err))
            return

        finally:
            # print('yay')

            self.conn.commit()
            # self.conn.close()

        return result

    def connect(self):  # DONE

        self.conn = conn = psycopg2.connect(
            database=self.dbName,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port)
        self.cursor = conn.cursor()

    def insert(self, obj):  # DONE

        # If NULL Then Insert NULL
        # if another class will be added, it works!!!
        attributes = ''
        values = ''

        items = obj.__dict__.items()
        class_name = obj.__class__.__name__

        is_first = True  # for first ','
        for i in items:

            if is_first:
                attributes = attributes + i[0]

                if i[1] is None:
                    i[1] = 'NULL'
                values = values + quote(str(i[1]))
                is_first = False
                continue

            attributes = attributes + ' , ' + i[0]
            val = i[1]
            if i[1] is None:
                i[1] = 'NULL'
            val = quote(str(i[1]))
            values = values + ' , ' + val

        if class_name in self.schemas:
            insert_query = f'INSERT INTO {class_name}({attributes}) VALUES({values})'
            self.exectue_query(insert_query)

        else:  # GIVE IT TO THE SQL WHEN CORRECTING TRY CATCH
            print('Table does not exist.')

    def delete(self, table, column, key):  # DONE
        # use column instead of id for all. because you might want to delete
        # all records which have the same feature

        query = f'DELETE FROM {table} WHERE {column} = {quote(key)}'
        self.exectue_query(query)

    def update(self, table, column, new_value, key_column, value_column):
        query = f'UPDATE {table} SET {column} = {quote(new_value)} WHERE {key_column} = {quote(value_column)}'
        self.exectue_query(query)

    def get(self, table):

        select_query = f'SELECT * FROM {table}'
        result = self.exectue_query(select_query)
        return result
