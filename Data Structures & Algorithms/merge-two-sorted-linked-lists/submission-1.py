# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # def printList(l):
        #     s = ""
        #     while l:
        #         if l.next != None:
        #             s += f"{l.val} -> "
        #         else:
        #             s += f"{l.val}"
        #         l = l.next
        #     return s
        result = ListNode()
        save = result

        while list1 and list2:
            # print(f"list1: {list1.val}, list2: {list2.val}")
            if list1.val > list2.val:
                # print(f"list1 > list2: {list1.val} > {list2.val}")
                result.next = list2
                list2 = list2.next
            else:
                # print(f"list1 < list2: {list1.val} < {list2.val}")
                result.next = list1
                list1 = list1.next
            result = result.next
            # print(f'result: {printList(save)}')
            # print(f"!----")

        if list1:
            result.next = list1
        else:
            result.next = list2
        save = save.next

        # print(f'final: {printList(save)}')

        return save
