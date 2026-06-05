class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for k, v in enumerate(nums):
            diff = target - v
            if diff in mp:
                return [mp[diff], k]
            mp[v] = k