### Beginning of v1 for Roger
from timeit import default_timer as timer
start = timer()

import os
from pathlib import Path
from os import scandir
import shutil
import csv
from datetime import datetime, timedelta
import pandas as pd
import fnmatch

os.chdir('C:\\Users\\mcguirt2\\documents\\Python\\')

# Gets Folders w/ trigger file
base1 = Path('C:\\Users\\mcguirt2\\documents\\Python\\test_folder') # Can ask user for initial filepath
list1 = []
with os.scandir(base1) as entries:
    for entry in entries:
        if entry.is_dir() and len(fnmatch.filter(os.listdir(entry), '*.txt')) >= 1:
            basepath1 = Path('C:\\Users\\mcguirt2\\documents\\Python\\test_folder\\' + entry.name)
            #list1.append(entry.name)
            with os.scandir(basepath1) as entries2:
                for entry1 in entries2:
                    if entry1.is_dir():
                        basepath2 = Path('C:\\Users\\mcguirt2\\documents\\Python\\test_folder\\' + entry.name + '\\' + entry1.name)
                        with os.scandir(basepath2) as entries3:
                            for entry2 in entries3:
                                    templist = []
                                    if os.path.exists(basepath2) == True: 
                                        templist.append(entry2.name.lower())
                                        print(templist)
                                        if 'ok.txt' in templist:
                                            list1.append(entry.name) 
                    #if entry.name.endswith(".txt"): #.zip
                        #list1.append(entry.name)
                    #list1.append(templist)
    print(list1)
print('Completed')


#for i in list1:
#    if len(fnmatch.filter(os.listdir(i), '*.txt')) >= 1:
#        print(i)
#print('Completed')

#Gets folders in archive folder
base2 = Path('C:\\Users\\mcguirt2\\documents\\Python\\test_folder2') # Can ask user for archive filepath
list2 = []
with os.scandir(base2) as entries:
    for entry in entries:
        #if entry.is_dir():
            #basepath2 = Path('C:\\Users\\mcguirt2\\documents\\Python\\test_folder2\\' + entry.name)
            #list1.append(entry.name)
            #with os.scandir(basepath2) as entries2:
                #for entry1 in entries2:
                    #templist = []
                    #if os.path.exists(basepath2) == True: 
                        #templist.append(entry1.name)
                        #print(templist)
                        #if 'ok.txt' in templist: # don't need this for this section. Should remove and just append all directory names directly to list2
        list2.append(entry.name.split('.')[0]) 
                    #if entry.name.endswith(".txt"): #.zip
                        #list1.append(entry.name)
                    #list1.append(templist)
        print(list2)
print('Completed')

print(list1, list2)

# Gets all the files that need to be moved
list3 = []
list4 = []
for i in list1:
    if i not in list2:
        list3.append(i)
        list4.append(' ' + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
#print(list3)
print(f'Files to be archived: {list3}')
print('Number of folders to be archived:', len(list3))
#print('Files to be archived:', list3)

if len(list3) < 1:
    print('No folders to be archived.')

# Zip folders
#print(list3)

#for i in list3:
#    print(Path(i))
#print('Completed')

# root_dir will be the root of the archive, base_dir is where to start archiving from
for i in list3:
    shutil.make_archive(base_name = Path('test_folder\\' + i), format = 'zip', root_dir = Path('test_folder'), base_dir = Path(i))
print('Archive Completed') 

# Move Folders
for i in list3:
    source = Path('C:\\Users\\mcguirt2\\documents\\Python\\test_folder\\' + i + '.zip')
    destination = Path('C:\\Users\\mcguirt2\\documents\\Python\\test_folder2\\')
    shutil.move(source, destination)
print('Move Completed')


# Remove completed files
#print(list1)
base_path = r'C:\\Users\\mcguirt2\\documents\\Python\\test_folder\\'
#print(base_path)

# Deletes all .txt files within folders that were in the original list
for folder in os.listdir(base_path):
    if folder in list1:
        folder_to_delete = base_path + folder
        for i in os.listdir(folder_to_delete):
            if '.txt' in i:
                file_to_delete = folder_to_delete + '\\' + i
                print(file_to_delete)
                print(os.path.isfile(file_to_delete))
                #os.remove(file_to_delete)
print('Files Deleted')

for i in list1:
    folder_to_delete = base_path + i
    #print(folder_to_delete)
    #os.rmdir(folder_to_delete)
    print("Deleted '%s' directory successfully" % folder_to_delete)
print('Deletion complete.')

# Log File (In Progress)

#print(list1)
datetoday = datetime.today().strftime('%Y-%m-%d')
print(datetoday)

d = {'folder': list1, 'date': datetoday}
d = pd.DataFrame(data = d)
#print(d)
csv_file_path = 'deleted_folders_log.csv'
try:
    d.to_csv(csv_file_path, mode='x', index = False, header = True)
    #print(df)
except FileExistsError:
    d.to_csv(csv_file_path, mode='a', header = False, index = False)
print('Log Updated')

lis5 = []
list5.append(list3)
list5.append(list4)

rez = [[list5[column][row] for column in range(len(list5)] for row in range(len(list5[0]))]
for row in rez:
    print(row)
print('Completed')
with open('deleted_folders_log.txt', 'a+') as f:
    for i in rez:
        f.writelines(i)
        f.writelines('\n')
print('Archive log complete')
f.close()

end = timer()
print(end - start)

# print(os.path.abspath('C:\\Users\\mcguirt2\\documents\\Python\\test_folder'))

# Potential work around for python 2.7
base1 = os.path.abspath('C:\\Users\\mcguirt2\\documents\\Python\\test_folder') 
list1 = []
with os.scandir(base1) as entries:
    for entry in entries:
        if entry.is_dir() and len(fnmatch.filter(os.listdir(entry), '*.txt')) >= 1:
            basepath1 = os.path.abspath('C:\\Users\\mcguirt2\\documents\\Python\\test_folder\\' + entry.name)
            #list1.append(entry.name)
            with os.scandir(basepath1) as entries2:
                for entry1 in entries2:
                    if entry1.is_dir():
                        basepath2 = os.path.abspath('C:\\Users\\mcguirt2\\documents\\Python\\test_folder\\' + entry.name + '\\' + entry1.name)
                        with os.scandir(basepath2) as entries3:
                            for entry2 in entries3:
                                    templist = []
                                    if os.path.exists(basepath2) == True: 
                                        templist.append(entry2.name.lower())
                                        print(templist)
                                        if 'ok.txt' in templist:
                                            list1.append(entry.name) 
                    #if entry.name.endswith(".txt"): #.zip
                        #list1.append(entry.name)
                    #list1.append(templist)
    print(list1)
print('Completed')
