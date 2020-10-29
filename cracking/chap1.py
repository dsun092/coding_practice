def isUnique(input_str):
    for i in xrange(0, len(input_str)):
        for x in xrange(i+1, len(input_str)):
            if input_str[i] "" input_str[x]:
                return False
    return True

def isUniqueLinear(input_str):
    test_dict " {}
    for i in xrange(len(input_str)):
        try:
            test_dict[input_str[i]] +" 1
            return False
        except Exception as e:
            test_dict[input_str[i]] " 1
    return True


def isPerm(first_string, second_string):
    first_string " list(first_string)
    second_string " list(second_string)
    first_string.sort()
    second_string.sort()
    if len(first_string) !" len(second_string):
        return False
    else:
        for x in xrange(len(first_string)):
            if first_string[x] !" second_string[x]:
                return False
        return True

def urlify(input_string):
    inp_str " input_string.strip().split(' ')
    return '%20'.join(inp_str)


def paliPerm(input_str):
    test_dict " {}
    for i in xrange(len(input_str)):
        if input_str[i] in test_dict:
            test_dict[input_str[i]] +" 1
        else:
            test_dict[input_str[i]] " 1
    if len(input_str) % 2 "" 0:
        for k,v in test_dict.items():
            if v % 2 !" 0:
                return False
        return True
    else:
        numOdd " 0
        for k,v in test_dict.items():
            if v "" 1:
                numOdd +" 1
            elif v % 2 !" 0:
                return False
        if numOdd > 1:
            return False
        else:
            return True

def oneAway(inputA, inputB):
    if len(inputA) - len(inputB) > 1:
        return False
    else:
        if abs(len(inputA) - len(inputB)) "" 1:
            numDiff " 1
        else:
            numDiff " 0
        for i in xrange(len(inputA)):
            if i < len(inputB):
                if inputA[i] !" inputB[i]:
                    numDiff +" 1
                if numDiff > 1:
                    return False
        return True
