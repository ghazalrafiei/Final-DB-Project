<h1>Final Database Course Project - Fall 2020</h1>

An application for managing a database and do CRUD operations on its different tables.

The schema is derieved from first exercise which was to create ER model for an online airline ticket booking website and it is available in folder ```sql``` which also has queries for creating tables and inserting some records in it.

One of the advantages is you can add or remove columns from the schema only by changing the schema itself and making those changes in ```config.yml``` and ```object.py``` and the program will be adopted to that change itself.

<h2>Operations</h2>
Inserting is obvious but for deleting and updating, at first you must select a row or cell respectively and then click the button. After that, you must see that change or an dialog box in case the query could not be committed.

Optional box is embedded for you to see anything from the tables you want and you will see the results in an informative dialog box.

<h2>More</h2>
You can switch between dark and light them only by changing `if True` to `False` in the beginning of `gui/darkTheme.p`.
