# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(l):
    s = ""
    while l:
        if l.next != None:
            s += f"{l.val} -> "
        else:
            s += f"{l.val}"
        l = l.next
    return s

class Solution:
    def removeNthFromEnd(self, head, n: int):

        start = head
        long = 0
        while start:
            start = start.next
            long += 1
        
        remove = long - n
    
        
        # word = ""
        # while start and start.next:
        #     if stop == remove:
        #         word = start.val
        #         print(f"long: {stop}, remove: {remove}, word: {word}")
        #     start = start.next
        #     stop += 1
    
        
        # print(f"We want to remove index: {remove} which is {word}")

        print(f"remove: {remove}")

        if remove == 0:
            return head.next
        
        start = head
        index = 0
        while start:
            if index == remove - 1:
                start.next = start.next.next
                break
            start = start.next
            index += 1

        print(printList(head))

        
        print(f"Function: {head.val}, index: {index}")


        return head

                
        