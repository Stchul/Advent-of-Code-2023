upCounter = 0
downCounter = 0
input = open("Day1Input", "r").read()
for i in range(len(input)):
    if input[i] == '(':
        upCounter += 1
    else:
        downCounter += 1
Floor = upCounter - downCounter
print(Floor)
