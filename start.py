import os
import login

from login import connections

print(" \n")                                                                                                                                         
print(",--.                              ,----.                            \n")
print("|  |    ,---. ,--.  ,--.,--. ,--.'  .-./   ,--.,--.,--.--.,--.,--.  \n")
print("|  |   | .-. : \  `'  /  \  '  / |  | .---.|  ||  ||  .--'|  ||  |  \n")
print("|  '--.\   --. /  /.  \   \   '  '  '--'  |'  ''  '|  |   '  ''  '  \n")
print("`-----' `----''--'  '--'.-'  /    `------'  `----' `--'    `----'   \n")
print("                        `---'                                       \n")
print(" \n")

categorya = ["category", "global", "inspect", "network", "peer", "rss", "search", "server", "settings", "tag", "torrent", "tags", "tracker", "web-seeds"]

a = [
    "0:  category   (X)",
	"1:  global     (0)",
	"2:  inspect    (X)",
	"3:  network    (X)",
	"4:  peer       (X)",
	"5:  rss        (X)",
	"6:  search     (X)",
	"7:  server     (0)",
	"8:  settings   (X)",
	"9:  tag        (X)",
	"10: torrent    (X)",
	"11: tags       (X)",
	"12: tracker    (X)",
	"13: web-seeds  (X)"
    ]

print("X-el jeloltek jelenleg nincsenek definialva")
print("0 jeloltek hianyosak")
print(*a, sep = "\n" )
print("\n")

start_cat = categorya[int(input("Enter a Number: "))]

#############################################################################################
if start_cat == categorya[0]:
    print("category")

    categorya_lista = ["add", "delete", "list", "set"]

    a = [
        "0:  add",
	    "1:  delete",
	    "2:  list",
	    "3:  set"
        ]

    print("X-el jeloltek jelenleg nincsenek definialva")
    print(*a, sep = "\n" )
    print("\n")
    category_list = categorya_lista[int(input("Enter a Number: "))]

#-------------------------------------------
    if category_list == categorya_lista[0]:
        #qbt category add [arguments] [options]
        
        #Arguments
        #<NAME>	Category name.

        #Options
        #Option	Description
        #--save-path <PATH> -s <PATH>	The save path for the category. Requires qBittorrent 4.1.3 or later.
        #--url <SERVER_URL>	QBittorrent Server URL
        #--username <USERNAME>	User name
        #--password <PASSWORD>	User password
        #--ask-for-password	Ask the user to enter a password in a secure way.
        #--help -h -?	Show help information
        print("add")
        
        
    if category_list == categorya_lista[1]:
        #bt category delete [arguments] [options]
        
        #Arguments
        #Argument	Description
        #<NAME_1 NAME_2 ... NAME_N>	The names of categories to delete.

        #Options
        #Option	Description
        #--url <SERVER_URL>	QBittorrent Server URL
        #--username <USERNAME>	User name
        #--password <PASSWORD>	User password
        #--ask-for-password	Ask the user to enter a password in a secure way.
        #--help -h -?	Show help information
        print("delete")
        

    if category_list == categorya_lista[2]:
        #qbt category list [options]
        
        #Options
        #Option	Description
        #--format <LIST_FORMAT> -F <LIST_FORMAT>	Output format: table | list | csv | json
        #--url <SERVER_URL>	QBittorrent Server URL
        #--username <USERNAME>	User name
        #--password <PASSWORD>	User password
        #--ask-for-password	Ask the user to enter a password in a secure way.
        #--help -h -?	Show help information
        print("list")
        

    if category_list == categorya_lista[3]:
        #qbt category set [arguments] [options]

        #Arguments
        #Argument	Description
        #<NAME>	Category name.

        #Options
        #Option	Description
        #--save-path <PATH> -s <PATH>	The save path for the category. Can be an empty string.
        #--url <SERVER_URL>	QBittorrent Server URL
        #--username <USERNAME>	User name
        #--password <PASSWORD>	User password
        #--ask-for-password	Ask the user to enter a password in a secure way.
        #--help -h -?	Show help information
        print("set")
        
        
