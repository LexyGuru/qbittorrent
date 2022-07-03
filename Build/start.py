import logo
import mag
from mag import *
import pathlib


file = pathlib.Path("C://temp//auth_log.txt")

if file.exists ():
    modul.category()
else:
    auth.login()
    with open('C://temp//auth_log.txt') as f:
        connections = f.read()
    modul.category()


