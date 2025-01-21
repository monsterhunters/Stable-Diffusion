import os
import shutil

os.system('git clone https://github.com/facefusion/facefusion.git')
shutil.move("facefusion", "face")
os.chdir('face')
os.rename('facefusion.py', 'run.py')
