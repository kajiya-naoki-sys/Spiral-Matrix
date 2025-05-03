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
        n = len(matrix[0])
        #1.left-to-right
        for i in range(n) :
            if(i == n-1) : continue
            sol.output.append(matrix[0][i])

        #2. top-to-bottom
        for i in range(m) :
            if(i == m-1) : continue 
            #print(matrix[i][n-1])
            sol.output.append(matrix[i][n-1])

        #3.left-to-right
        for i in reversed(range(n)) :
            if(i == 0) : continue
            print(matrix[0][i])
            sol.output.append(matrix[m-1][i])

        #4.bottom-to-top
        for i in reversed(range(m)) :
            if(i == 0) : continue
            #print(matrix[:i][0])
            sol.output.append(matrix[i][0])

        for i in matrix :
            for j in sol.output :
                if j in i:
                    i.remove(j)
        print(matrix)
        return sol.output

sol = Solution() 
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
result = sol.spiralOrder(matrix)
print(result)