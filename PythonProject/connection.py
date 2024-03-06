import sqlite3 as sql

try:

    with sql.connect("BootcampWork/Python/Week10/PythonProject/filmflix.db") as dbCon:
         
        dbCursor=dbCon.cursor() 

except sql.OperationalError as e: 
    print(f"Connection failed:{e}")

