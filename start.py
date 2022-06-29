print(" \n")                                                                                                                                         
print(",--.                              ,----.                            \n")
print("|  |    ,---. ,--.  ,--.,--. ,--.'  .-./   ,--.,--.,--.--.,--.,--.  \n")
print("|  |   | .-. : \  `'  /  \  '  / |  | .---.|  ||  ||  .--'|  ||  |  \n")
print("|  '--.\   --. /  /.  \   \   '  '  '--'  |'  ''  '|  |   '  ''  '  \n")
print("`-----' `----''--'  '--'.-'  /    `------'  `----' `--'    `----'   \n")
print("                        `---'                                       \n")
print(" \n")


variant = ["", "info", "warning", "critical", "all"]
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



