class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)
    
    def _propagate(self, node, node_start, node_end):
        if self.lazy[node] != 0:
            self.tree[node] += (node_end - node_start + 1) * self.lazy[node]
            if node_start != node_end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0
    
    def _update_range(self, node, node_start, node_end, start, end, value):
        self._propagate(node, node_start, node_end)
        if start > node_end or end < node_start:
            return
        if start <= node_start and node_end <= end:
            self.lazy[node] += value
            self._propagate(node, node_start, node_end)
            return
        mid = (node_start + node_end) // 2
        self._update_range(2 * node + 1, node_start, mid, start, end, value)
        self._update_range(2 * node + 2, mid + 1, node_end, start, end, value)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def update_range(self, start, end, value):
        self._update_range(0, 0, self.size - 1, start, end, value)
    
    def _query_range(self, node, node_start, node_end, start, end):
        self._propagate(node, node_start, node_end)
        if start > node_end or end < node_start:
            return 0
        if start <= node_start and node_end <= end:
            return self.tree[node]
        mid = (node_start + node_end) // 2
        left_sum = self._query_range(2 * node + 1, node_start, mid, start, end)
        right_sum = self._query_range(2 * node + 2, mid + 1, node_end, start, end)
        return left_sum + right_sum
    
    def query_range(self, start, end):
        return self._query_range(0, 0, self.size - 1, start, end)


class HLD:
    def __init__(self, n):
        self.n = n
        self.tree = [[] for _ in range(n)]
        self.size = [0] * n
        self.parent = [-1] * n
        self.depth = [0] * n
        self.chain_head = [-1] * n
        self.chain_index = [-1] * n
        self.pos_in_base = [-1] * n
        self.base_array = []
        self.seg_tree = None
        self.ptr = 0

    def add_edge(self, u, v): # 간선들을 추가하는 함수
        self.tree[u].append(v)
        self.tree[v].append(u)

    def dfs(self, v): # v를 root로 했을 때의 size 행렬을 구축하는 함수
        self.size[v] = 1
        for u in self.tree[v]:
            if u == self.parent[v]:
                continue
            self.parent[u] = v
            self.depth[u] = self.depth[v] + 1
            self.size[v] += self.dfs(u)
        return self.size[v]

    def hld(self, v):
        if self.chain_head[self.ptr] == -1:
            self.chain_head[self.ptr] = v
        self.chain_index[v] = self.ptr
        self.pos_in_base[v] = len(self.base_array)
        self.base_array.append(0)  # Initial value in the segment tree
        
        heaviest_child = -1
        for u in self.tree[v]:
            if u != self.parent[v] and (heaviest_child == -1 or self.size[u] > self.size[heaviest_child]):
                heaviest_child = u
        
        if heaviest_child != -1:
            self.hld(heaviest_child)
        
        for u in self.tree[v]:
            if u != self.parent[v] and u != heaviest_child:
                self.ptr += 1
                self.hld(u)

    def build_segment_tree(self):
        self.seg_tree = SegmentTree(len(self.base_array))

    def update_path(self, u, v, value):
        while self.chain_index[u] != self.chain_index[v]:
            if self.depth[self.chain_head[self.chain_index[u]]] < self.depth[self.chain_head[self.chain_index[v]]]:
                u, v = v, u
            self.seg_tree.update_range(self.pos_in_base[self.chain_head[self.chain_index[u]]], self.pos_in_base[u], value)
            u = self.parent[self.chain_head[self.chain_index[u]]]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        self.seg_tree.update_range(self.pos_in_base[u], self.pos_in_base[v], value)

    def query_path(self, u, v):
        result = 0
        while self.chain_index[u] != self.chain_index[v]:
            if self.depth[self.chain_head[self.chain_index[u]]] < self.depth[self.chain_head[self.chain_index[v]]]:
                u, v = v, u
            result += self.seg_tree.query_range(self.pos_in_base[self.chain_head[self.chain_index[u]]], self.pos_in_base[u])
            u = self.parent[self.chain_head[self.chain_index[u]]]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        result += self.seg_tree.query_range(self.pos_in_base[u], self.pos_in_base[v])
        return result


# Example usage:
n = 5
hld = HLD(n)
edges = [(0, 1), (0, 2), (1, 3), (1, 4)]

for u, v in edges:
    hld.add_edge(u, v)

hld.dfs(0)
hld.hld(0)
hld.build_segment_tree()

# Perform updates and queries
hld.update_path(3, 4, 5)  # Update path from node 3 to node 4 with value 5
print(hld.query_path(3, 4))  # Query the path from node 3 to node 4
