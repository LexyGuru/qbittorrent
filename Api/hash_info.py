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

word  = 'infohash_v1'
world = 'name'

with open(r'C://temp//torrent_log.json', 'r') as fp:
# read all lines in a list
    lines = fp.readlines()
    for line in lines:
    # check if string present on a current line
        if line.find(word)  != -1:
            print(line)

        if line.find(world)  != -1:
            print(line)
