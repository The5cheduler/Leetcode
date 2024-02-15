class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        # row = matrix[..][0]
        # col = matrix[0][..]

        columnZero = 1

        # traverse through the array and check if there area any zeros and mark respective column and row to zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # mark i th row to zero
                    matrix[i][0] = 0
                    # mark jth row to zero
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        columnZero = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] != 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        if columnZero == 0:
            for i in range(m):
                matrix[i][0] = 0