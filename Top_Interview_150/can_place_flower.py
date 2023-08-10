class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed_len  = len(flowerbed)
       
        for i in range (0,flowerbed_len) :
            if(n != 0):
                if flowerbed[0] == 0:
                    if flowerbed_len == 1:
                        flowerbed[0] = 1
                        n = n-1
                    else:
                        if flowerbed[1] == 0:
                            flowerbed[0] = 1
                            n = n-1
                        
        
                elif flowerbed[i] == 0 :
                    if (flowerbed[i-1] == 0 and flowerbed[i+1]==0) :
                        flowerbed[i] = 1
                        n = n-1

                elif flowerbed[flowerbed_len-1] == 0:
                    if flowerbed[flowerbed_len-2] == 0:
                        flowerbed[flowerbed_len-1] = 1
                        n = n-1
                    
                
        if (n == 0):
            return True
        else :
            return False

        
            

        







if __name__== "__main__":
    s = Solution()
    print(s.canPlaceFlowers([0,0,1,0,0,0,1],2))