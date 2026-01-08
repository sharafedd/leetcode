class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif (not stack) or (stack[-1] != pairs[char]):
                    return False 
            else:
                stack.pop()
        
        return len(stack) == 0