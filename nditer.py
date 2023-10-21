import numpy as np


a = np.arange(6).reshape(2, 3)

print('\n================== automatically chosen to match the memory layout of the array')

print(f'a: {a}')
for i in np.nditer(a):
    print(i, end=' ')

print('\n------------------')

print(f'a.T: {a.T}')
for i in np.nditer(a.T):
    print(i, end=' ')

print('\n================== manually specify C or Fortran orderings')

print('--- based on C ---')
print(a)
for i in np.nditer(a.copy(order='C')):
    print(i, end=' ')
print()

print(a.T)
for i in np.nditer(a.T.copy(order='C')):
    print(i, end=' ')
print()

print('--- based on Fortran ---')
print(a)
for i in np.nditer(a.copy(order='F')):
    print(i, end=' ')
print()

print(a.T)
for i in np.nditer(a.T.copy(order='F')):
    print(i, end=' ')

print('\n================== modify array values')
print(a)
with np.nditer(a, op_flags=['readwrite']) as it:
    for x in it:
        x[...] = 2 * x
print(a)

print('================== external loop')
print(a)
for i in np.nditer(a, flags=['external_loop']):
    print(i, end=' ')
print()

for i in np.nditer(a, flags=['external_loop'], order='F'):
    print(i)
