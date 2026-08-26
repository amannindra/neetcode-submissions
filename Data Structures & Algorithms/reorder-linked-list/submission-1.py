# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        length_s = 0
        length_f = 0
        slow = head
        fast = head

     

        while fast and fast.next:
            print(f"Slow Val: {slow.val}, Fast Val: {fast.val}")
            slow = slow.next
            fast = fast.next
            fast = fast.next
            length_s += 1
            length_f += 2
        print(f"length S: {length_s}")
        print(f"length F: {length_f}")
        second = slow.next
        prev = None
        slow.next = None


        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # print(f'second: {second}')
        second = prev
        
        # merge
        
        first, second = head, prev 
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
        # merge

#        while head and second:

        




            

        