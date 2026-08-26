# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def shown(link):
    s = ""
    while link:
        if link.next != None:
            s += f"{link.val} --> "
        else:
            s += f"{link.val}"
        link = link.next
    return s
class Solution:
    def addTwoNumbers(self, l1, l2):
        print(shown(l1))
        print(shown(l2))
        
        new = ListNode()
        new2 = new
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry 
            carry = val // 10
            val = val % 10
            new2.next = ListNode(val)
            
            new2 = new2.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        
        if carry > 0:
            new2.next = ListNode(carry)
        return new.next