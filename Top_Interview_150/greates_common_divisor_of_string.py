class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        gcd_string = ""
        n = len(str1)
        m = len(str2)
        i = 0
        j = 0
        while (i<n) and (j<m):
            if(n <= m):

                if (str1[i] == str2[j]):
                    gcd_string = gcd_string + str1[i]
                else:
                    break
            else :
                if (str1[i] == str2[j]):
                    gcd_string = gcd_string + str1[j]
                else:
                    break

            i = i+1
            j = j+1
        return gcd_string




if __name__=="__main__":
    s = Solution()
    print(s.gcdOfStrings("ABABAB","ABACABAB"))