class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Fast/slow pointers to find half
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        # Reversing Linked List
        prev = None
        current = second_half

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        # Merging 2 sorted linked lists
        l1 = head
        l2 = prev

        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2
            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2