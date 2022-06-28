#Auth server connection

url     = input("url   :")
user    = input("user  :")
passwd  = input("passwd:")
auth_url    = " --url " 
auth_user   = " --username " 
auth_passwd = " --password "

connections = auth_url + url + auth_user + user + auth_passwd + passwd
#print(auth_url + url + auth_user + user + auth_passwd + passwd)
