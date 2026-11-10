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
        
        arr = []
        
        while head:
            if head.next in arr:
                return True
            arr.append(head.next)
            head = head.next

        return False