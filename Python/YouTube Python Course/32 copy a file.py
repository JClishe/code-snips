#Commands within shutil module:
#copyfile()     =   copies contents of a file
#copy()         =   copyfile() + permission mode + destination can be a directory
#copy2()        =   copy() + copies metadata (file's creation and modification times)

import shutil 

shutil.copyfile('32_original.txt','32_copy.txt') #source, destination. Use full path if file is not in project folder