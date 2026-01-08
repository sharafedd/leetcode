class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                prod = nums1[i] * nums2[j]
                dp[i][j] = prod
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j], prod + max(dp[i-1][j-1], 0))
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
        
        return dp[n-1][m-1]