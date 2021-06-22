for i in range(0,3):
    a = input('輸入密碼：')
    if a == 'key':
        print('登入')
    else:
        print('錯誤，剩餘嘗試次數為'+ str(2 - i))    