#-------------------------------------------

#############################################################################################

#############################################################################################
if start_cat == categorya[1]:
    print("global")

    global_lista = ["info", "limit", "save-path"]

    a = [
        "0:  info       ",
	    "1:  limit      (X)",
	    "2:  save-path  (X)"
        ]

    print("X-el jeloltek jelenleg nincsenek definialva")
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
        


    if global_list == global_lista[1]:
        #qbt global limit [options] [command]

        #Options
        #Option	Description
        #--url <SERVER_URL>	QBittorrent Server URL
        #--username <USERNAME>	User name
        #--password <PASSWORD>	User password
        #--ask-for-password	Ask the user to enter a password in a secure way.
        #--help -h -?	Show help information

        #Commands
        #Command	Aliases	Description
        #alternative		Enables/disables alternative speed mode.
        #download		Gets or sets global download speed limit.
        #upload		Gets or sets global upload speed limit.
        print("limit")
        

    if global_list == global_lista[2]:
        #qbt global limit [options] [command]
        
        #Options
        #Option	Description
        #--url <SERVER_URL>	QBittorrent Server URL
        #--username <USERNAME>	User name
        #--password <PASSWORD>	User password
        #--ask-for-password	Ask the user to enter a password in a secure way.
        #--help -h -?	Show help information

        #Commands
        #Command	Aliases	Description
        #alternative		Enables/disables alternative speed mode.
        #download		Gets or sets global download speed limit.
        #upload		Gets or sets global upload speed limit.
        print("save-path")  
#############################################################################################

#############################################################################################
if start_cat == categorya[2]:
    print("inspect")
#############################################################################################

#############################################################################################
if start_cat == categorya[3]:
    print("network")
#############################################################################################

#############################################################################################
if start_cat == categorya[4]:
    print("peer")
#############################################################################################

#############################################################################################
if start_cat == categorya[5]:
    print("rss")
#############################################################################################

#############################################################################################
if start_cat == categorya[6]:
    print("search")
#############################################################################################

#############################################################################################
if start_cat == categorya[7]:

    print("server")
    server_list = ["info", "log", "settings"]

    a = [
        "0:  info      ",
	    "1:  log       ",
	    "2:  settings  (X)"
        ]

    print("X-el jeloltek jelenleg nincsenek definialva")
    print(*a, sep = "\n" )
    print("\n")

    global_server_list = server_list[int(input("Enter a Number: "))]

    if global_server_list == server_list[0]: #Szerver info
        x = "qbt server info"
        logfile = " > C://temp//server_info.txt"
        b = x + connections
        print("qbt server info")
        os.system(b + logfile)
        os.system(b)


    if global_server_list == server_list[1]: #szerver log
        x = "qbt server log"
        log_form = " --severity "
        server_log = ["all", "normal", "info", "warning", "critical"]
        a = [
            "0:  ALL",
	        "1:  NORMAL",
	        "2:  INFO",
            "3:  WARNING",
            "4:  CRITICAL"
            ]

        print("X-el jeloltek jelenleg nincsenek definialva")
        print(*a, sep = "\n" )
        print("\n")

        server_list_log = server_log[int(input("Enter a Number: "))]
        y = x + log_form + server_list_log + connections

        print("qbt server log")
        logfile = " > C://temp//server_log.txt"
        os.system(y + logfile)
        os.system(y)

    if global_server_list == server_list[2]:
        print("settings")

#############################################################################################

#############################################################################################
if start_cat == categorya[8]:
    print("settings")
#############################################################################################

#############################################################################################
if start_cat == categorya[9]:
    print("tag")
#############################################################################################

#############################################################################################
if start_cat == categorya[10]:
    print("torrent")
#############################################################################################

#############################################################################################
if start_cat == categorya[11]:
    print("tags")
#############################################################################################

#############################################################################################
if start_cat == categorya[12]:
    print("tracker")
#############################################################################################

#############################################################################################
if start_cat == categorya[13]:
    print("web-seeds")

#############################################################################################


