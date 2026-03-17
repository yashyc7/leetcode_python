class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        # Step 1: Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Compare (MOVED OUTSIDE)
        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True