import sys
input = sys.stdin.readline

def propagate_segment_tree(index,start,end): # 이 함수를 실행하면 seg_tree[index]의 값이 update되었음이 보장됨.
    if lazy[index] != 0:
        seg_tree[index] = (end-start+1) - seg_tree[index]
        if start != end:
            lazy[2*index] ^= 1
            lazy[2*index+1] ^= 1
        lazy[index] = 0

def update_segment_tree(index,start,end,left,right):
    propagate_segment_tree(index,start,end)

    if right < start or end < left:
        return
    
    if left <= start and end <= right:
        seg_tree[index] = (end-start+1) - seg_tree[index]
        if start != end:
            lazy[2*index] ^= 1
            lazy[2*index+1] ^= 1
        return
    
    mid = (start+end) >> 1
    update_segment_tree(2*index,start,mid,left,right)
    update_segment_tree(2*index+1,mid+1,end,left,right)
    seg_tree[index] = seg_tree[2*index] + seg_tree[2*index+1]

def query_segment_tree(index,start,end,left,right):
    propagate_segment_tree(index,start,end)

    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return seg_tree[index]
    
    mid = (start+end) >> 1
    return query_segment_tree(2*index,start,mid,left,right) + query_segment_tree(2*index+1,mid+1,end,left,right)

n,m = map(int,input().split())
seg_tree = [0]*(4*n)
lazy = [0]*(4*n)
for _ in range(m):
    o,s,t = map(int,input().split())
    if o == 0:
        update_segment_tree(1,1,n,s,t)
    else:
        print(query_segment_tree(1,1,n,s,t))