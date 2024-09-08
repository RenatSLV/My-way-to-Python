def SelectionSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] < A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A
A = [1,5,3,2,7,8,4,34,23,12]
sorted = SelectionSort(A)
print(sorted)