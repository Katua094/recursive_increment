import os


destination="C:\\Users\\Admin\\OneDrive\\Desktop\\wow post"


try:
    os.rmdir(destination)

except FileNotFoundError:
    print("file does not exist bro!!")

