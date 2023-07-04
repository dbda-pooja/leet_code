from typing import List



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elementCount = dict()
        for i in nums:
            if(elementCount.__contains__(i)):
                return True
            
            elementCount[i]=1

        return False



if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,4,1]))