class Solution(object):
    def hasCycle(self, head):
        first = head
        while first and first.next:
            head = head.next
            first = first.next.next
            if head is first:
                return True
        return False
