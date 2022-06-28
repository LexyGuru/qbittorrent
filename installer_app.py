import os

print(" \n")
print(" \n")                                                                                                                                         
print(",--.                              ,----.                            \n")
print("|  |    ,---. ,--.  ,--.,--. ,--.'  .-./   ,--.,--.,--.--.,--.,--.  \n")
print("|  |   | .-. : \  `'  /  \  '  / |  | .---.|  ||  ||  .--'|  ||  |  \n")
print("|  '--.\   --. /  /.  \   \   '  '  '--'  |'  ''  '|  |   '  ''  '  \n")
print("`-----' `----''--'  '--'.-'  /    `------'  `----' `--'    `----'   \n")
print("                        `---'                                       \n")
print(" Qbittorrent api python script  \n")
print(" Instalation api + Qbittorrent + Script  \n")


downloads_qbit = ["Qbittorrent", "Qbittorenx64", "none"]

a = [
    "0 :Qbittorrent install",
    "1 :Qbittorenx64 install",
    "2 :Van"
    ]
print(*a, sep = "\n" )
print("\n")

downloads_qbit_var = downloads_qbit[int(input("Enter a Number: "))]


x32 = "bitsadmin /transfer debjob /download /priority HIGH https://sourceforge.net/projects/qbittorrent/files/qbittorrent-win32/qbittorrent-4.4.3.1/qbittorrent_4.4.3.1_setup.exe/download C:\\temp\\qbittorrent_4.4.3.1_setup.exe"
x64 = "bitsadmin /transfer debjob /download /priority HIGH https://sourceforge.net/projects/qbittorrent/files/qbittorrent-win32/qbittorrent-4.4.3.1/qbittorrent_4.4.3.1_x64_setup.exe/download C:\\temp\\qbittorrent_4.4.3.1_x64_setup.exe"


if downloads_qbit_var == downloads_qbit[0]:
    os.system(x32)
    print("qbittorrent_4.4.3.1 install")
    install = "C:\\temp\\qbittorrent_4.4.3.1_setup.exe"
    os.system(install)
    

if downloads_qbit_var == downloads_qbit[1]:
    os.system(x64)
    print("qbittorrent_4.4.3.1_x64 install")
    install = "C:\\temp\\qbittorrent_4.4.3.1_x64_setup.exe"
    os.system(install)

if downloads_qbit_var == downloads_qbit[2]:
    print("")


downloads_api = ["qbit api", "none"]
a = [
    "0 :qbit api install",
    "1 :Van"
    ]
print(*a, sep = "\n" )
print("\n")

downloads_qbit_api_var = downloads_api[int(input("Enter a Number: "))]

if downloads_qbit_api_var == downloads_api[0]:
    print("Install API")
    #api  = "pip install qbittorrent-api"
    api = "pip install --upgrade --force-reinstall qbittorrent-api"
    os.system(api)

if downloads_qbit_api_var == downloads_api[1]:
    print("bye")
