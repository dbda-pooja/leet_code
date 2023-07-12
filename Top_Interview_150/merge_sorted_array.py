class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        for i in range(0,n):
            nums1[m+i]=nums2[i]
        temp = 0
        for i in range(0,len(nums1)):
            for j in range(i+1,len(nums1)):
                if nums1[i]>nums1[j]:
                    temp = nums1[i]
                    nums1[i] = nums1[j]
                    nums1[j] = temp
        return nums1
        



if __name__ == "__main__":
    s = Solution()
    print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))