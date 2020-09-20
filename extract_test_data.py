import os
import shutil
from pathlib import Path
import math

dest_dir = "E:/Sentinel 2/EuroSAT/test/"
test_perc = 0.15
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    if(os.path.basename(root)!='.'):#skip the parent directory of the first file which is where the script located
        os.mkdir(os.path.join(dest_dir,os.path.basename(root)))
    
    test_index = math.floor(len(files)*test_perc)

    for file in files[-test_index:]: # get the x percent of images from each class
        src = str(Path(file).parent.absolute()) + "\\"+os.path.basename(root)+ "\\" +str(Path(file))
        dest = dest_dir+os.path.basename(root)+ "\\"
        shutil.copyfile(src, os.path.join(dest,Path(file)))   
        if(str(Path(file)) != 'extract_test_data.py'):
            os.remove(src)
    input()



