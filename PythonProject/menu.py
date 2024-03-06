import readfilms
import addfilms
import deletefilms
import searchfilms
import updatefilms


def menu_op():
    try:
        with open("BootcampWork/Python/Week10/PythonProject/FilmOptions.txt") as fileRead:
            fr=fileRead.read()
        return fr 
    except FileNotFoundError as nf:
        print (f"Check: {nf}")


#Create the menu function
        
def members_menu():
    option=0 # set as default value
    optionlist=["1","2","3","4","5","6"]

    #assign readfile() function to menuchoices
    menuchoices=menu_op()

    #Create a while loop

    while option not in optionlist:
        print(menuchoices)

        #re-assign the value of option using input function
        option=input("Enter an option from Menu:") 


        #check if the input from the option variable above correlates to any menu numbers/optionlist
        if option not in optionlist:
            print(f"Option: {option} is not a a real value choice")
    return option



mainprogram=True #Boolean vairable used to toggle probably used for while loop


while mainprogram:       #same as while mainprogram=True
     #assign the members_menu function to mainmenu variable
    mainmenu=members_menu()


    match mainmenu:
        case "1":
            readfilms.readfilms()
        case "2":
            addfilms.insert_films()
        case "3":
            updatefilms.update_films()
        case "4":
            deletefilms.delete_films()
        case "5":
            searchfilms.film_search()
        case _:
            #reassign the value of mainprogram to false if input is anything other than the cases above
            mainprogram=False
input("Press Enter key to exit the program")
        
         

