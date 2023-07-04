from typing import List

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        n=len(nums)-1
        for i in range(n):
            for j in range(i+1,n+1):
                if ((nums[i]+nums[j])==target):
                    return i,j


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([1,2,3,4,1],6))