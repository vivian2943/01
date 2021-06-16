import os
dir = 'mydoc'
if os.path.exists(dir):
    os.rmdir(dir)
else:
    print(dir + '未建立')