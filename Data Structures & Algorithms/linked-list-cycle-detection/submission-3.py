# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = head
        j = head
        while j and j.next: 
            if j.next == None:
                return False
            i = i.next
            j = j.next
            j = j.next
            if j == i:
                return True
        return False
        # while start:
        #     print(f"Val: {start.val}")
        #     print(f"{start.val} < {i} and {start.next == i}")
        #     if start.val < i and start.next == i:
        #         return True
        #     start = start.next
        #     i += 1
        #     if i > 10:
        #         break
        # return False
        