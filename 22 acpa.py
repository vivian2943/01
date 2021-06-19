#能結合字典出一個可acceess的帳號+密碼名單嗎?

account = input('請輸入帳號:')
if account == 'A':
    print('帳號正確。')
    password = input('請輸入密碼:')
    if password == '1234':
	    print('歡迎回來' + 'A')
    else:
        print('密碼錯誤') #錯誤要怎麼回到重新輸入密碼?
        #要做個while true迴圈?
else:
    print('帳號未註冊')
