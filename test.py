'''
これでも動くが，良くない例．
outoputが一度もリセットされないので，再起で無限ループの陥る可能性がある．（matrix1の時とか）
'''
class Solution:
    output = []
        
    def spiralOrder(self, matrix) :
        m = len(matrix)
        n = len(matrix[m//2])
        #print(matrix)
        #1.left-to-right
        for i in range(n) :
            #print("#1")
            if(i == n-1) : continue
            #print(matrix[0][i])
            if not matrix[0]: continue
            sol.output.append(matrix[0][i])
            #print(sol.output)
            #print("------------------")

        #2. top-to-bottom
        for i in range(m) :
            #print("#2")
            if(i == m-1) : continue 
            #print(matrix[i])
            if not matrix[i] : continue
            sol.output.append(matrix[i][n-1])
            #print(sol.output)
            #print("------------------")

        #3.left-to-right
        for i in reversed(range(n)) :
            if(i == 0) : continue
            #print("#3")
            #print(matrix[0][i])
            if not matrix[m-1] : continue
            sol.output.append(matrix[m-1][i])
            #print(sol.output)
            #print("------------------")

        #4.bottom-to-top
        for i in reversed(range(m)) :
            #print("#4")
            if(i == 0) : continue
            #print(matrix[:i][0])
            if not matrix[i] : continue
            sol.output.append(matrix[i][0])
            #print(sol.output)
            #print("------------------")
            
        for i in matrix :
            for j in sol.output :
                if j in i:
                    i.remove(j)
        #空の要素を削除
        matrix = list(filter(None, matrix))

        if matrix :
            return sol.spiralOrder(matrix)
        
        return sol.output
        

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