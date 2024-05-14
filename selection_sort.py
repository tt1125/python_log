def selection_sort(A, n):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j > -1 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key


if __name__ == "__main__":
    A = [31, 41, 59, 26, 41, 58]
    selection_sort(A, 6)
    print(A)
