class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if i - dic[nums[i]] <= k:
                    return True
                dic[nums[i]] = i
        return False
    

if __name__=='__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1],3))