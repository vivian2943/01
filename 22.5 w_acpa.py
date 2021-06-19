name = ''
while name !='A':
    print('請輸入帳號:')
    name = input()
    if name != 'A':
        print('帳號錯誤。')
        #想插入一個for迴圈 輸入次數超過三就跳出 跳出部分可以用break嗎?
        #使用sys.exit加for迴圈三次就跳出
    else:
        print('帳號正確。')
        password = ''#要有這個''不然下一步的while會造成無限迴圈
        while password != ('1234'): #==才是等於， =是指派給變數
            password = input('請輸入密碼:')            
            if password != '1234':
                print('密碼錯誤。')
      
       
print('登入成功。')
