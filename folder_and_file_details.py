import os
import numpy as np
import pandas as pd

from pathlib import Path
from datetime import datetime
from os import scandir

os.getcwd()
os.chdir('C:\\Users\\mcguirt2\\OneDrive - Bristol Myers Squibb\\Documents\\Python\\ ')
os.getcwd()

#entries = os.listdir('T:/  Automation/Projects')
#print(entries)

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

basepath = Path('T:\  Automation\Projects')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    #if item is not item.is_file(): to get folders
    if item.is_dir():
    #if item.is_file(): to get files
        print(item.name)
print('Completed')

fd = []
basepath = Path('T:\  Automation\Projects\\')
with os.scandir(basepath) as entries:
    for entry in entries:
        info = entry.stat()
        basepath1 = Path('T:\  Automation\Projects\\' + entry.name)
        if entry.is_dir():
            with os.scandir(basepath1) as entries2:
                for entry2 in entries2:
                    info = entry2.stat()
                    if entry2.is_dir():
                        basepath = Path('T:\  Automation\Projects\\' + entry.name + '\\' + entry2.name)
                        with os.scandir(basepath) as entries3:
                            for entry3 in entries3:
                                info = entry3.stat()
                                if entry3.is_dir():
                                    basepath = Path('T:\  Automation\Projects\\' + entry.name + '\\' + entry2.name + '\\' + entry3.name)
                                    with os.scandir(basepath) as entries4:
                                        for entry4 in entries4:
                                            info = entry4.stat()
                                            if entry4.is_dir():
                                                basepath = Path('T:\  Automation\Projects\\' + entry.name + '\\' + entry2.name + '\\' + entry3.name + '\\' + entry4.name)
                                                with os.scandir(basepath) as entries5:
                                                    for entry5 in entries5:
                                                        info = entry5.stat()
                                                        fd.append(
                                                        {
                                                        'Basepath': basepath1,
                                                        'Directory': basepath,
                                                        'File_name': entry5.name,
                                                        'Last_modified_time': convert_date(info.st_mtime),
                                                        'Creation_Date': convert_date(info.st_ctime),
                                                        'File_Size': info.st_size    
                                                        })
                                            else:
                                                fd.append(
                                                 {
                                                'Basepath': basepath1,
                                                'Directory': basepath,
                                                'File_name': entry4.name,
                                                'Last_modified_time': convert_date(info.st_mtime),
                                                'Creation_Date': convert_date(info.st_ctime),
                                                'File_Size': info.st_size
                                                })
                                else:
                                    fd.append(
                                        {
                                        'Basepath': basepath1,
                                        'Directory': basepath,
                                        'File_name': entry3.name,
                                        'Last_modified_time': convert_date(info.st_mtime),
                                        'Creation_Date': convert_date(info.st_ctime),
                                        'File_Size': info.st_size
                                        }
                                    )
                    else:
                        fd.append(
                            {
                            'Basepath': basepath1,
                            'Directory': basepath,
                            'File_name': entry2.name,
                            'Last_modified_time': convert_date(info.st_mtime),
                            'Creation_Date': convert_date(info.st_ctime),
                            'File_Size': info.st_size
                            }
                        )
        else:
            fd.append(
            {
            'Basepath': basepath1,
            'Directory': basepath,
            'File_name': entry.name,
            'Last_modified_time': convert_date(info.st_mtime),
            'Creation_Date': convert_date(info.st_ctime),
            'File_Size': info.st_size
            }
        )
pd.DataFrame(fd)

fd = pd.DataFrame(fd)
fd.head()

df = []
basepath = Path('T:\  Automation\Projects\\')
with os.scandir(basepath) as entries:
    for entry in entries:
        info = entry.stat()
        df.append(
        {
        'Directory': basepath,'Folder_name': entry.name,'Last_modified_time': convert_date(info.st_mtime),'Creation_Date': convert_date(info.st_ctime)
        }
        )
print('Completed')
pd.DataFrame(fd)
df = pd.DataFrame(df)
df.tail()

#fd.to_csv('project_2024q4.csv')
get_year = input('Enter year: ')
get_quarter = input('Enter quarter: ')
filename = ' _'+get_year+get_quarter
print(filename)
fd.to_excel(filename +'.xlsx', sheet_name='file_info')

with pd.ExcelWriter(filename +'.xlsx', mode = 'a') as writer:
    df.to_excel(writer, sheet_name='folder_info')
print('Completed')


# from datetime import datetime
# datetoday = datetime.today().strftime('%Y-%m-%d')
