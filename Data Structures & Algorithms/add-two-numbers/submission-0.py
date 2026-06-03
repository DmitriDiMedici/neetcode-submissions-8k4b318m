class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        actual = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            result = v1 + v2 + carry
            actual.next = ListNode((result % 10))
            carry = result // 10

            actual = actual.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next