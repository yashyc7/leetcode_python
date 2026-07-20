# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pointer = head # copying the head to transfer address 

        if pointer is None : 
            return head 
        while(pointer.next):
            if pointer.val == pointer.next.val : 
                pointer.next= pointer.next.next
            else : 
                pointer = pointer.next 
        return head                