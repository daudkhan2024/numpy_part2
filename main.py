### Special Types of Array (FIlled with Specific Value)

#array filled with 0
#array filled with 1
#creat empty array
#an array with range of elements
#array diagonal element filled with 1
#creat an array with values that are spaced linearly in
#specified interval


# ARRAY FILLED WIH 0

import numpy as np
ar_zero = np.zeros(4)
ar_zeros1 = np.zeros((3,4))#3  rows and 4 columns
print(ar_zero)
print(ar_zeros1)



#ARRAY  FILLED WITH 1
ar_one = np.ones(4)
print(ar_one)

# CRREATING EMPTY ARRAY
ar_em=  np.empty(4)
print(ar_em)# it wiill show previouos memory


# CREATE RANGE ARRAY
ar_rn = np.arange(4)
print(ar_rn)


#CREATE ARRAY FILLED WITH DIAGONAL
ar_dia = np.eye(3)
print(ar_dia)

ar_dia2 = np.eye(2)
print(ar_dia)

ar_dia = np.eye(6,7)
print(ar_dia)


# Special type of array linspace
ar_lin = np.linspace(0,20,num=5)
print(ar_lin)
