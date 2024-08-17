class SegmentTreeBeats:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.max1 = [0] * (4 * self.n)  # 최대값 저장
        self.max2 = [0] * (4 * self.n)  # 두 번째 최대값 저장
        self.min1 = [0] * (4 * self.n)  # 최소값 저장
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            self.max1[node] = data[start]
            self.min1[node] = data[start]
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            self._push_up(node)

    def _push_up(self, node):
        left = 2 * node + 1
        right = 2 * node + 2
        self.max1[node] = max(self.max1[left], self.max1[right])
        self.min1[node] = min(self.min1[left], self.min1[right])

        # 두 번째 최대값을 설정
        max1 = [self.max1[left], self.max1[right]]
        if self.max1[left] != self.max1[node]:
            max1.append(self.max1[left])
        if self.max1[right] != self.max1[node]:
            max1.append(self.max1[right])
        max1 = sorted(max1, reverse=True)
        self.max2[node] = max1[1]

    def _apply_max_limit(self, node, limit):
        if self.max1[node] <= limit:
            return
        self.tree[node] -= (self.max1[node] - limit) * self.count_max1[node]
        self.max1[node] = limit

    def range_max_limit(self, l, r, limit):
        self._range_max_limit(0, 0, self.n - 1, l, r, limit)

    def _range_max_limit(self, node, start, end, l, r, limit):
        if self.max1[node] <= limit:
            return

        if l <= start and end <= r and self.max2[node] < limit:
            self._apply_max_limit(node, limit)
            return

        mid = (start + end) // 2
        if l <= mid:
            self._range_max_limit(2 * node + 1, start, mid, l, r, limit)
        if mid < r:
            self._range_max_limit(2 * node + 2, mid + 1, end, l, r, limit)

        self._push_up(node)

    def range_min_query(self, l, r):
        return self._range_min_query(0, 0, self.n - 1, l, r)

    def _range_min_query(self, node, start, end, l, r):
        if r < start or end < l:
            return float('inf')

        if l <= start and end <= r:
            return self.min1[node]

        mid = (start + end) // 2
        left_min = self._range_min_query(2 * node + 1, start, mid, l, r)
        right_min = self._range_min_query(2 * node + 2, mid + 1, end, l, r)

        return min(left_min, right_min)


# 사용 예시
arr = [10, 20, 15, 7, 18, 22, 30]
stb = SegmentTreeBeats(arr)

# 구간 최대값 제한
stb.range_max_limit(1, 5, 15)

# 구간 최소값 쿼리
print(stb.range_min_query(1, 5))  # 출력: 7
