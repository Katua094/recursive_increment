import os

path="C:\\Users\\Admin\\OneDrive\\Desktop\\bola.txt"

if os.path.isdir(path):
    print("it is thre my guy")
elif os.path.isfile(path):
    print("it is a file nigga")
elif os.path.exists(path):
    print("it is real my nigga")