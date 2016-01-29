def compress(inputString):
    # O(n) time and O(n) space
    if not inputString: return ''

    size = countCompress(inputString)
    if size >= len(inputString):
        return inputString

    charArray = [''] * size
    last, count, index = inputString[0], 1, 0
    for i in range(1, len(inputString)):
        if inputString[i] == last:
            count += 1
        else:
            index = setChar(charArray, index, count, last)
            last = inputString[i]
            count = 1
    setChar(charArray, index, count, last)
    return ''.join(charArray)

def countCompress(inputString):
    count, last, size = 1, inputString[0], 0
    for i in range(1, len(inputString)):
        if inputString[i] == last:
            count += 1
        else:
            size += 1 + len(str(count))
            count = 1
            last = inputString[i]
    size += 1 + len(str(count))
    return size

def setChar(charArray, index, count, last):
    charArray[index] = last
    index += 1
    for i in range(len(str(count))):
        charArray[index] = str(count)[i]
        index += 1
    return index

# Test
inputString = ''
print compress(inputString)

inputString = 'abcde'
print compress(inputString)

inputString = 'aabccccaaa'
print compress(inputString)

inputString = 'abccdee'
print compress(inputString)

inputString = 'accc'
print compress(inputString)
