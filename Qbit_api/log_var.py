variant = " "
server_var = ""

b = [
    "0 :info",
    "1 :log"
    ]
print(*b, sep = "\n" )
print("\n")
server_var = b[int(input("Enter a Number: "))]

print(server_var)


