class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        index = 0
        k = {}

        
        for j in  range(len(nums)):
            if nums[j] in k:
                k[nums[j]] +=1
            
            else:
                k[nums[j]] = 1
                nums[index] = nums[j]
                index = index + 1

        return index

        


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates( [0,0,1,1,1,2,2,3,3,4]))