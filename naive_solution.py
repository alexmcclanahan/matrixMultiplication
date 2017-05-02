#an attempt at less robust naive (n^3) solution of matrix multiplication
def mult(A, B):
    # colA=rowB is the condition of mat. mult.
    C = []
    for a in range(0, len(A)):
        C.append([0] * len(B[0]))
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            C[i][j] = 0
            for k in range(0, len(B)):
                C[i][j] += A[i][k]*B[k][j]
    print C
A = [[2, 1, 3], [2, 3, 1]]
B = [[2, 1], [132, 2], [1, 0]]
E = [[5, 10], [1, 2], [2, 3]]
F = [[2, 3], [6, 7]]
H = [[2, 2], [1, 1]]
Q = [[1, 2104], [1, 1416], [1, 1534], [1, 852]]
QQ = [[-40], [0.25]]
mult(A,E)
#final conclusion: in order to naively calculate matrix multiplication with two nxn matricies,
#one simply has to loop k in range of original n. I had to loop k up to a second variable, v,
#in order to account for the cases where we have two matrices with unequal dimensions. Therefore,
#A and B inputs into mult(A, B) can now be any two matrices AS LONG AS columns of A = rows of B.
