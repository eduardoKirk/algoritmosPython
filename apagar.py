import numpy as np
from rich import print

A = np.asmatrix('[1 0 8; 3 9 2; 7 2 0]')
B = np.asmatrix('[10 ; 7]')
print(f"determinante de \n{A}: ", np.linalg.det(A))