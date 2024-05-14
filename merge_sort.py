def merge(A, p, q, r):
    n_l = q - p + 1
    n_r = r - q
    L = [0] * (n_l)
    R = [0] * (n_r)
    for i in range(n_l):
        L[i] = A[p + i]
    for j in range(n_r):
        R[j] = A[q + j + 1]
    i = 0
    j = 0
    k = p
    while i < n_l and j < n_r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < n_l:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n_r:
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A, p, r):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)


# if __name__ == "__main__":
#     A = [2, 4, 5, 7, 1, 2, 3, 6]
#     merge_sort(A, 0, len(A) - 1)
#     print(A)
