from typing import List
class Solution:
    output = []
        #繰り返す回数を再帰させて求める
    def times(self, k, l, time) :
        time += 1
        k -= 2
        l -= 2
        if(k < 3 or l < 3) :
            return time
        else :
            return sol.times(k, l, time) 
        
    def spiralOrder(self, matrix) :
        m = len(matrix)
        n = len(matrix[m//2])
        #print(m, n)
        #1.left-to-right
        for i in range(n) :
            if(i == n-1) : continue
            print(matrix[0][i])
            if not matrix[0][i]: continue
            sol.output.append(matrix[0][i])

        for i in matrix :
            for j in sol.output :
                if j in i:
                    i.remove(j)

        #2. top-to-bottom
        for i in range(m) :
            if(i == m-1) : continue 
            print(matrix[i])
            if not matrix[i] : continue
            sol.output.append(matrix[i][n-1])

        for i in matrix :
            for j in sol.output :
                if j in i:
                    i.remove(j)

        #3.left-to-right
        for i in reversed(range(n)) :
            if(i == 0) : continue
            print(matrix[0][i])
            if not matrix[m-1][i] : continue
            sol.output.append(matrix[m-1][i])

        for i in matrix :
            for j in sol.output :
                if j in i:
                    i.remove(j)

        #4.bottom-to-top
        for i in reversed(range(m)) :
            if(i == 0) : continue
            print(matrix[:i][0])
            if not matrix[i] : continue
            sol.output.append(matrix[i][0])
            
        for i in matrix :
            for j in sol.output :
                if j in i:
                    i.remove(j)

        for i in matrix :
            if i :
                return sol.spiralOrder(matrix)
        return sol.output
        

sol = Solution() 
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
result = sol.spiralOrder(matrix)
print(result)