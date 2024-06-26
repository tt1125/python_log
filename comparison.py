from insertion_sort import insertion_sort
from merge_sort import merge_sort
import random
import copy
import time
from matplotlib import pyplot as plt


def comparison():
    average_insertion = []
    average_merge = []
    m = 100
    for n in range(1000, 10001, 1000):
        print("process", n / 100, "%")
        time_insertion = 0
        time_merge = 0
        for _ in range(m):
            A = []
            for i in range(n):
                A.append(random.randint(0, 10 * n))

            B = copy.deepcopy(A)
            start_time = time.perf_counter()
            insertion_sort(B, len(B))
            end_time = time.perf_counter()
            time_insertion = time_insertion + end_time - start_time

            C = copy.deepcopy(A)
            start_time = time.perf_counter()
            merge_sort(C, 0, len(C) - 1)
            end_time = time.perf_counter()
            time_merge = time_merge + end_time - start_time

        average_insertion.append(time_insertion / m)
        average_merge.append(time_merge / m)
    plt.xlabel("input size")
    plt.ylabel("average computation time [ns]")
    plt.plot(
        range(1000, 10001, 1000),
        average_insertion,
        label="Insertion Sort",
        marker="o",  # rangeの上限を修正
    )
    plt.plot(
        range(1000, 10001, 1000),
        average_merge,
        label="Merge Sort",
        marker="s",  # rangeの上限を修正
    )
    plt.legend()
    plt.savefig("comparison.png")


if __name__ == "__main__":
    comparison()
