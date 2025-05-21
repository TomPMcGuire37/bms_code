import os
from pathlib import Path
from os import scandir
import shutil
from datetime import datetime, timedelta
import fnmatch

# Broad Hammer
# info = entry.stat
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date
# convert_date(info.st_atime)

base1 = os.path.abspath('C:\\Users\\mcguirt2\\documents\\Python\\test_folder') 
list1 = []
with os.scandir(base1) as entries:
    for entry in entries:
        if entry.is_dir() and len(fnmatch.filter(os.listdir(entry), '*.txt')) >= 1 and 'test' in entry.name:
            info = entry.stat()
            last_access_date = convert_date(info.st_mtime)
            format = '%d %b %Y'
            last_access_date = datetime.strptime(last_access_date,format)
            if (datetime.today() - last_access_date) > timedelta(days = 180):
                list1.append(entry.name)
            else:
                print(entry.name, last_access_date)

            #print(entry.name, last_access_date)
print('Completed')

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


# datetoday = datetime.today().strftime('%Y-%m-%d')
# sixmonths = timedelta(days = 180)
# dateminus6 = datetoday - sixmonths
# print((datetime.today() - sixmonths).strftime('%Y-%m-%d'))

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

# Archive Testing w/ no pandas
"""
import os
from pathlib import Path
from os import scandir
import shutil
from datetime import datetime, timedelta
import fnmatch

os.chdir('C:\\Users\\mcguirt2\\documents\\Python\\')

# Broad Hammer
# info = entry.stat
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y %H:%M:%S')
    return formated_date
# convert_date(info.st_atime)

base1 = os.path.abspath('C:\\Users\\mcguirt2\\documents\\Python\\test_folder') 
list4 = []
list1 = []
list2 = []
with os.scandir(base1) as entries:
    for entry in entries:
        if entry.is_dir() and len(fnmatch.filter(os.listdir(entry), '*.txt')) >= 1:
            info = entry.stat()
            last_access_date = convert_date(info.st_mtime)
            format = '%d %b %Y %H:%M:%S'
            last_access_date = datetime.strptime(last_access_date,format)
            if (datetime.today() - last_access_date) > timedelta(days = 180):
                list4.append(entry.name)
            else:
                list1.append(entry.name)
                list2.append(' ' + datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

            #print(entry.name, last_access_date)
print('Completed')

#list1.pop()
#list2.pop()
print(list1, list2)

list3 = []
list3.append(list1)
list3.append(list2)
print(list3[1][1])

#result = [[0,0,0],[0,0,0]]

# transpose the list of lists
rez = [[list3[column][row] for column in range(len(list3))] 
    for row in range(len(list3[0]))]
for row in rez:
     print(row)
print('Completed')

import csv

with open('deleted_folders_log.txt', 'a+') as f:
    for i in rez:
        f.writelines(i)
        f.writelines('\n')
print('End')

# Below was to open the log, probably not needed to be kept
with open('deleted_folders_log.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
print('Completed')

csvfile.close()
"""
