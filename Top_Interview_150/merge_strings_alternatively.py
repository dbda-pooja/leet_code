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
        j = 0
        
        if (len(word1) == len(word2)):
            while (i<m) and (j<n):
                merge_string = merge_string + word1[i] + word2[i]
                i = i+1
        elif(len(word1)< len(word2)):
            while (i<m) and (j<n):
                merge_string = merge_string + word1[j] + word2[i]
                i = i+1
                j = j+1
            merge_string = merge_string+word2[j:]
        else:
            while (i<m) and (j<n):
                merge_string = merge_string + word1[j] + word2[i]
                i = i+1
                j = j+1
            merge_string = merge_string+word1[i:]
        return merge_string
                  


if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("abc","p"))