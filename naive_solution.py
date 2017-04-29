#a matrix multiplication algorithm
import randMatrix

def initC(n):
    C = []
    for j in range(0, n):
        C.insert(j, [0]*n)
    return C

def matrixM(A, B):
    #len delivers the number of rows in a matrix
    n = len(A)
    C = initC(n)
    if len(A) == len(B):
        if len(A[0]) == len(B):
            # case where we have two arrays of n x n; must make sure columns of A = rows of B
            for i in range(0, n):
                for j in range(0, n):
                    for k in range(0, n):
                        C[i][j] += A[i][k]*B[k][j]
        else:
            print "Cross product matrix is not defined. The first matrix must have the same number of columns as the second matrix has rows."
            return
    if len(A[0]) == len(B):
        # case where we have two arrays which don't have the same dimensions
        if len(A) < len(B):
            # subcase where the first array is wider and less skinny than the second, B array
            for i in range(0, n):
                for j in range(0, n):
                    for k in range(0, n+1):
                        C[i][j] += A[i][k] * B[k][j]
        if len(A) > len(B):
            #subcase where the first array is taller and skinner than the B array
            for i in range(0, n):
                for j in range(0, n):
                    for k in range(0, n-1):
                        C[i][j] += A[i][k] * B[k][j]
        print C
    else:
        print "Cross product matrix is not defined. The first matrix must have the same number of columns as the second matrix has rows."
        return
print '-----------------------------------------------------'
print '-----------------------------------------------------'
print "First (x) random generated matrix is:", randMatrix.x
print "Second (y) random generated matrix is: ", randMatrix.y

matrixM(randMatrix.x, randMatrix.y)

print '-----------------------------------------------------'
print '-----------------------------------------------------'

#extinct matrixmult
#A = [[2, 1, 3], [2, 3, 1]]
#B = [[2, 1], [132, 2], [1, 0]]
#E = [[5, 10], [1, 2], [2, 3]]
#F = [[2, 3], [6, 7]]
#H = [[2, 2], [1, 1]]
