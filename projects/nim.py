import os

path="C:\\Users\\Admin\\OneDrive\\Desktop\\bola.txt"

if os.path.isdir(path):
    print("There is a directory")
else:
    print("Nop")

if os.path.isfile(path):
    print("It is a file !!")
if os.path.exists(path):
    print("it exists")