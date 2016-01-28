def solution1(str1, str2):
    # Sorting method, O(nlogn) time O(n) space
    if not str1 and not str2: return True
    if not str1 and str2 or not str2 and str1: return False
    if len(str1) != len(str2): return False

    array1 = sorted(str1)
    array2 = sorted(str2)

    return array1 == array2

def solution2(str1, str2):
    # With hash table, O(n) time O(n) space
    if not str1 and not str2: return True
    if not str1 and str2 or not str2 and str1: return False
    if len(str1) != len(str2): return False

    charDic = {}
    for char in str1:
        charDic[char] = charDic.get(char, 0) + 1

    for char in str2:
        if char not in charDic or charDic[char] == 0:
            return False
        else:
            charDic[char] -= 1

    return True

def solution3(str1, str2):
    # If the characters are ASCII, we can do it in O(n) time O(1) space
    if not str1 and not str2: return True
    if not str1 and str2 or not str2 and str1: return False
    if len(str1) != len(str2): return False

    letters = [0] * 128
    for char in str1:
        letters[ord(char)] += 1

    for char in str2:
        if letters[ord(char)] == 0:
            return False
        else:
            letters[ord(char)] -= 1

    return True

str1, str2 = '', ''
print solution1(str1, str2), solution2(str1, str2), solution3(str1, str2)

str1, str2 = 'a', ''
print solution1(str1, str2), solution2(str1, str2), solution3(str1, str2)

str1, str2 = 'a', 'b'
print solution1(str1, str2), solution2(str1, str2), solution3(str1, str2)

str1, str2 = 'abc', 'acb'
print solution1(str1, str2), solution2(str1, str2), solution3(str1, str2)

str1, str2 = 'abccsbb', 'cabbbsc'
print solution1(str1, str2), solution2(str1, str2), solution3(str1, str2)

str1, str2 = 'abccsbb', 'cabbbs'
print solution1(str1, str2), solution2(str1, str2), solution3(str1, str2)
