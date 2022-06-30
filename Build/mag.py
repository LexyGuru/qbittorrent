
class language:

    def __init__(self):
        print()

    def magyar(self):
        global a1, a2, a3
        #hungary = ["Csatlakozas", "login_file", "exit"]
        a1 = "Csatlakozas"
        a2 = "Csatlakozas file hasznalataval"
        a3 = "Kilepes"

    def english(self):
        global a1, a2, a3
        a1 = "Connection"
        a2 = "Connection from file"
        a3 = "Exit"


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

        if categorya_var == categorya[1]:
            print("global")

        if categorya_var == categorya[2]:
            print("inspect")
            
        if categorya_var == categorya[3]:
            print("network")
            
        if categorya_var == categorya[4]:
            print("peer")
            
        if categorya_var == categorya[5]:
            print("rss")
            
        if categorya_var == categorya[6]:
            print("search")
            
        if categorya_var == categorya[7]:
            print("server")
            
        if categorya_var == categorya[8]:
            print("settings")
            
        if categorya_var == categorya[9]:
            print("tag")
            
        if categorya_var == categorya[10]:
            print("torrent")
            
        if categorya_var == categorya[11]:
            print("tags")
            
        if categorya_var == categorya[12]:
            print("tracker")
        
        if categorya_var == categorya[13]:
            print("web-seeds")

            
authh = auth
languages = language()
modull = modul
#languages.magyar()
#languages.english()







