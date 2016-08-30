def divBy2(decNumber):
    binary = []
    while decNumber > 0:
        rem = decNumber % 2
        binary.append(rem)
        decNumber = decNumber // 2
    return binary[::-1]


def toDecNumber(binary):
    decNumber = 0
    index = 0
    while index < len(binary):
        print(decNumber)
        decNumber = decNumber + (2**index * binary[index])
        index = index + 1
    return decNumber


def toInfix(string):
    ops = {}
    ops["*"] = 2
    ops["/"] = 2
    ops["+"] = 1
    ops["-"] = 1
    ops["("] = 0
    postfix = []
    opStack = []
    list_string = list(string)
    for x in list_string:
        print opStack
        if x.isalnum():
            postfix.append(x)
        elif x == '(':
            opStack.append(x)
        elif x == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfix.append(topToken)
                topToken = opStack.pop()
        elif x in ops:
                while len(opStack) != 0 and ops[opStack[-1]] >= ops[x]:
                    postfix.append(opStack.pop())
                opStack.append(x)
    print opStack
    while len(opStack) != 0:
        postfix.append(opStack.pop())
    return postfix
