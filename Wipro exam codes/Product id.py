vowels = "aAeEiIoOuU"
string = input()
vowl = []
finalstr = ""
for i in string:
    if i in vowels:
        vowl.append(i)
vowl.reverse()
ct = 0
for i in string:
    if i in vowels:
        finalstr+=vowl[ct]
        ct+=1
    else:
        finalstr+=i
print(finalstr)
