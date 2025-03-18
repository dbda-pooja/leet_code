class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        n =  len(nums)
        
        for i in range(0,n):
            diff = target - nums[i]
            if diff in dict:
                return [dict[diff],i]
            dict[nums[i]] = i