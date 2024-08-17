import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,num):
        node = self.root
        for i in range(29,-1,-1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
def find_min_xor(node,num,depth):
    xor_sum = 0
    for i in range(depth,-1,-1):
        bit = (num >> i) & 1
        if not bit in node.children:
            bit ^= 1
            xor_sum |= (1 << i)
        node = node.children[bit]
    return xor_sum

def find_minimum_xor_pair(set0,node1,depth):
    if depth < 0: return 0
    min_xor = float('inf')
    for num in set0:
        min_xor = min(min_xor,find_min_xor(node1,num,depth))
    return min_xor

def divide_and_conquer(numbers,node,depth):
    if depth < 0: return 0
    set1 = []
    set0 = []
    tmp = 1<<depth
    for num in numbers:
        if (num >> depth) & 1:
            set1.append(num - tmp)
        else:
            set0.append(num)
    _ret = 0
    if len(set1) > 0 and len(set0) > 0:
        _ret += find_minimum_xor_pair(set0,node.children[1],depth-1) + tmp
    if len(set1) >= 2:
        _ret += divide_and_conquer(set1,node.children[1],depth-1)
    if len(set0) >= 2:
        _ret += divide_and_conquer(set0,node.children[0],depth-1)
    return _ret

n = int(input())
numbers = list(map(int,input().split()))
trie = Trie()
for num in numbers:
    trie.insert(num)
print(divide_and_conquer(numbers,trie.root,29))