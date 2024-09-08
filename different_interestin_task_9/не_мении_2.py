def med(A):
    A.sort()
    min_diff = float("inf")
    closest_pair = (None, None)

    for i in range(len(A) - 1):
        diff = A[i + 1] - A[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (A[i], A[i + 1])
    return closest_pair

A = list(map(int,input().split()))
result = med(A)
print(result)