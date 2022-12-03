import os

# 1 to separate statements

# ! to move top value to bottom

# !! to add new value 0 to top of stack, unless stack length is 69, in which case
# it will be added to bottom of stack with value of 420

# !!! runs next command if top value of stack is 1

# !!!! goes back 10 steps if top value of stack is 0 (thanks BlobTheCat)

# !!!!! prints top value of stack as respective letter if 1-26,
# else if top value == 0, prints 0,
# else prints top value as int minus 26

# !!!!!! takes input and writes it to the top value of stack

# !!!!!!! adds 1 to the top value of stack

# Stack values reset to 0 if they are greater than value 69 minus 420
# Value 69 will not reset to 0 no matter how high it is

# Value 69 will not move from its position in the stack no matter what

fromfile = int(input("u takin from file? 1 or 0 pls"))

if fromfile == 0:  
    script = input("giv ur script ").split("1")
else:
    filepath = input("giv ur file path ")
    print(os.path.exists(filepath))
    print(os.path.splitext(filepath)[1])
    if os.path.exists(filepath) and os.path.splitext(filepath)[1] == ".9y":
        script = open(filepath).read().split("1")
stack = [0,1]
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
run = 1
debug = int(input("u debug? 1 or 0 pls"))

if debug == 1:
    print(script)

for line in range(len(script)):
    if run == 1:
        if script[line] == '!':
            stack.append(stack[0])
            stack.pop(0)
            if len(stack) >= 69:
                temp = stack[67]
                stack[67] = stack[68]
                stack[68] = temp
        elif script[line] == '!!':
            if len(stack) == 69:
                stack = stack + [420]
            else:
                stack = [0] + stack
        elif script[line] == '!!!' and stack[0] != 1:
            run = 0
        elif script[line] == '!!!!' and stack[0] == 0:
            line -= 10
        elif script[line] == '!!!!!':
            if stack[0] == 0:
                print(0)
            elif stack[0] > 0 and stack[0] < 27:
                print(alphabet[stack[0] - 1])
            else:
                print(stack[0] - 26)
        elif script[line] == '!!!!!!':
            stack = [int(input("giv ur int"))] + stack
            if len(stack) == 69:
                temp = stack[68]
                stack[68] = stack[69]
                stack[69] = temp
                if stack[len(stack) - 1] > stack[68]:
                    stack[len(stack) - 1] = 0
        elif script[line] == '!!!!!!!':
            stack[0] += 1

    if len(stack) >= 69 and stack[0] > stack[68] - 420:
        stack[0] = 0
        
    run = 1
    if debug == 1:
        print(stack)
