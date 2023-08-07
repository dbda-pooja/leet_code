class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """


        maximum_candy = max(candies)
        output = []
        
        for i in candies :
            total_candis = i + extraCandies
            output.append(total_candis>=maximum_candy)
        return output
            


if __name__=="__main__":
    s = Solution()
    print(s.kidsWithCandies([4,2,1,1,2],1))