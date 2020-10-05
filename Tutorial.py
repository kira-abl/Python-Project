import numpy as np

#ndarray object

arr = np.array([1, 2, 3, 4, 5])

arr1 = (1, 2, 3, 4, 5)

num = 2

print(arr)
print(arr1[3])


print(np.__version__)
print(type(arr))
print(type(arr))
print(type(arr1))
print(type(num))

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print('5th element on 2nd dim: ', arr[1, 4])

arr2 = np.array([1, 2, 3, 4], ndmin=5)

print(arr2)
print('number of dimensions :', arr2.ndim)
print(arr2[0])
