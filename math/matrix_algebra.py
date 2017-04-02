# Matrix Algebra

import numpy as np

A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix('5 -1; 9 1; 6 0')
D = np.matrix('3 -2 -1; 1 2 3')
u = np.matrix('6 2 -3 5')
v = np.matrix('3 5 -1 4')
w = np.matrix('1; 8; 0; 5')

#1.1
print(A.shape)
#(2,3)

#1.2
print(B.shape)
#(2,2)

#1.3
print(C.shape)
#(3,2)

#1.4
print(D.shape)
#(2,3)

#1.5
print(u.shape)
#(1,4)

#1.6
print(w.shape)
#(4,1)

#2.1
print(np.add(u, v))
# [[9 7 -4 9]]

#2.2
print(np.subtract(u, v))
#[[3 -3 -2 1]]

#2.3
alpha = 6
print(alpha*u)
#[[36 12 -18 30]]

#2.4
v_transpose = (np.transpose(v))
print(np.dot(u, v_transpose))
#51

#2.5
print(np.linalg.norm(u))
#8.60232526704

#3.1
#Not defined

#3.2
C_transpose = (np.transpose(C))
print(np.subtract(A, C_transpose))
#[[-4 -7 -3]
# [3  6  4]

#3.3
three_D = (D*3)
print(np.add(C_transpose, three_D))
#[[14 3 3]
# [2 7 9]]

#3.4
print(np.matmul(B, A))
#[[-1 -5 -1]
# [2  7  4]]

#3.5
A_transpose = (np.transpose(A))
#Not defined

#3.6
#Not defined

#3.7
print(np.matmul(C, B))
#[[5 -6]
# [9 -8]
# [6 -6]]

#3.8
print(np.linalg.matrix_power(B, 4))
#[[1 -4]
# [0  1]]

#3.9
print(np.matmul(A, A_transpose))
# [[14 28]
#  [28 69]

#3.10
D_transpose = (np.transpose(D))
print(np.matmul(D_transpose, D))
# [[10 -4 0]
#  [-4 8  8]
#  [0  8 10]]
