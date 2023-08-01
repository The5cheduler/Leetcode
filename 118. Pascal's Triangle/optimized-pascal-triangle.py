def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    final = []
    prev = []
    for i in range(n):
        current = []
        for j in range(i+1):
            if j in (0, i):
                current.append(1)
            else:
                current.append(prev[j-1] + prev[j])
        prev = current
        final.append(current)
    return final
