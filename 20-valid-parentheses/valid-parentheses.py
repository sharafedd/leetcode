class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        myhash = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        mystack = []

        for ch in s:
            if ch in myhash:
                if not mystack or mystack.pop() != myhash[ch]:
                    return False
            else:
                mystack.append(ch)

        return not mystack

