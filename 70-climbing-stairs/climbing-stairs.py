class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # In order to reach step n there are only two ways: n - 1, n - 2
        # Which gives us the follwing relationship: f(n) = f(n-1) + (n-2)
        # Which is a Fibonacci

        # if n<3:
        #     return n
        
        # one = 1
        # two = 2

        # for _ in range(3, n+1):
        #     current = one + two
        #     one = two
        #     two = current
        
        # return two

        # Optimisation
        one, two = 0, 1
        for _ in range(n):
            one, two = two, one + two
        return two

