from connection import *

def delete_films():
    try:
            #use Member ID
        idField=input("What is the id of the field you want to delete:")
        #select the record that you want to delete
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID={idField}")
        print(f"Record{idField} has been deleted")

        selectedrow=dbCursor.fetchone()
        #None function is used to check if a value exists

        if selectedrow==None:
            print(f"{idField} can not be found")
        else:
            dbCursor.execute(f"DELETE FROM members WHERE MemberID={idField}")
            dbCon.commit()

    except sql.OperationalError[e]:
        print(f"Delete failed:{e}")
if __name__=="__main__":
    delete_films()
        




  
