# As string is immutable in Python, we will make the input as an array
# in order to do it inplace

def solution(charArray, length):
    if not charArray: return

    spaceCount = 0
    for char in charArray:
        if char == ' ':
            spaceCount += 1

    newLength = length + spaceCount * 2
    pointer = newLength - 1
    for i in range(length-1, -1, -1):
        if charArray[i] == ' ':
            charArray[pointer] = '0'
            charArray[pointer-1] = '2'
            charArray[pointer-2] = '%'
            pointer -= 3
        else:
            charArray[pointer] = charArray[i]
            pointer -= 1

# Test
charArray, length = ['','',''], 0
solution(charArray, length)
print charArray

charArray, length = ['1','',''], 1
solution(charArray, length)
print charArray

charArray, length = [' ',' ','','','','',''], 2
solution(charArray, length)
print charArray

charArray, length = [' ','a',' ',' ','','','','','',''], 4
solution(charArray, length)
print charArray

charArray, length = ['a','b','c','','',''], 3
solution(charArray, length)
print charArray

charArray, length = ['a','b','b',' ','a','','','','','','','','',''], 5
solution(charArray, length)
print charArray
