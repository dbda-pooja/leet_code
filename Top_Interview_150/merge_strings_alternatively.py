class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1)+len(word2)
        for i in range(n):
            if  


if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("abc","pqr"))