
import os
directory = os.getcwd()
#used to obtain the current working directory (cwd) and assign it to the variable directory


file_list = []
#retrieve information about files in the current working directory.


for file in os.listdir(directory): #his loop iterates over the files in the directory 
    file_size = os.path.getsize(file) #size of the file in bytes
    mod_time = os.path.getmtime(file) #last modification time of the file, obtained 
    creation_time = os.path.getctime(file) #creation time of the file
    file_path = os.path.realpath(file)   
    file_list.append({'name': file, 'size': file_size, 'mod time':mod_time, 'path': file_path})
    

print(file_list, sep="\n")
 #By setting sep="\n", the items will be printed on separate lines.
