startingFloor = 0
upCounter = 0
downCounter = 0
input = open("Day1Input", "r").read()
for i in range(len(input)):
   if(startingFloor == -1):
       print(i)
       break
   else:
       if input[i] == '(':
           startingFloor += 1
       else:
           startingFloor -= 1
