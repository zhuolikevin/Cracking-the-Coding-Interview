# This problem can actually not be solved by Python, Java or many other languages
# except C/C++ in place, because the string variable is immutable in these languages.
# Here we modify the input argument as an array and do it in place

def solution(inputArray):
    # O(n) time O(1) space
    if not inputArray: return

    i, j = 0, len(inputArray) - 1
    while i < j:
        inputArray[i], inputArray[j] = inputArray[j], inputArray[i]
        i += 1
        j -= 1

# Test
inputArray = []
solution(inputArray)
print inputArray

inputArray = [1]
solution(inputArray)
print inputArray

inputArray = [1, 2, 3]
solution(inputArray)
print inputArray

inputArray = [1, 2, 3, 4]
solution(inputArray)
print inputArray
