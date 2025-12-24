class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """

        # Compute total number of apples
        num_apples = sum(apple)

        # Process boxes from largest to smallest
        for i, c in enumerate(sorted(capacity, reverse=True), 1):
            num_apples -= c

            if num_apples <= 0:
                return i
        
        # Fallback
        return i
            
        