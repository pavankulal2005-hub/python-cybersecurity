#program 08
#find count of particular file type in a directory
import os
path = input("enter file path:")
count = 0
for file in os.listdir(path):
 if file.endswith(".exe"):
   count+=1
   print(".exe files found",count)