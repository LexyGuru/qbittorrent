class auth:

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

class modul:
    def __init__(self):
        print()

    def back():
        categorya = ["Start", "Back"]
        a = [
            "0 :Start",
            "1: Back"
            ]
           
        print(*a, sep = "\n" )
        print("\n")
        cate_var = categorya[int(input("Enter a Number: "))]

        if cate_var == categorya[0]:
            print("")

        if cate_var == categorya[1]:
            print("back")
            modul.category()

    def category():
        
        global categorya
        categorya = ["category","global","inspect","network","peer","rss","search","server","settings","tag","torrent","tags","tracker","web-seeds"]
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
	        "13 :web-seeds"
	        ]
    
        print(*a, sep = "\n" )
        print("\n")

        categorya_var = categorya[int(input("Enter a Number: "))]

        if categorya_var == categorya[0]:
            print("category")
            modul.back()
            categorya = ["add","delete","list","set"]
            a = [
	            "0  :add",
	            "1  :delete",
	            "2  :list",
	            "3  :set"
	            ]
            print(*a, sep = "\n" )
            print("\n")

            categ_var = categorya[int(input("Enter a Number: "))]
            if categ_var == categorya[0]:
                print("add")
                modul.back()


            if categ_var == categorya[1]:
                print("delete")
                modul.back()
            
            if categ_var == categorya[2]:
                print("list")
                modul.back()
            
            if categ_var == categorya[3]:
                print("set")
                modul.back()

        if categorya_var == categorya[1]:
            print("global")
            modul.back()

        if categorya_var == categorya[2]:
            print("inspect")
            modul.back()

        if categorya_var == categorya[3]:
            print("network")
            modul.back()

        if categorya_var == categorya[4]:
            print("peer")
            modul.back()

        if categorya_var == categorya[5]:
            print("rss")
            modul.back()

        if categorya_var == categorya[6]:
            print("search")
            modul.back()

        if categorya_var == categorya[7]:
            print("server")
            modul.back()

        if categorya_var == categorya[8]:
            print("settings")
            modul.back()

        if categorya_var == categorya[9]:
            print("tag")
            modul.back()

        if categorya_var == categorya[10]:
            print("torrent")
            modul.back()

        if categorya_var == categorya[11]:
            print("tags")
            modul.back()

        if categorya_var == categorya[12]:
            print("tracker")
            modul.back()

        if categorya_var == categorya[13]:
            print("web-seeds")
            modul.back()

authh = auth
modull = modul

