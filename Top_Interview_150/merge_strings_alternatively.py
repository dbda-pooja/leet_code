class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge_string = ""
        n = len(word1)
        m = len(word2)
        i=0
        while  (i < n):
             if (len(word1) == len(word2)):
                merge_string = merge_string + word1[i] + word2[i]
             i = i+1
        # elif(len(word1)< len(word2)):
                         
        return merge_string
                  


if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("abc","pqr"))