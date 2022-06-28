#server or torrent

a = ""
log = ["server", "torrent"]
server = "qbt"
variant = ["info", "log"]
server_var = ""
log_stats = ""

a = [
    "0 :server",
    "1 :torrent"
    ]

print(*a, sep = "\n" )
print("\n")


log_list = log[int(input("Enter a Number: "))]




if log_list == log[0]:
    b = [
        "0 :info",
        "1 :log"
        ]
    print(*b, sep = "\n" )
    print("\n")
    server_var = variant[int(input("Enter a Number: "))]
    #print(server_var)


#print("{0} {1} {2}".format(server, log_list, server_var))
log_stats = ("{0} {1} {2}".format(server, log_list, server_var))
