def isRotation(s1, s2):
    if not s1 and not s2: return True
    if s1 and s2 and len(s1) == len(s2):
        return isSubString(s1+s1, s2)
    else:
        return False

# KMP-based isSubString
def isSubString(haystack, needle):
    if not needle: return True
    if not haystack or len(haystack) < len(needle): return False
    table = [0] * len(needle)
    i = 0
    j = 1
    while j < len(needle):
        if needle[j] == needle[i]:
            table[j] = i + 1
            i += 1
            j += 1
        elif i > 0:
            i = table[i-1]
        else:
            table[j] = 0
            j += 1
    m = i = 0
    while m < len(haystack) - len(needle) + 1:
        if haystack[m+i] == needle[i]:
            i += 1
            if i == len(needle):
                return True
        else:
            if i == 0:
                m += 1
            else:
                m = m + i - table[i-1]
                i = table[i-1]
    return False

# Test
s1 = ''
s2 = ''
print isRotation(s1, s2)

s1 = ''
s2 = 'a'
print isRotation(s1, s2)

s1 = 'a'
s2 = ''
print isRotation(s1, s2)

s1 = 'abc'
s2 = 'abc'
print isRotation(s1, s2)

s1 = 'leetcode'
s2 = 'tcodelee'
print isRotation(s1, s2)

s1 = 'leetcode'
s2 = 'tcodeele'
print isRotation(s1, s2)

s1 = 'leetcode'
s2 = 'tcodeleee'
print isRotation(s1, s2)
