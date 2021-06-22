import sys #更新了密碼部分用for記數，超過三次跳出

name = ''
while name !='A':
    print('請輸入帳號:')
    name = input()
    if name != 'A':
        print('無此帳號。')
        print('離開請輸入[Y]:')
        r = input()
        if r == 'Y':
            sys.exit('您已離開此頁面。')#用sys.exit如果不想輸入帳號可直接跳出
    else:        
        print('帳號正確。')
        for i in range(0,3): #想插入一個for迴圈 輸入密碼次數超過三就跳出 跳出部分可以用break嗎?
            password = input('請輸入密碼：')
            if password == '1234':
                print('登入成功')
            elif i > 1:#使用sys.exit加for迴圈三次就跳出
                sys.exit('錯誤次數達到3次，自動登出。')
            else:
                print('密碼錯誤，您還剩' + str(2 - i) +'次機會。')
