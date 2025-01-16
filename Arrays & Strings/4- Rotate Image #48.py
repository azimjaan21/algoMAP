from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix) # to get matrix length

        for i in range(n):   # Transposation #STEP 1
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] =   matrix[j][i], matrix[i][j]  #reverse

        for i in range(n):   # Horizonatal Reflection #STEP 2
            for j in range(n // 2):
              matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j],  matrix[i][j] #reverse