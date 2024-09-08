def InsertionSort(A):
    n = len(A)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
        gap //= 2
    return A

A = [1,2,3,6,4,5,6,7,8]
B = [1,6,2,8,2,45,78,31,1]
sort = InsertionSort(A)
sort2 = InsertionSort(B)
print(sort)
print(sort2)