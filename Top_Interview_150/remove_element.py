class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([0,1,2,2,3,0,4,2],2))