import os


#QBIT ALAP INFO

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

serv_var = ""
server = ""
torrent = ""


#--url <SERVER_URL>	QBittorrent Server URL
#--username <USERNAME>	User name
#--password <PASSWORD>	User password


#category		Manage categories.
#global		Gets or sets global qBittorrent settings.
#inspect		Inspects the torrent.
#network		Configure network settings, credentials, etc.
#peer	peers	Manages the peers.
#rss		Manages RSS feeds and rules.
#search		Searches torrents on the trackers.
#server		Manage qBittorrent server.
#settings		Gets or sets this application's settings.
#tag	tags	Manages the tags.
#torrent		Manage torrents.


serv_var = ["server", "torrent", "exit"]

a = [
    "0 :server",
    "1 :torrent",
    "2 :exit"
    ]
print(*a, sep = "\n" )
print("\n")

qbit_api_var = serv_var[int(input("Enter a Number: "))]

if qbit_api_var == serv_var[0]:
    #qbt server [options] [command]
    #info		Gets the qBittorrent server info.
    #log		Gets the qBittorrent log.
    #settings		Manage qBittorrent server settings.
    variant = ["info", "log", "settings"]
    a = [
        "0 :info",
        "1 :log",
        "2 :settings (X)"
        ]
    print("X-el jeloltek nem mukodnek")
    print(*a, sep = "\n" )
    print("\n")
    qbit_api_var = variant[int(input("Enter a Number: "))]

    #login info
    #qbt server info [options]
    if qbit_api_var == variant[0]:
        info = "qbt server info "
        #print(info + connections)
        logfile = " > C://temp//server_log.txt"
        os.system(info + connections + logfile)
        osCommandString = "notepad.exe C://temp//server_log.txt"
        os.system(osCommandString)

    #login log
    #qbt server log [options]
    if qbit_api_var == variant[1]:
        log = "qbt server log "
        variant = ["normal", "info", "warning", "critical", "all"]
        a = [
            "0 :NORMAL",
            "1 :INFO",
            "2 :WARNING",
            "3 :CRITICAL",
            "4 :ALL"
            ]
        print(*a, sep = "\n" )
        print("\n")

        qbit_api_var = variant[int(input("Enter a Number: "))]
        #--severity <S1,S2,...,SN> 
        # -s <S1,S2,...,SN>	Comma separated list of severities to display (NORMAL,INFO,WARNING,CRITICAL) or ALL
       
        log_var = "--severity " + qbit_api_var

        print(log + log_var + connections)
        os.system(log + log_var + connections)

    #login settings
    #qbt server settings [options] [command]
    if qbit_api_var == variant[2]:
        
        #Command	Aliases	Description
        #authentication	auth	Manages authentication settings.
        #auto-tmm	autotmm	Manages automatic torrent management mode (Auto TMM).
        #connection		Manages connection settings.
        #dns		Manages dynamic DNS settings.
        #downloads		Manages folders and options for downloads.
        #email	e-mail
        #mail	Manages e-mail notifications.
        #ip-filter	ipfilter	Manages IP filter.
        #monitored-folder	monitoredfolder
        #mf	Manages monitored folders.
        #privacy		Manages BitTorrent privacy settings.
        #proxy		Manages proxy settings.
        #queue		Manages BitTorrent queueing settings.
        #seeding		Manages BitTorrent seeding settings.
        #speed		Manages speed limits.
        #tracker		Manages additional trackers.
        #web		Manages web UI and API settings.
        print("Jelenleg nincs definialva")


if qbit_api_var == serv_var[1]:
    #Command	Aliases	Description
    #add		Adds new torrents.
    #category		Sets the torrent category.
    #check		Rechecks the torrent.
    #content		Shows the torrent content. Alias for "torrent file list"
    #delete		Deletes the torrent.
    #file		Gets and manipulates torrent contents.
    #limit		Gets or sets download and upload speed limits.
    #list		Shows the torrent list.
    #move		Moves the downloaded files to the other folder.
    #options		Sets torrent options.
    #pause		Pauses the specified torrent or all torrents.
    #peer		Manages torrent peers.
    #peers		Show the list of torrent peers.
    #pieces		Shows the torrent pieces' hashes and states.
    #priority		Changes torrent priority.
    #properties		Shows the torrent properties.
    #reannounce		Reannounces the torrent.
    #rename		Renames the torrent.
    #resume		Resumes the specified torrent or all torrents.
    #share	sharing
    #seeding	Manages torrent sharing limits.
    #tags	tag	Manages the torrent tags.
    #tracker		Gets or adds torrent trackers.
    #web-seeds	webseeds
    #ws	Shows the torrent web seeds.

    variant = ["check", "pause", "list"]
    a = [
        "0 :check (X)"
        "1 :pause (X)",
        "2 :list"
        ]
    print(*a, sep = "\n" )
    print("\n")
    qbit_api_var = variant[int(input("Enter a Number: "))]
    if qbit_api_var == variant[0]:
        print("Check torrent")
        print("Open log file // C:/temp/torrent_log.json //")
        print("Tipe (HASH) ")
        #qbt torrent check [arguments] [options]
        #fil = "qbt torrent list --filter "
        #logfile = " > C://temp//torrent_log.json"
        #os.system(fil + qbit_api_var + " --format json" + connections + logfile)
        #osCommandString = "notepad.exe C://temp//torrent_log.json"
        #Sos.system(osCommandString)

        # file hash 



    if qbit_api_var == variant[1]:
        print("asdasd")
        #fil = "qbt torrent list --filter "
        #logfile = " > C://temp//torrent_log.json"
        #os.system(fil + qbit_api_var + " --format json" + connections + logfile)
        #osCommandString = "notepad.exe C://temp//torrent_log.json"
        #Sos.system(osCommandString)

        # file hash 

    if qbit_api_var == variant[2]:
        #print("list")
        #--filter <STATUS>	Filter by status: all | downloading | seeding | completed | paused | resumed | active | inactive | errored | stalled | stalledDownloading | stalledUploading
        variant = ["all", "downloading", "seeding", "completed", "paused", "resumed", "active", "inactive", "errored", "stalled", "stalledDownloading", "stalledUploading"]
        a = [
            "0  :all"
            "1  :downloading" 
            "2  :seeding"
            "3  :completed"
            "4  :paused"
            "5  :resumed"
            "6  :active"
            "7  :inactive"
            "8  :errored"
            "9  :stalled"
            "10 :stalledDownloading"
            "11 :stalledUploading"
            ]
        print(*a, sep = "\n" )
        print("\n")

        

        qbit_api_var = variant[int(input("Enter a Number: "))]
         #--format <LIST_FORMAT> Output format: table | list | csv | json
        fil = "qbt torrent list --filter "
        #print(fil + qbit_api_var + " --format table" + connections)

        logfile = " > C://temp//torrent_log.json"
        os.system(fil + qbit_api_var + " --format json" + connections + logfile)
        osCommandString = "notepad.exe C://temp//torrent_log.json"
        os.system(osCommandString)


if qbit_api_var == serv_var[2]:
    print("bye")





