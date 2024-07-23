"""
Created on 2024/06/03

@author: Suguru Ueda
"""


class MyQueue:

    def __init__(self, n):

        # 配列Qの初期化
        self.queue = [None] * n

        # 属性Q.size, Q.top, Q.tailの設定
        self.size = n
        self.head = 0
        self.tail = 0

    def is_empty(self):

        return self.head == self.tail

    def enqueue(self, x):

        self.queue[self.tail] = x

        if self.tail == self.size:
            self.tail = 0
        else:
            self.tail = self.tail + 1

    def dequeue(self):

        x = self.queue[self.head]

        if self.head == self.size:
            self.head = 0
        else:
            self.head = self.head + 1

        return x

    def __str__(self):

        if self.is_empty():
            return str([])
        elif self.head <= self.tail:
            return str(self.queue[self.head : self.tail])
        else:
            return str(self.queue[self.head :] + self.queue[: self.tail])


if __name__ == "__main__":

    Q = MyQueue(6)

    Q.enqueue(4)
    Q.enqueue(1)
    Q.enqueue(3)

    print(Q)

    print("DEQUEUE(Q):", Q.dequeue())

    print(Q)

    Q.enqueue(8)

    print(Q)

    print("DEQUEUE(Q):", Q.dequeue())

    print(Q)
