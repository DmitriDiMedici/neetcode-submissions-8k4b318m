class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        actual = head
        clones = {None: None}

        while actual:
            clone = Node(actual.val)
            clones[actual] = clone
            actual = actual.next
        
        actual = head
        while actual:
            clones[actual].next = clones[actual.next]
            clones[actual].random = clones[actual.random]
            actual = actual.next

        return clones[head]