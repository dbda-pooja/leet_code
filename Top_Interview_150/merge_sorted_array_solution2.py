class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        i = m-1
        j = n-1
        writer_pointer = m+n-1
    

        while(i >= 0 and j >= 0 ):
            if (nums1[i] < nums2[j]):
                nums1[writer_pointer] = nums2[j]
                writer_pointer = writer_pointer -1
                j = j-1
            else:
                nums1[writer_pointer] = nums1[i]
                writer_pointer = writer_pointer-1
                i = i-1

        while(i >= 0):
            nums1[writer_pointer] = nums1[i]
            writer_pointer = writer_pointer-1
            i = i-1

        while(j >= 0):
            nums1[writer_pointer] = nums2[j]
            writer_pointer = writer_pointer-1
            j = j-1

                    
               
        return nums1
           





if __name__ == "__main__":
    s = Solution()
    print(s.merge([1,2,3,0,0,0],3,[4,5,6],3))