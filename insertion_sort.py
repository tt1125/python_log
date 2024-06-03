def insertion_sort(A, n):
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

    return A


if __name__ == "__main__":
    A = [31, 41, 59, 26, 41, 58]
    insertion_sort(A, 6)
    print(A)
