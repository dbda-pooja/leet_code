class Solution:
    def missingCharacters(Str):
         MAX_CHAR = 26
    
         x = [False for i in range(MAX_CHAR)]
         for i in range(len(Str)):
            if (Str[i] >= 'a' and Str[i] <= 'z'):
                x[ord(Str[i]) - ord('a')] = True
        
         result = ""
 
         for i in range(MAX_CHAR):
            if (x[i] == False):
                 result += chr(i + ord('a'))
        
         return result

if __name__ == "__main__":
    s = Solution()
    print(s.missingCharacters("13579bdfgjkmnqrsuv"))