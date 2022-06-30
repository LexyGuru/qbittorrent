import mag
from mag import * 

#qbt category add [arguments] [options]
#qbt category create [arguments] [options]

#Arguments
#Argument	Description
#<NAME>	Category name.

#Options
#Option	Description
#--save-path <PATH> -s <PATH>	The save path for the category. Requires qBittorrent 4.1.3 or later.
#--url <SERVER_URL>	QBittorrent Server URL
#--username <USERNAME>	User name
#--password <PASSWORD>	User password
#--ask-for-password	Ask the user to enter a password in a secure way.
#--help -h -?	Show help information


class modul_category:
    
        def kategory():
                kategorys = ["add","delete","list","set"]
                a = [
	                "0  :add",
	                "1  :delete",
	                "2  :list",
	                "3  :set"
	                ]
                print(*a, sep = "\n" )
                print("\n")            
                
                kat_var = kategorys[int(input("Enter a Number: "))]

                if kat_var == kategorys[0]:#2222
                    print("add")

                    x = "qbt category add "

                    print("Requires qBittorrent 4.1.3 or later.")
                    locations = input("Add to locations: ")  #//location part
                    cat_name = input("Category name: ")

                    categ_add = x + "--save-path " + cat_name + " " + locations +  connections
                    os.system(categ_add)
                    mag.modul.back()

                if kat_var == kategorys[1]:#2222
                    print("delete")
                    mag.modul.back()
            
                if kat_var == kategorys[2]:#2222
                    print("list")
                    mag.modul.back()
            
                if kat_var == kategorys[3]:#2222
                    print("set")
                    mag.modul.back()

#modul_category.kategory()