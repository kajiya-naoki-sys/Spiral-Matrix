class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        for k in 
        output = []
        #1.left-to-right
        for i in range(m-1) :
            n = len(matrix[i])
            for j in range(n-2) :
                output.append(matrix[0][j])
        #2. top-to-bottom
        for i in range(m-1) :
            n = len(matrix[i])
            for j in range(n-1) :
                if(i == m-1) : continue
                output.append(matrix[i][n-1])
        #3.left-to-right
        for i in range(m-1) :
            n = len(matrix[i])
            for j in range(n-1) :
                if(j == 0) : continue
                output.append(matrix[m-1][:j])
        #4.bottom-to-top
        for i in range(m-1) :
            n = len(matrix[i])
            for j in range(n-1) :
                if(i == 0) : continue
                output.append(matrix[:i-1])
        print(output)
        return output