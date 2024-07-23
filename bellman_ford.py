"""
Created on 2024/06/17

@author: Suguru Ueda
"""

import networkx as nx
import matplotlib.pyplot as plt

# グラフ探索に用いる色
WHITE = 0
GRAY = 1
BLACK = 2


class MyVertex:

    def __init__(self, name):
        # 頂点属性
        self.name = name
        self.color = WHITE
        self.d = float("inf")
        self.pi = None

    def __str__(self):
        return str(self.name)


class MyGrapgh:

    def __init__(self, E, directed=False):
        # 無向グラフか有向グラフか設定
        self.directed = directed

        # 頂点集合を空の辞書形式で初期化
        self.V = {}

        # 隣接リストを空の辞書形式で初期化
        self.Adj = {}

        self.edges = []

        for e in E:
            u, v = e

            # 頂点 u が V に登録されていないとき，頂点 u を作成し，u の空の隣接リストを作成する
            if u not in self.V.keys():
                self.V[u] = MyVertex(u)
                self.Adj[self.V[u]] = []

            # 頂点 v が V に登録されていないとき，頂点 v を作成し，v の空の隣接リストを作成する
            if v not in self.V.keys():
                self.V[v] = MyVertex(v)
                self.Adj[self.V[v]] = []

            # 頂点 u の隣接リストの末尾に頂点 v を追加する
            self.Adj[self.V[u]].append(self.V[v])
            self.edges.append((self.V[u], self.V[v]))  # エッジを追加

            if not self.directed:  # 無向グラフの場合は，逆向きの処理も行う．
                # 頂点 v の隣接リストの末尾に頂点 u を追加する
                self.Adj[self.V[v]].append(self.V[u])
                self.edges.append((self.V[v], self.V[u]))  # 逆向きのエッジを追加

        # 描画用の networkx のグラフを作成
        if directed:
            self.G = nx.DiGraph(E)
        else:
            self.G = nx.Graph(E)

    def __str__(self):
        string = "V = " + str(set(self.V.keys()))
        for v in self.V.values():
            string += (
                "\n" + "Adj[" + str(v) + "] = " + str([u.name for u in self.Adj[v]])
            )
        return string

    def show(self):
        nx.draw(self.G, with_labels=True)
        plt.show()


def initialize_single_source(G, s):
    for v in G.V.values():
        v.d = float("inf")
        v.pi = None
    s.d = 0


def relax(u, v, w):
    if v.d > u.d + w[(u.name, v.name)]:
        v.d = u.d + w[(u.name, v.name)]
        v.pi = u


def bellman_ford(G, w, s):
    initialize_single_source(G, s)

    for _ in range(len(G.V) - 1):
        for u, v in G.edges:
            relax(u, v, w)

    for u, v in G.edges:
        if u.d != float("inf") and u.d + w[(u.name, v.name)] < v.d:
            return False  # Negative weight cycle found

    return True


def show_shortest_path(G, w):
    TSP = nx.DiGraph()

    for v in G.V.values():
        if v.pi is not None:
            TSP.add_edge(v.pi.name, v.name, weight=w[(v.pi.name, v.name)])

    edge_labels = {(i, j): w for i, j, w in TSP.edges(data="weight")}

    pos = nx.spring_layout(TSP)

    nx.draw(TSP, pos, with_labels=True)
    nx.draw_networkx_edge_labels(TSP, pos, edge_labels=edge_labels)
    plt.show()


if __name__ == "__main__":
    E = {
        ("s", "t"),
        ("s", "y"),
        ("t", "x"),
        ("t", "y"),
        ("t", "z"),
        ("x", "t"),
        ("y", "x"),
        ("y", "z"),
        ("z", "s"),
        ("z", "x"),
    }

    w = {
        ("s", "t"): 6,
        ("s", "y"): 7,
        ("t", "x"): 5,
        ("t", "y"): 8,
        ("t", "z"): -4,
        ("x", "t"): -2,
        ("y", "x"): -3,
        ("y", "z"): 9,
        ("z", "s"): 2,
        ("z", "x"): 7,
    }

    G = MyGrapgh(E, directed=True)

    if bellman_ford(G, w, G.V["s"]):
        show_shortest_path(G, w)
    else:
        print("グラフに負の閉路が存在します。")
