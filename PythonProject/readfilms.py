from connection import *

#create a subroutine

def readfilms():
    try:
        dbCursor.execute("SELECT * FROM tblFilms")
        #fetchall()- selects all the selected records
        row=dbCursor.fetchall() #holds all fetched records

        if not row:
           print(f"No records exist")

        else:
             for aRecord in row:
              #loop thru all records in row

              print(aRecord)
              #used to print all records
    

          
    except sql.OperationalError[e]:
        print(f"Records can not be found/shown")
    
if __name__=="__main__":
    readfilms()
    