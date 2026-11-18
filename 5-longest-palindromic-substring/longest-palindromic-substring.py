class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        final = ""

        for c in range(len(s)):

            # Odd Palindorme
            i, j = c, c
            while i>=0 and j<len(s) and s[i]==s[j]:
                if j + 1 - i > len(final):
                    final = s[i:j+1]
                i-=1
                j+=1

            # Even Palindorme
            i, j = c, c+1
            while i>=0 and j<len(s) and s[i]==s[j]:
                if j + 1 - i > len(final):
                    final = s[i:j+1]
                i-=1
                j+=1

        return final