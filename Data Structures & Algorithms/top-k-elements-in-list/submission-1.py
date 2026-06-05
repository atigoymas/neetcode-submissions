class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums:
            mp[i] = 1 + mp.get(i, 0)
        minHeap = []
        for key, val in mp.items():
            heapq.heappush(minHeap, (val, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [val for key, val in minHeap]