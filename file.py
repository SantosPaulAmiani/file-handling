f = open('practice.txt', 'w+')
f.write("This is a new file")
f.close()

import os
print(os.getcwd())
print(os.listdir('/home/santos/'))
import shutil
shutil.move('practice.txt','/home/santos/Documents/')

