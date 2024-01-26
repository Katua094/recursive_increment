#Reading a file with python 

path="C:\\Users\\Admin\\OneDrive\\Desktop\\bola.txt"
with open(path,"r")as file:
  for line in file:
    print(line.strip())