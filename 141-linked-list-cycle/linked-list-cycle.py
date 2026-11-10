# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # First Solution TC = O(n) SC = O(n)
        # arr = []
        
        # while head:
        #     if head.next in arr:
        #         return True
        #     arr.append(head.next)
        #     head = head.next

        # return False

        if not head:
            return False
            
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
        
