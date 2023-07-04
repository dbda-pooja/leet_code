from typing import List



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z=0  
        n= len(nums)
        for i in range(n):
            if nums[i] ==0 :
                z=z+1
            elif z>0:
                temp = nums[i]
                nums[i]= 0 
                nums[i-z] = temp
        return nums
        


if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))