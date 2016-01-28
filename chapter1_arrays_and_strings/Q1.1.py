# With extra data structure

def solution1(inputString):
    # O(n) time O(n) space
    if not inputString: return True

    charSet = set()
    for char in inputString:
        if char not in charSet:
            charSet.add(char)
        else:
            return False
    return True

# Without extra data structure

def solution2(inputString):
    # Determine if it is ASCII or Unicode, assume it is Unicode
    # O(n) time O(1) space
    if not inputString: return True
    if len(inputString) > 128: return False

    charSet = [False] * 128
    for char in inputString:
        if charSet[ord(char)]:
            return False
        else:
            charSet[ord(char)] = True
    return True

inputString = ''
print solution1(inputString), solution2(inputString)

inputString = 'a'
print solution1(inputString), solution2(inputString)

inputString = 'abc'
print solution1(inputString), solution2(inputString)

inputString = 'asdfa'
print solution1(inputString), solution2(inputString)
