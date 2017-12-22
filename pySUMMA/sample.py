import sys
import os

print("If there is decision file in the current directory, you need to write 'filename.txt'. However there is another folder inside the current directory, you have to write 'foldername/filename.txt'")
user_input = raw_input("Enter the path of your file: ")

assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input,'r+')
print("Hooray we found your file!")
#stuff you do with the file goes here
f.close()