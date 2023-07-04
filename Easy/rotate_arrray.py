from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            n=nums[len(nums)-1]
            nums.pop()
            nums.insert(0,n)

if __name__ == "__main__":
    s = Solution()
    print(s.rotate([1,2,3,4,5,6,7],3))