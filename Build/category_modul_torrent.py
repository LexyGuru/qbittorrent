#	[ ]add
#		[ ]file
#		[ ]url
#	[ ]category
#	[ ]check
#	[ ]content
#	[ ]delete
#	[ ]file
#		[ ]list
#		[ ]priority
#		[ ]rename
#	[ ]limit
#		[ ]download
#		[ ]upload
#	[X]list
#	[ ]move
#	[ ]options
#	[ ]pause
#	[ ]peer
#		[ ]add
#		[ ]list
#	[ ]peers
#	[ ]pieces
#	[ ]priority
#		[ ]down
#		[ ]max
#		[ ]min
#		[ ]up
#	[ ]properties
#	[ ]reannounce
#	[ ]rename
#	[ ]resume
#	[ ]share
#

from multiprocessing import connection
import mag
from mag import *
import os


class torrent_var():
    global connections
    def torrent_add():
        mag.modul.backa()

    def torrent_category():
        mag.modul.backa()

    def torrent_check():
        mag.modul.backa()

    def torrent_content():
        mag.modul.backa()

    def torrent_delete():
        mag.modul.backa()

    def torrent_file():
        mag.modul.backa()

    def torrent_limit():
        mag.modul.backa()

    def torrent_list():
        print("Torrent List")
        mag.modul.back()

        with open('C://temp//auth_log.txt') as f:
            connections = f.read()
        #qbt torrent list [options]
        
        #Options
        #Option	Description
        #--verbose	Displays verbose information.
        #--filter <STATUS> -f <STATUS>	Filter by status: all | downloading | seeding | completed | paused | resumed | active | inactive | errored | stalled | stalledDownloading | stalledUploading
        #--category <CATEGORY> -c <CATEGORY>	Filter by category.
        #--sort <PROPERTY> -s <PROPERTY>	Sort by property.
        #--reverse  -r	Reverse the sort order.
        #--limit <LIMIT> -l <LIMIT>	Number of torrents to display.
        #--offset <OFFSET> -o <OFFSET>	Offset from the beginning of the list.
        #--format <LIST_FORMAT> -F <LIST_FORMAT>	Output format: table | list | csv | json
        #--url <SERVER_URL>	QBittorrent Server URL
        #--username <USERNAME>	User name
        #--password <PASSWORD>	User password
        #--ask-for-password	Ask the user to enter a password in a secure way.
        #--help -h -?	Show help information

       
        #Filter by status: all | downloading | seeding | completed | paused | resumed | active | inactive | errored | stalled | stalledDownloading | stalledUploading
        torrent_list_filter_var = ["all", "downloading", "seeding", "completed", "paused", "resumed", "active", "inactive", "errored", "stalled", "stalledDownloading", "stalledUploading"]
        xa =[
            "[ 0  ] :all",
            "[ 1  ] :downloading",
            "[ 2  ] :seeding",
            "[ 3  ] :completed",
            "[ 4  ] :paused",
            "[ 5  ] :resumed",
            "[ 6  ] :active",
            "[ 7  ] :inactive",
            "[ 8  ] :errored",
            "[ 9  ] :stalled",
            "[ 10 ] :stalledDownloading",
            "[ 11 ] :stalledUploading"
            ]
        print(*xa, sep = "\n" )
        print("\n")
        torrent_list_filter_varr = torrent_list_filter_var[int(input("Enter a Number: "))]
        torrent_listfilter = (" --filter " + torrent_list_filter_varr)

        torrent_list_format_var = ["table", "list", "csv", "json"]

        a =[
            "[ 0  ] :table",
            "[ 1  ] :list",
            "[ 2  ] :csv",
            "[ 3  ] :json"
            ]
        print(*a, sep = "\n" )
        print("\n")

        torrent_list_format_varr = torrent_list_format_var[int(input("Enter a Number: "))]

        if torrent_list_format_varr == torrent_list_format_var[0]:
            torrent_listformat = (" --format " + torrent_list_format_varr)
            logfile = " > C://temp//torrent_list_table.txt"

            #print("qbt torrent list " + torrent_listfilter + torrent_listformat + connections + logfile)
            #print(torrent_listfilter + torrent_listformat + logfile)
            os.system("qbt torrent list " + torrent_listfilter + torrent_listformat + connections)
            os.system("qbt torrent list " + torrent_listfilter + torrent_listformat + connections + logfile)
        
        if torrent_list_format_varr == torrent_list_format_var[1]:
            torrent_listformat = (" --format " + torrent_list_format_varr)
            logfile = " > C://temp//torrent_list_list.txt"

            #print("qbt torrent list " + torrent_listfilter + torrent_listformat + connections + logfile)
            #print(torrent_listfilter + torrent_listformat + logfile)
            os.system("qbt torrent list " + torrent_listfilter + torrent_listformat + connections )
            os.system("qbt torrent list " + torrent_listfilter + torrent_listformat + connections + logfile)
        
        if torrent_list_format_varr == torrent_list_format_var[2]:
            torrent_listformat = (" --format " + torrent_list_format_varr)
            logfile = " > C://temp//torrent_list_csv.csv"

            #print("qbt torrent list " + torrent_listfilter + torrent_listformat + connections + logfile)
            os.system("qbt torrent list " + torrent_listfilter + torrent_listformat + connections )
            os.system("qbt torrent list " + torrent_listfilter + torrent_listformat + connections + logfile)
    
        if torrent_list_format_varr == torrent_list_format_var[3]:
            torrent_listformat = (" --format " + torrent_list_format_varr)
            logfile = " > C://temp//torrent_list_json.json"

            #print("qbt torrent list " + torrent_listfilter + torrent_listformat + connections + logfile)
            os.system("qbt torrent list " + torrent_listfilter + torrent_listformat + connections )
            os.system("qbt torrent list " + torrent_listfilter + torrent_listformat + connections + logfile)

        mag.modul.backa()
                


    def torrent_move():
        mag.modul.backa()

    def torrent_pause():
        mag.modul.backa()

    def torrent_pause():
        mag.modul.backa()

    def torrent_peer():
        mag.modul.backa()

    def torrent_peers():
        mag.modul.backa()

    def torrent_pieces():
        mag.modul.backa()

    def torrent_priority():
        mag.modul.backa()

    def torrent_properties():
        mag.modul.backa()

    def torrent_reannounce():
        mag.modul.backa()

    def torrent_rename():
        mag.modul.backa()

    def torrent_resume():
        mag.modul.backa()

    def torrent_share():
        mag.modul.backa()
