import sys
import os

def AssignDefaultDirectory(Decision_filename_directory):
    assert os.path.exists(Decision_filename_directory), "I did not find the file at, "+str(Decision_filename_directory)
    f = open(Decision_filename_directory,'r+')
    print("we found your file!")
    return Decision_filename_directory

print("If there is decision file in the current directory, you need to write 'filename.txt'. \n"
      "However there is another folder inside the current directory, you have to write 'foldername/filename.txt'.")
Decision_filename_directory = raw_input("Enter the path of your file: ")
AssignDefaultDirectory(Decision_filename_directory)