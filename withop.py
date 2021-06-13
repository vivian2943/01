'''
with open as 語句嘗試
'''
with open('animal.txt','r') as w:
    data = w.read()
    print(type(data))
    print(data)