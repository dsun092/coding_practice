def isUnique(input_str):
    for i in xrange(0, len(input_str)):
        for x in xrange(i+1, len(input_str)):
            if input_str[i] == input_str[x]:
                return False
    return True

def isUniqueLinear(input_str):
    test_dict = {}
    for i in xrange(len(input_str)):
        try:
            test_dict[input_str[i]] += 1
            return False
        except Exception as e:
            test_dict[input_str[i]] = 1
    return True

