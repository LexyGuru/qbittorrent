import mag
from mag import *
import os

class modul_category:
        def server_log():
                x = "qbt server info "
                os.system(x + connectionss)
                mag.modul.back()
    
        def server_info():
                server_lista = ["info", "limit", "save-path"]
                a = [
                    "0:  info       ",
	                "1:  limit      (X)",
	                "2:  save-path  (X)"
                ]

                print(*a, sep = "\n" )
                print("\n")

                serverlist = server_lista[int(input("Enter a Number: "))]

                if serverlist == server_lista[0]:
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
                        a = x + " --format " + list_mod + connectionss
                        os.system(a + logfile)
                        mag.modul.back()

                if serverlist == server_lista[1]:
                        print("limit")
                        mag.modul.back()

                if serverlist == server_lista[2]:
                        print("save-path")
                        mag.modul.back()