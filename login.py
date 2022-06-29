print(" \n")
print(" \n")                                                                                                                                         
print(",--.                              ,----.                            \n")
print("|  |    ,---. ,--.  ,--.,--. ,--.'  .-./   ,--.,--.,--.--.,--.,--.  \n")
print("|  |   | .-. : \  `'  /  \  '  / |  | .---.|  ||  ||  .--'|  ||  |  \n")
print("|  '--.\   --. /  /.  \   \   '  '  '--'  |'  ''  '|  |   '  ''  '  \n")
print("`-----' `----''--'  '--'.-'  /    `------'  `----' `--'    `----'   \n")
print("                        `---'                                       \n")
print(" Qbittorrent python script  \n")
print("   \n")

print("Connection: server auth")
print("")
print("legelso alakllomal sima login")
print("utanna hasznalhatod a login_file valtozot")
print("\n")
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