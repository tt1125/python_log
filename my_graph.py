'''
Created on 2024/06/17

@author: Suguru Ueda
'''

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
        self.d = float('inf')
        self.pi = None
        
    def __str__(self):
        return str(self.name)

class MyGrapgh:
    
    def __init__(self, E, directed = False):
        
        # 無向グラフか有向グラフか設定
        self.directed = directed
        
        # 頂点集合を空の辞書形式で初期化
        self.V = {}
        
        # 隣接リストを空の辞書形式で初期化
        self.Adj = {}
        
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
        
            if not self.directed:   # 無向グラフの場合は，逆向きの処理も行う．
                # 頂点 v の隣接リストの末尾に頂点 u を追加する
                self.Adj[self.V[v]].append(self.V[u])
                
        # 描画用の networkx のグラフを作成
        if directed:
            self.G = nx.DiGraph(E)
        else:
            self.G = nx.Graph(E)
    
    def __str__(self):
        
        string = 'V = ' + str(set(self.V.keys()))
        
        for v in self.V.values():
            string += '\n' + 'Adj[' + str(v) + '] = ' + str([u.name for u in self.Adj[v]])
        
        return string
    
    def show(self):
        
        nx.draw(self.G, with_labels = True)
        plt.show()

if __name__ == '__main__':
    
    E = {(1, 2), (1, 5), (2, 3), (2, 4), (3, 4), (4, 5)}
    
    G = MyGrapgh(E)
    
    print(G)
    
    G.show()
    
