
import os


#QBIT ALAP INFO
url     = input("url   :")
user    = input("user  :")
passwd  = input("passwd:")
auth_url    = " --url " 
auth_user   = " --username " 
auth_passwd = " --password "
connections = auth_url + url + auth_user + user + auth_passwd + passwd

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
        "2 :settings"
        ]
    print(*a, sep = "\n" )
    print("\n")
    qbit_api_var = variant[int(input("Enter a Number: "))]

    #login info
    #qbt server info [options]
    if qbit_api_var == variant[0]:
        info = "qbt server info "
        #print(info + connections)
        os.system(info + connections)

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
    print("torrent")
    

if qbit_api_var == serv_var[2]:
    print("bye")





