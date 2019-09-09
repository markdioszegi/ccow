text = input("Enter a sentence! ")
newText = []
start = 0
end = 0
for i in range(len(text)):
    if text[i] == '<':
        start = i + 1
    elif text[i] == '>':
        end = i
        newText.append(text[start:end])
for i in range(len(newText)):
    print(newText[i])