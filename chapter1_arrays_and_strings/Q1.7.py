def setZeroes(matrix):
    # O(mn) time O(1) space
    if not matrix or not len(matrix[0]): return
    m, n = len(matrix), len(matrix[0])
    firstRowZero = firstColZero = False
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if i == 0:
                    firstRowZero = True
                if j == 0:
                    firstColZero = True
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if firstRowZero:
        for j in range(n):
            matrix[0][j] = 0
    if firstColZero:
        for i in range(m):
            matrix[i][0] = 0

# Test
matrix = []
setZeroes(matrix)
print matrix

matrix = [[]]
setZeroes(matrix)
print matrix

matrix = [[1,2,3],[4,0,5],[6,7,8]]
setZeroes(matrix)
print matrix

matrix = [[1,2,3,4],[5,0,6,7],[8,9,10,11],[12,13,14,0]]
setZeroes(matrix)
print matrix

matrix = [[1,2,3,0],[5,6,6,7],[8,9,10,11],[12,13,14,15]]
setZeroes(matrix)
print matrix

matrix = [[0,2,3,4],[5,6,6,7],[8,9,10,11],[12,13,14,15]]
setZeroes(matrix)
print matrix

matrix = [[0,2,0,4],[5,0,6,7],[8,9,10,11],[12,13,14,15]]
setZeroes(matrix)
print matrix
