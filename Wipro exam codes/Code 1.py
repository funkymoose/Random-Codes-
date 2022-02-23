code = input()
num = int(input())
if code.islower():
    if ord(code)+num<=122:
        print(chr(ord(code)+num))
    else:
        x = (ord(code)+num)-122
        print(chr(x+96))

elif code.isupper():
    if ord(code)+num<=90:
        print(chr(ord(code)+num))
    else:
        x = (ord(code)+num)-90
        print(chr(x+64))
