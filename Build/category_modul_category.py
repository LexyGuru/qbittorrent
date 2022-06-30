import os
from mag import *


global_lista = ["info", "limit", "save-path"]
a = [
    "0:  info       ",
	"1:  limit      (X)",
	"2:  save-path  (X)"
    ]

print(*a, sep = "\n" )
print("\n")

global_list = global_lista[int(input("Enter a Number: "))]

if global_list == global_lista[0]:
    print("qbt global info")
    x = "qbt global info"
    #--format <OBJECT_FORMAT> -F <OBJECT_FORMAT>	Output format: list | csv | json | property
    a = [
        "0: list",
        "1: csv",
        "2: json"
        ]

    print(*a, sep = "\n" )
    print("\n")

    var_list = ["list", "csv", "json"]
    list_mod = var_list[int(input("Enter a Number: "))]
    print("qbt global info")
    
    #print(list_mod)
    logfile = " > C://temp//global_info.txt"
    a = x + " --format " + list_mod + connections
    os.system(a + logfile)
    os.system(a)