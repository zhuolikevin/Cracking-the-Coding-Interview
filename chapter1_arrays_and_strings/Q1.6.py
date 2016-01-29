def rotateImage(matrix):
    # O(n^2) time and O(1) space
    if not matrix or not matrix[0]: return

    n = len(matrix)
    for x in range(n/2+1):
        first = x
        last = n - 1 - x
        for y in range(first, last):
            temp = matrix[x][y]
            matrix[x][y] = matrix[n-1-y][x]
            matrix[n-1-y][x] = matrix[n-1-x][n-1-y]
            matrix[n-1-x][n-1-y] = matrix[y][n-1-x]
            matrix[y][n-1-x] = temp

# Test
matrix = []
rotateImage(matrix)
print matrix

matrix = [[]]
rotateImage(matrix)
print matrix

matrix = [[1,2],[3,4]]
rotateImage(matrix)
print matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotateImage(matrix)
print matrix
