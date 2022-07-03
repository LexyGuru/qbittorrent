#	[x]info
#	[x]log
#	[ ]settings
#		[ ]authentication
#			[ ]whitelist
#				[ ]clear
#				[ ]delete
#				[ ]list
#				[ ]whitelist
#		[ ]auto-tmm
#		[ ]connection
#		[ ]dns
#		[ ]downloads
#		[ ]email
#		[ ]ip-filter
#			[ ]add
#			[ ]clear
#			[ ]delete
#			[ ]list
#		[ ]monitored-folder
#			[ ]add
#			[ ]clear
#			[ ]delete
#			[ ]list
#		[ ]privacy
#		[ ]proxy
#		[ ]queue
#		[ ]seeding
#		[ ]speed
#		[ ]tracker
#			[ ]add
#			[ ]clear
#			[ ]delete
#			[ ]list
#		[ ]web

import mag
from mag import *
import os

class modul_category:

        def server_info():
                with open('C://temp//auth_log.txt') as f:
                        connections = f.read()
                info = "qbt server info "
                logfile = " > C://temp//server_info.txt"

                os.system(info + connections + logfile)
                mag.modul.backa()
    
        def server_log():
                with open('C://temp//auth_log.txt') as f:
                        connections = f.read()

                print("qbt global info")
                x = "qbt global info"
                
                #--format <OBJECT_FORMAT> -F <OBJECT_FORMAT>	Output format: list | csv | json | property
                a = [
                        "[ 0  ] :list",
                        "[ 1  ] :csv",
                        "[ 2  ] :json"]
                print(*a, sep = "\n" )
                print("\n")

                var_list = ["list", "csv", "json"]

                list_mod = var_list[int(input("Enter a Number: "))]
                print("qbt global info")
                logfile = " > C://temp//server_log.txt"
                #print(list_mod)
                a = x + " --format " + list_mod + connections
                os.system(a + logfile)
                mag.modul.backa()

        def server_settings():
            mag.modul.backa()
