from connection import *



def film_search():
    try:
        while True:
            field = input("Would you like to search by filmID,\n title,\n yearReleased,\n rating,\n duration,\n genre ")
            
            if field == "filmID":
                while True:
                    idInput = input("Enter filmID: ")
                    dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idInput}")
                    row = dbCursor.fetchone()
                    
                    if row is None:
                        print(f"No record with {idInput} exists in the table.")
                    else:
                        for aRecord in row:
                            print(aRecord)
                        break  # Break the inner loop as a valid filmID is found
            
            elif field.lower() == "title" or field.lower() == "yearReleased" or field.lower() == "rating" or field.lower()=="genre" or field.lower()=="duration":
                searchInput = input(f"Enter search field for {field}: ")
                dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{searchInput}%'")
                rows = dbCursor.fetchall()
                
                if not rows:
                    print(f"No record with field {field} matching '{searchInput}' in the table.")
                else:
                    for records in rows:
                        print(records)
            
            else:
                print(f"Invalid search field {field}")

    except sql.OperationalError as e:
        print(f"No Database or table found: {e}")

if __name__ == "__main__":
    film_search()

    
