class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-abs(x) for x in stones]
        heapq.heapify(pq)
        
        while len(pq) > 1:
            pq1 = heapq.heappop(pq)
            pq2 = heapq.heappop(pq)
            if pq1 == pq2:
                pass
            else:
                heapq.heappush(pq, pq1-pq2)

        return -1*pq[0] if pq else 0

        