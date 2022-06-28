#Comma separated list of severities to display (NORMAL,INFO,WARNING,CRITICAL) or ALL

a = ""
b = " --severity "
server = ["all", "normal", "info", "critical", "warning"]

a = [
    "0 :all",
    "1 :normal",
    "2 :info",
    "3 :critical",
    "4 :warning",
    ]
print(*a, sep = "\n" )
print("\n")
server_list = server[int(input("Enter a Number: "))]
serter = b + server_list
print(serter)
