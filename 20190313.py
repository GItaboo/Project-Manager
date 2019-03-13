
# to search the library refer to -> stack overflow, github

# Data structure (stack) -> FILO
# underflow, overflow
# push, pop


stack = []
SIZE = 10
position = -1

def push(data, stack, SIZE, position) :

    #Overflow function
    if(position == SIZE):
        print("overflow")
        return stack, position

    stack.append(data)
    position = position + 1

    return stack,position


def pop(stack, position) :

    #underflow
    if(position == -1):
        print("underflow")
        return "error", position

    temp = stack[position]
    del stack[position]
    position = position - 1

    return temp, position

while(True) :

    choice = int(input('input the choice (1 is push, else is pop) : '))

    if(choice == 1) :
        data = int(input('input the data value : '))
        stack,position = push(data, stack, SIZE, position)

    else :
        data, position = pop(stack, position)

    print('stack', stack)
    print('data', data)
    print('position', position)