# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        present = head
        while present:
            x = present
            while x.next and x.next.val == present.val:
                x.next = x.next.next
            present = present.next
        return head    
        
        