"""
Created on 2024/05/24

@author: Suguru Ueda
"""

import math
import random
import copy

from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort, merge
from quicksort import quicksort, partition

# def selection_sort(A, n):

# def insertion_sort(A, n):

# def merge(A, p, q, r):

# def merge_sort(A, p, r):

# def partition(A, p, r):

# def quicksort(A, p, r):

if __name__ == "__main__":

    n = 100
    m = 10
    algorithms = {
        "selection_sort": True,
        "insertion_sort": True,
        "merge_sort": True,
        "quicksort": True,
    }

    for _ in range(m):

        A = [random.randint(0, 10 * n) for _ in range(n)]

        B = sorted(A)

        # 選択ソートのチェック
        if algorithms["selection_sort"]:

            C = copy.deepcopy(A)
            selection_sort(C, len(C))

            for i in range(n):
                if C[i] != B[i]:
                    algorithms["selection_sort"] = False
                    break

        # 挿入ソートのチェック
        if algorithms["insertion_sort"]:

            C = copy.deepcopy(A)
            insertion_sort(C, len(C))

            for i in range(n):
                if C[i] != B[i]:
                    algorithms["insertion_sort"] = False

        # マージソートのチェック
        if algorithms["merge_sort"]:

            C = copy.deepcopy(A)
            merge_sort(C, 0, len(C) - 1)

            for i in range(n):
                if C[i] != B[i]:
                    algorithms["merge_sort"] = False

        # クイックソートのチェック
        if algorithms["quicksort"]:

            C = copy.deepcopy(A)
            quicksort(C, 0, len(C) - 1)

            for i in range(n):
                if C[i] != B[i]:
                    algorithms["quicksort"] = False

    print(algorithms)
