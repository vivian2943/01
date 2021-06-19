import sys

while True:
    print('s')
    response = input()
    if response == 'exit':
        sys.exit()
    print('f' + response + '。')
