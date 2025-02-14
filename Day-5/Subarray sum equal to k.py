class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
    
        for start in range(n):
           current_sum = 0
           for end in range(start, n):
               current_sum += nums[end]
               if current_sum == k:
                   count += 1
    
        return count