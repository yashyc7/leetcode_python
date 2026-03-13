# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # i am using the slow and the fast pointer approach in this question so 
        # starting with the slow and fast pointers

        slow = head
        fast = head 
        while (fast!=None) and (fast.next!=None):
            # move the slow pointer one time and then 
            # move the fast pointer two times for detecting cycle 
            slow = slow.next
            fast = fast.next.next

            if slow  == fast : 
                return True # if the pointeres meet at place then it mean the cycle has been found then return the true
        return False # otherwise return false 