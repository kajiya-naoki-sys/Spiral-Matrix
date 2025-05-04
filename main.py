class Solution:
    def spiralOrder(self, matrix):
        result = []

        while matrix:
            result += matrix.pop(0)  # top row

            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())  # right column

            if matrix:
                #buf = reversed(matrix.pop())
                result += matrix.pop()[::-1]  # bottom row reversed

            if matrix and matrix[0]:
                for row in reversed(matrix):
                    result.append(row.pop(0))  # left column

        return result

sol = Solution() 
matrix1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]
matrix2 = [[1,2,3,4],
            [5,6,7,8],
            [9, 10,11, 12]]
matrix3 = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]]
result = sol.spiralOrder(matrix1)
print(result)