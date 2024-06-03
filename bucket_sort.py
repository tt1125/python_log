from insertion_sort import insertion_sort


def Bucket_Sort(A, n):
    B = [[] for _ in range(n)]

    for i in range(n):
        index_b = int(n * A[i])
        B[index_b].append(A[i])

    for i in range(n):
        B[i] = insertion_sort(B[i], len(B[i]))

    sorted_A = []
    for i in range(n):
        sorted_A += B[i]

    return sorted_A


# if __name__ == "__main__":
#     A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
#     n = len(A)
#     sorted_A = Bucket_Sort(A, n)
#     print(sorted_A)
