from my_queue import MyQueue
from my_graph import MyGrapgh


WHITE = 0
GRAY = 1
BLACK = 2


def bfs(G, s):
    #
    for u in G.nodes:
        G.nodes[u]["color"] = WHITE
        G.nodes[u]["d"] = float("inf")
        G.nodes[u]["π"] = None

    # 開始ノードを初期化
    G.nodes[s]["color"] = GRAY
    G.nodes[s]["d"] = 0
    G.nodes[s]["π"] = None

    Q = MyQueue(len(G.nodes))
    Q.enqueue(s)

    while not Q.is_empty():
        u = Q.dequeue()
        for v in G.adj[u]:
            if G.nodes[v]["color"] == WHITE:
                G.nodes[v]["color"] = GRAY
                G.nodes[v]["d"] = G.nodes[u]["d"] + 1
                G.nodes[v]["π"] = u
                Q.enqueue(v)
        G.nodes[u]["color"] = BLACK
