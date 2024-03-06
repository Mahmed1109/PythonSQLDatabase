from connection import * #import everything from connect.py


def insert_films():
    #create empty list
    newfilm=[]
    # Ask for first name and last name and email
    #we dont need to ask for memberID because its autoincremented and doesnt need an input
    title=input("Enter your title:")
    yearReleased=input("Enter yeardReleased:")
    rating=input("Enter your rating:")
    duration=input("Enter how long the movie is in minutes:")
    genre=input("Enter what genre it is:")


    newfilm.append(title)
    newfilm.append(yearReleased)
    newfilm.append(rating)
    newfilm.append(duration)
    newfilm.append(genre)



    try:
        
        dbCursor.execute("INSERT INTO tblFilms VALUES (NULL,?,?,?,?,?)",newfilm) #values from the list
        dbCon.commit() #makes change permenant
        print(f"{title} inserted in the Table")
    except sql.OperationalError as e:
     
     dbCon.rollback()
     print(f"Insert failed {e}")    
if __name__== "__main__":
     insert_films()






