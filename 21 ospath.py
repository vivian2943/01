import os.path
cur=os.path.dirname(__file__)#底線一邊要兩個
print('現在目錄路徑:' + cur)

a = os.path.abspath(input('請輸入檔案名稱:'))
print('是否為檔案:',os.path.isfile(a))
print('是否為目錄:',os.path.isdir(a))    
print('這是a' + a)

if os.path.exists(a):
    c, f= os.path.split(a)
    print('目錄路徑:' + c)
    print('檔名:' + f)
    
    print('完整檔案路徑名:' + a)
    print('檔案大小為',os.path.getsize(a))
    
    b = os.path.basename(a)
    print('最後的檔案或路徑名稱:' + a)
    
    t , r = os.path.splitdrive(a)
    
    print('磁碟機是' + t)
    print('路徑是' + r )
    
else:
    print('不存在此檔案')
