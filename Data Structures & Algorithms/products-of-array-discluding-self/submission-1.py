class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        zero = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                prod *= nums[i] 
        for num in nums:
            if zero > 1:
                return [0]*len(nums)
            if zero ==1:
                res.append(prod if num == 0 else 0)
            else:
                res.append(prod//num)
        return res
        