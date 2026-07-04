class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        (x, y) = (0, 0)
        pq = []
        for i in points:
            x1, y1 = i
            dist = ((x-x1)**2 + (y-y1)**2) ** 0.5
            heapq.heappush(pq, (-dist, i))
            while len(pq) > k:
                heapq.heappop(pq)
        return [val for dist, val in pq]