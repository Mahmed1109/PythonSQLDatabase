from connection import *

# #create a subroutine

# def updateMembers():
#     #Use MemberID

#     idfield=input("Enter ID that corralates to row you want to change:")
#     fieldName=input("Enter the field name(Firstname,Lastname,Email) that you want to change:").title()


#     newFieldValue=input(f"Enter the new content for {fieldName}")
#     #we will add quotes to the newFieldValue
#     newFieldValue="'"+newFieldValue+"'"

#     try:
#         dbCursor.execute(f"UPDATE members SET{fieldName}={newFieldValue} WHERE MemberID={idfield}")
#         dbCon.commit()
#         print(f"{newFieldValue} has been added to the Members Database")
#     except sql.OperationalError[e]:
#         print(f"Update failed{e}")

# if __name__=="__main__":
#     updateMembers()
# DIDNT WORK WHY??????????????


# create a subroutine
def update_films():
   try:
     #     #Use MemberID
      idField = input("Enter the filmID of the record you want to update: ")
      fieldName = input("Which field do you want to change(title,yearReleased,rating,duration,genre) to update: ")
      # the value to be entered in the field 
      newfieldValue = input(f"Enter the new value for the {fieldName}: ")
      # add quotes to field value
      newfieldValue = "'"+newfieldValue+"'"
      # UPDATE members SET Firstname = "James" WHERE MemberID = 1/2/3/4....
      dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = {newfieldValue} WHERE filmID = {idField} ")
      dbCon.commit()
      print(f"{idField} Updated in the tblFilms table ")
   except sql.OperationalError as e:
    print(f"Update failed: {e}")
if __name__ == "__main__":
   update_films()








