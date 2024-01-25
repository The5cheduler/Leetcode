def zeroMatrix(matrix):
    # Write your code here.
    if not matrix or not matrix[0]:
        return matrix
    #get the first row = matrix[..][0]
    #get the first column = matrix[0][..]
    n = len(matrix)
    m = len(matrix[0])

    #define variable to store column zero variable
    columnZero = 1
    #traverse through the array
    for i in range(n):
        for j in range(m):
            # check if any element in the entire matrix
            if matrix[i][j] == 0:
                # set ith row to zero
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    columnZero = 0

    # traverse again through inner matrix
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                # set that value to zero
                matrix[i][j] = 0

    # check if first element is zero
    if matrix[0][0] == 0:
        # if zero than make entire first column zero
        for j in range(m):
            matrix[0][j] = 0

    # check columnZero flag is zero
    if columnZero == 0:
        # if it is zero than make entire first row zero.
        for i in range(n):
            matrix[i][0] = 0

    return matrix
