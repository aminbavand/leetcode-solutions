# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        setNodes = {head}
        current_element = head
        while (current_element!=None):
            current_element = current_element.next    
            if current_element is None:
                return False            
            if current_element in setNodes:
                return True
            setNodes.add(current_element)
        return False