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
qbittorrent_cli = "bitsadmin /transfer debjob /download /priority HIGH  https://github.com/fedarovich/qbittorrent-cli/releases/download/v1.7.22127.1/qbittorrent-cli-1.7.22127.1-x64.msi C:\\temp\\qbittorrent-cli-1.7.22127.1-x64.msi"

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
    "0 :qbit api/cli  install",
    "1 :Van"
    ]
print(*a, sep = "\n" )
print("\n")

downloads_qbit_api_var = downloads_api[int(input("Enter a Number: "))]

if downloads_qbit_api_var == downloads_api[0]:
    a = [
    "0 :API/CLI  install",
    "1 :CLI install",
    "2 :API install",
    "3 :Exit"
    ]

    qbit_api_cli = ["API/CLI  install", "CLI install", "API install", "Exit"]
    
    print(*a, sep = "\n" )
    print("\n")
    qbit_api_var = qbit_api_cli[int(input("Enter a Number: "))]

    if qbit_api_var == qbit_api_cli[0]:
        print("Install API")
        api = "pip install --upgrade --force-reinstall qbittorrent-api"
        os.system(api)

        print("Download + CLI install")
        os.system(qbittorrent_cli)
        qbittorrent_cli_i = "C:\\temp\\qbittorrent-cli-1.7.22127.1-x64.msi"
        os.system(qbittorrent_cli_i)
    
    if qbit_api_var == qbit_api_cli[1]:
        print("Download + CLI install")
        os.system(qbittorrent_cli)
        qbittorrent_cli_i = "C:\\temp\\qbittorrent-cli-1.7.22127.1-x64.msi"
        os.system(qbittorrent_cli_i)

    if qbit_api_var == qbit_api_cli[2]:
        print("Install API")
        api = "pip install --upgrade --force-reinstall qbittorrent-api"
        os.system(api)

    if qbit_api_var == qbit_api_cli[3]:
        print("bye")

if downloads_qbit_api_var == downloads_api[1]:
    print("bye")
