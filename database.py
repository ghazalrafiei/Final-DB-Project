from sys import stderr
import psycopg2

class DataBase:
    def __init__(self,dbName,user,password,host,port):

        self.dbName = dbName
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = ''
        self.schemas = {'Customer','HostWebsite','TravelAgency','TicketCollects','TransactionBuy'}

    def exectue_query(self,query):

        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()
        return 'no error still'

    def connect(self): #DONE
        self.conn = conn = psycopg2.connect(database=self.dbName, user = self.user , password = self.password, host = self.host, port = self.port)
        self.cursor = conn.cursor()
        # return conn

    def insert(self,obj): #DONE
        #If NULL Then Insert NULL
        #if another class will be add, it works!!!
        attributes = ''
        values = '' #String Completed be parsed

        items = obj.__dict__.items()

        is_first = True #for first ','
        for i in items:

            if is_first:
                attributes = attributes + i[0]

                if i[1] is None:
                    i[1] = 'NULL'
                values = values+ '\'' + str(i[1]) + '\''
                is_first = False
                continue  

            attributes = attributes+' , '+ i[0]
            val = i[1]
            if i[1] is None:
                i[1] = 'NULL'
            val = '\'' + str(i[1]) + '\''
            values = values +' , '+ val
        
        


        if obj.__class__.__name__ in self.schemas:
            insert_query = f'INSERT INTO {obj.__class__.__name__}({attributes}) VALUES({values});'
            self.exectue_query(insert_query)

        else:
            raise Exception('Table does not exist.')


    # def delete():
    #     cursor.execute('SQL')
    # def update():
    #     cursor.execute('SQL')
    # def get():
    #     cursor.execute('SQL')
