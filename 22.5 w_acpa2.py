import sys

name = ''
while name !='A':
    print('請輸入帳號:')
    name = input()
    if name != 'A':
        print('無此帳號。')
        print('離開請輸入[Y]:')
        r = input()
        if r == 'Y':
            sys.exit('您已離開此頁面。')
       #用sys.exit如果不想輸入帳號可直接跳出
    else:
         #想插入一個for迴圈 輸入密碼次數超過三就跳出 跳出部分可以用break嗎?
        #使用sys.exit加for迴圈三次就跳出
        print('帳號正確。')
        password = ''#要有這個''不然下一步的while會造成無限迴圈
        i = 0
        while password != ('1234'): #==才是等於， =是指派給變數
       #i = 0 放這邊會造成while跟他的子句分開
            password = input('請輸入密碼:')  
         
            i = i + 1 #原本以為要在下層才要i = i+1,但在下一層的話就不會計次
            if password != '1234': 
            #好像不能用if 要用while 才會累積i的次數?
                print('密碼錯誤'+ str(i) +'次，您還剩' + str(3 - i) +'次機會。')
                if i > 2:
                    sys.exit('錯誤次數達到3次，自動登出。')
                  
      
       
print('登入成功。')
