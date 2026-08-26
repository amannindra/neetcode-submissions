# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printSol(self, head):
        s = ""
        while head != None:
            s += str(head.val) + " -> "
            head = head.next
        print(s)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        
        current = head
        if current == None:
            return current
        self.printSol(current)

        while current != None:
            # print(f"Current: {current.val}")
            after = current.next
            current.next = prev

            prev = current
            current = after
            self.printSol(prev)
        # current = prev
        self.printSol(prev)

        return prev

        

            
        