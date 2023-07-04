class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """

        total_cost = 0
        for i in range (k):
            min_value = costs[0]
            min_value_index = 0
            for i in range(1,len(costs)):
                if costs[i] < min_value:
                    min_value = costs[i]  
                    min_value_index = i
           
            print(min_value)
            print(min_value_index)
            total_cost = total_cost + min_value
            costs.pop(min_value_index)
            
            print(total_cost)
            print(costs)
             
        return total_cost  


if __name__=='__main__':
    s = Solution()
    print(s.totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58],11,2))