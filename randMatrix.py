import numpy as np

def rand(col):
    #will generate a list of random integers, with a 'col' number of indicies, given desired columns data
    colss = []
    for i in range(0, col):
        r = np.random.randint(-50, 50)
        colss.append(r)
    return colss

def gen(rows, cols):
    # a function to return a rows X cols MATRIX (in form of list) of random integers, given desired row and column stats
    randMat = []
    for j in range(0, rows):
        randMat.append(rand(cols))
    return randMat

x = gen(2, 2)
y = gen(2, 2)
