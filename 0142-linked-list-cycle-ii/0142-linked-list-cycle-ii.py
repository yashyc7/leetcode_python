# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # here we have the linked list with the head 
        # what we would do is to use the floyd cycle detection algorithm here 
        #start slow and the fast pointer with the head 

        slow,fast = head , head 

        # iterate with slow with x 1 and with fast with x 2 speed
        while(fast and fast.next):
            slow,fast = slow.next , fast.next.next
            if slow==fast :  # if they meet at some point then break out of loop 
                break 
        else: 
            return None  
        # outside loop we must set the slow at the point head and leave fast as it is 
        slow = head 
        # iterate them untill they meet again 

        while(slow!=fast): 
            slow = slow.next
            fast = fast.next

        return slow