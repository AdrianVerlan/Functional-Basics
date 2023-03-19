from os import system

def generateinitials():
    system('cls')
    firstname = input("First Name: ")
    lastname  = input("Last Name:  ")
    if len(firstname)<3 or len(lastname)<3:
        print("Error should be more than 3 chars!!!") 
    elif not firstname.isalpha() or not lastname.isalpha():
        print("Error should be only latin letters")
    elif not firstname[0].isupper() or not lastname[0].isupper():
        print("ERROr! First letter should be Upper!!")
    else:
        intials= firstname[0]+"."+ lastname[0]+"."
        print(intials)

generateinitials()