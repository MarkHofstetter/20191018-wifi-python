'''
+ den Inhalt des Verzeichnis data auflisten bzw durchssuchen
os.walk

+ alle .txt Dateien in das Verzeichnis "import" moven
+ beim "moven" den namen auf kleinschreibung umstellen
shutil.move

(+ pfade aus configdatei)
'''

import os, shutil
import re
import datetime

target_dir = 'import'
source_dir = 'data'

# 2019-10-28-1527_import

dt = datetime.datetime.now()
new_target_dir = "{:d}-{:d}-{:d}-{:d}{:d}_{:s}" \
  .format(dt.year, dt.month, dt.day, dt.hour, dt.minute, target_dir)
  
if not os.path.isdir(new_target_dir):
    print('target dir does not exist - creating ...')
    os.mkdir(new_target_dir)

for root, dirs, files in os.walk(source_dir):
    print(root, dirs, files)    
    for file in files:
        # match = re.search(r'\.txt$', file)
        # if match:            
        if file.endswith('.txt'):
            new_file_name = file.lower()
            print(file, new_file_name)               
            shutil.move(os.path.join(source_dir, file), 
                        os.path.join(new_target_dir, new_file_name))
    

