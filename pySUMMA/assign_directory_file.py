import sys
import os

print("If there is decision file in the current directory, you need to write 'filename.txt'. However there is another folder inside the current directory, you have to write 'foldername/filename.txt'")
Decision = raw_input("Enter the path of your file: ")

assert os.path.exists(Decision), "I did not find the file at, "+str(user_input)
f = open(Decision,'r+')
print("we found your file!")
f.close()