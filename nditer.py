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
with np.nditer(a, op_flags=['readwrite']) as it:
    for x in it:
        x[...] = x / 2
print(a)

print('================== external loop')
print(a)
for i in np.nditer(a, flags=['external_loop']):
    print(i, end=' ')
print()

for i in np.nditer(a, flags=['external_loop'], order='F'):
    print(i)

print('================== tracking index')
print(a)
it = np.nditer(a, flags=['f_index'])
for x in it:
    print(f"{x} <{it.index}>")
print()

it = np.nditer(a, flags=['multi_index'])
for x in it:
    print(f"{x} <{it.multi_index}>")
print()

with np.nditer(a, flags=['multi_index'], op_flags=['writeonly']) as it:
    for x in it:
        x[...] = it.multi_index[1] - it.multi_index[0]
print(a)

print('================== tracking index by checking whether finished or not')
a = np.arange(6).reshape(2,3)
print(a)
it = np.nditer(a, flags=['f_index'])
while not it.finished:
    print(f"{it[0]} <{it.index}>")
    is_not_finished = it.iternext()
print()

it = np.nditer(a, flags=['multi_index'])
while not it.finished:
    print(f"{it[0]} <{it.multi_index}>")
    is_not_finished = it.iternext()
print()

with np.nditer(a, flags=['multi_index'], op_flags=['writeonly']) as it:
    while not it.finished:
        it[0] = it.multi_index[1] - it.multi_index[0]
        is_not_finished = it.iternext()
print(a)

print('================== one dimension')
a = np.arange(6)
print(a)
it = np.nditer(a, flags=['f_index'])
for x in it:
    print(f"{x} <{it.index}>")
print()

it = np.nditer(a, flags=['multi_index'])
for x in it:
    print(f"{x} <{it.multi_index}>")
print()

it = np.nditer(a, flags=['f_index'])
while not it.finished:
    print(f"{it[0]} <{it.index}>")
    is_not_finished = it.iternext()
print()

it = np.nditer(a, flags=['multi_index'])
while not it.finished:
    print(f"{it[0]} <{it.multi_index}>")
    is_not_finished = it.iternext()
print()