#Filter by status: all | downloading | seeding | completed | paused | resumed | active | inactive | errored | stalled | stalledDownloading | stalledUploading
a = ""
torrent = ["all", "downloading", "seeding", "completed", "paused", "resumed", "active", "inactive", "errored", "stalled", "stalledDownloading", "stalledUploading"]

a = [
    "0 :all",
    "1 :downloading",
    "2 :seeding",
    "3 :completed",
    "4 :paused",
    "5 :resumed",
    "6 :active",
    "7 :inactive",
    "8 :errored",
    "9 :stalled",
    "10:stalledDownloading",
    "11stalledUploading"
    ]
print(*a, sep = "\n" )
print("\n")
torrent_list = torrent[int(input("Enter a Number: "))]
print(torrent_list)
