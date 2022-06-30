from mag import *
import logo


main = "authh.login()"
modul =  modull
language = languages

#languages.magyar()
#languages.english()
# a1, a2, a3
login = ["Hungary", "English", "Exit"]
a = [
    "0 :Hungary",
    "1 :English",
    "2 :Exit"
    ]
    
print(*a, sep = "\n" )
print("\n")

api_var = login[int(input("Enter a Number: "))]

if  api_var == login[0] and main:
    languages.magyar()
    modull.category()
   

if  api_var == login[1] and main:
    languages.english()
    modul.categorya()

if api_var == login[2]:
    exit





    



