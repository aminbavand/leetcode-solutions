# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        current = result
        ten = 0
        stp = 0
        while (l1 is not None) or (l2 is not None):
            
            if l1 is None: l1 = ListNode()
            if l2 is None: l2 = ListNode()
            if stp>0:
                current.next = ListNode()
                current = current.next
            
            summ = ten + l1.val + l2.val
            current.val = summ%10
            ten = int(summ/10)
            
            l1 = l1.next
            l2 = l2.next
            stp+=1

        if ten==1:
            current.next = ListNode()
            current.next.val = 1
        
        return result
        
            
        