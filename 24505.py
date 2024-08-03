MOD = 10**9+7
N = int(input())
tree = [[0]*11 for _ in range(2*N)]

def update(idx, val, depth) :
  idx += N
  while idx :
    tree[idx][depth] = (tree[idx][depth]+val) % MOD
    idx //= 2

def search(left, right, depth) :
  left += N
  right += N
  res = 0
  while left <= right :
    if left % 2 :
      res += tree[left][depth]
      left += 1
    if right % 2 == 0 :
      res += tree[right][depth]
      right -= 1
    left //= 2
    right //= 2
  return res

nums = list(map(int, input().split()))
for i in range(N) :
  update(nums[i]-1, 1, 0)
  if nums[i] == 1 :
    continue
  for j in range(1, 11) :
    res = search(0, nums[i]-2, j-1)
    update(nums[i]-1, res, j)
print(tree[1][-1] % MOD)