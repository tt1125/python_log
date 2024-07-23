from pyparsing import C
import random
import copy
import time
from matplotlib import pyplot as plt


# from merge_sort import merge_sort
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


# from quicksort import quicksort


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


# from selection_sort import selection_sort


def selection_sort(A, n):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j > -1 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key


# from insertion_sort import insertion_sort


def insertion_sort(A, n):
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

    return A


def comparison():
    average_insertion = []
    average_merge = []
    average_quick = []
    average_selection = []
    m = 100
    for n in range(1000, 10001, 1000):
        print("process", n / 100, "%")
        time_insertion = 0
        time_merge = 0
        time_quick = 0
        time_selection = 0
        for _ in range(m):
            A = [random.randint(0, 10 * n) for i in range(n)]

            B = copy.deepcopy(A)
            start_time = time.perf_counter()
            merge_sort(B, 0, len(B) - 1)
            end_time = time.perf_counter()
            time_merge += (end_time - start_time) * 1000  # 秒をミリ秒に変換

            C = copy.deepcopy(A)
            start_time = time.perf_counter()
            quicksort(C, 0, len(C) - 1)
            end_time = time.perf_counter()
            time_quick += (end_time - start_time) * 1000  # 秒をミリ秒に変換

            D = copy.deepcopy(A)
            start_time = time.perf_counter()
            selection_sort(D, len(D))
            end_time = time.perf_counter()
            time_selection += (end_time - start_time) * 1000  # 秒をミリ秒に変換

            E = copy.deepcopy(A)
            start_time = time.perf_counter()
            insertion_sort(E, len(E))
            end_time = time.perf_counter()
            time_insertion += (end_time - start_time) * 1000  # 秒をミリ秒に変換

        average_insertion.append(time_insertion / m)
        average_merge.append(time_merge / m)
        average_quick.append(time_quick / m)
        average_selection.append(time_selection / m)

    plt.xlabel("input size")
    plt.ylabel("average computation time [ms]")  # ミリ秒単位に変更
    plt.plot(range(1000, 10001, 1000), average_merge, label="Merge Sort", marker="o")
    plt.plot(range(1000, 10001, 1000), average_quick, label="Quick Sort", marker="s")
    plt.plot(
        range(1000, 10001, 1000), average_selection, label="Selection Sort", marker="^"
    )
    plt.plot(
        range(1000, 10001, 1000), average_insertion, label="Insertion Sort", marker="v"
    )

    plt.legend()
    plt.savefig("comparison.png")


if __name__ == "__main__":
    comparison()
