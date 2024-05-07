def marge(A, p, q, r):
    n_l = q - p + 1
    n_r = r - q
    L = [0] * (n_l)
    R = [0] * (n_r)
    for i in range(n_l - 1):
        L[i] = A[p + i]
    for j in range(n_r - 1):
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
