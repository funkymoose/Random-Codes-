vow = {"a": "e", "A": "E", "e": "i", "E": "I", "i": "o", "I": "O", "o": "u", "O": "U", "u": "a", "U": "A"}
inp = list(map(str, input()))
for i in range(0,len(inp)):
    if inp[i] in vow:
        inp[i] = vow[inp[i]]
print("".join(inp))

