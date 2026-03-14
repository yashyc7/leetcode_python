# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #start with the slow and the fast pointers
        slow, fast = head , head
        while(fast and fast.next) :
            slow = slow.next
            fast = fast.next.next
        return slow # the middle Node of the linked list is this so we return the slow pointer such that the judge can traverse the remaining array 