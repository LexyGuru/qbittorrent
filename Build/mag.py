import os
import category_modul_category
import category_modul_server


class auth:

################################################################################

    def login():

        global connections
        login = ["login", "login_file", "exit"]
        a = [
            "0 :login",
            "1 :login_file",
            "2 :exit"
            ]
    
        print(*a, sep = "\n" )
        print("\n")

        qbit_api_var = login[int(input("Enter a Number: "))]

        if qbit_api_var == login[0]:
            url     = input("url   :")
            user    = input("user  :")
            passwd  = input("passwd:")
            auth_url    = " --url " 
            auth_user   = " --username " 
            auth_passwd = " --password "
            connections = auth_url + url + auth_user + user + auth_passwd + passwd
            f = open("C://temp//auth_log.txt", "w")
            f.write(connections)
            f.close()

        if qbit_api_var == login[1]:
            with open('C://temp//auth_log.txt') as f:
                connections = f.read()
        #print(connections)

        if qbit_api_var == login[2]:
            print("bye")

################################################################################

class modul:
    global modul
    def __init__(self):
        print()

    def back():
        back = ["Start", "Back"]
        a = [
            "0 :Start",
            "1: Back"
            ]
           
        print(*a, sep = "\n" )
        print("\n")
        cate_var = back[int(input("Enter a Number: "))]

        if cate_var == back[0]:
                import logo
                print("")

        if cate_var == back[1]:
                print("back")
                modul.category()

    def backa():
                import logo
                modul.category()

################################################################################

    def category():
        global categorya
        categorya = ["category","global","inspect","network","peer","rss","search","server","settings","tag","torrent","tags","tracker","web-seeds", "", "EXIT"]
        a = [
	        "0  :category",
	        "1  :global",
	        "2  :inspect",
	        "3  :network",
	        "4  :peer",
	        "5  :rss",
	        "6  :search",
	        "7  :server",
	        "8  :settings",
	        "9  :tag",
	        "10 :torrent",
	        "11 :tags",
	        "12 :tracker",
	        "13 :web-seeds",
                "",
                "15 :EXIT"
	        ]
    
        print(*a, sep = "\n" )
        print("\n")

        categorya_var = categorya[int(input("Enter a Number: "))]

        if categorya_var == categorya[0]:#1111
                print("category")
                category_modul_category.modul_category.kategory()

        if categorya_var == categorya[1]:#1111 
                print("global")
                modul.back()

        if categorya_var == categorya[2]:#1111
                print("inspect")
                modul.back()

        if categorya_var == categorya[3]:#1111
                print("network")
                modul.back()

        if categorya_var == categorya[4]:#1111
                print("peer")
                modul.back()

        if categorya_var == categorya[5]:#1111
                print("rss")
                modul.back()

        if categorya_var == categorya[6]:#1111
                print("search")
                modul.back()

        if categorya_var == categorya[7]:#1111
                print("server")
                modul.back()
                server_modul_category = ["info", "log", "settings"]

                a = [
                "0:  info       ",  
                "1:  log       (X)",
	        "2:  settings  (X)"
                ]

                print(*a, sep = "\n" )
                print("\n")

                serverlist = server_modul_category[int(input("Enter a Number: "))]

                if serverlist == server_modul_category[0]:
                        category_modul_server.modul_category.server_info()

                if serverlist == server_modul_category[1]:
                        category_modul_server.modul_category.server_log()

                if serverlist == server_modul_category[2]:
                        category_modul_server.modul_category.server_settings()
                


        if categorya_var == categorya[8]:#1111
                print("settings")
                modul.back()

        if categorya_var == categorya[9]:#1111
                print("tag")
                modul.back()

        if categorya_var == categorya[10]:#1111
                print("torrent")
                modul.back()

        if categorya_var == categorya[11]:#1111
                print("tags")
                modul.back()

        if categorya_var == categorya[12]:#1111
                print("tracker")
                modul.back()

        if categorya_var == categorya[13]:#1111
                print("web-seeds")
                modul.back()

        if categorya_var == categorya[14]:#1111
                modul.backa()

        if categorya_var == categorya[15]:#1111
                exit


authh = auth
modull = modul

