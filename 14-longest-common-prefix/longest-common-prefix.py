class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        lcp = strs[0]

        for s in strs[1:]:
            while not s.startswith(lcp):
                lcp = lcp[:-1]
                if lcp == "":
                    return ""

        return lcp
        