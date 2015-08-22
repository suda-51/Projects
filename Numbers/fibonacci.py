"""
Fibonacci Sequence
Enter a number (N) and the program will print the N-th number in fibonacci sequence.
This program uses an algorithm with the complexity of O(log N)
"""

def matrixMul(firstMatrix, secondMatrix):
    """
    Return the result of matrix multiplication of firstMatrix and secondMatrix
    """
    ret = []

    for i in range(0, len(firstMatrix)):
        ret.append([])

        for j in range(0, len(secondMatrix[i])):
            ret[i].append(0)

            for k in range(0, len(firstMatrix[i])):
                ret[i][j] += firstMatrix[i][k] * secondMatrix[k][j]

    return ret

def matrixPow(matrix, x):
    """
    Return matrix to the power of x
    """
    if(x == 0):
        identity = []

        for i in range(0, len(matrix)):
            identity.append([])

            for j in range(0, len(matrix)):
                if(i == j):
                    identity[i].append(1)
                else:
                    identity[i].append(0)
        return identity # Return the identity matrix with the same size as the input matrix
    elif(x == 1):
        return matrix
    else:
        temp = matrixPow(matrix, x / 2)
        ret = matrixMul(temp, temp)
        
        if(x % 2 == 0):
            return ret
        else:
            return matrixMul(ret, matrix)

def fib(n):
    """
    Returns the n-th number in fibonacci sequence
    """
    if(n == 1) or (n == 2):
        return 1
    else:
        matrix = [
            [0, 1],
            [1, 1]
        ]

        matrix = matrixPow(matrix, n - 2)
        return matrix[0][1] + matrix[1][1]

if __name__ == '__main__':
    n = int(raw_input())
    print fib(n)