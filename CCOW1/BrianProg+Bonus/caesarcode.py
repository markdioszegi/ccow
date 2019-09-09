txt = input("Enter a sentence: ")
newTxt = []
for i in range(len(txt)):
    ch = ord(txt[i]) + 2
    newTxt.append(chr(ch))
print("".join(newTxt))