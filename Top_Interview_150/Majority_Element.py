class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math

        k = {}
        n = len(nums)
        for i in nums:
            if i in k:
                k[i] = k[i]+1

            else:
                k[i] = 1
        for i in k:
            if k[i] > math.floor(n/2):
                return i



if __name__ == "__main__" :
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))