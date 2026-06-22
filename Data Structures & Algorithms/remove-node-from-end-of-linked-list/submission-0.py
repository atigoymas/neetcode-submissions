# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head.next
        cnt = 1
        while node:
            cnt += 1
            node = node.next
        
        length = cnt - n 
        if length == 0:
            return head.next
        prev, curr, tmp  = None, head, head.next
        while length > 0:
            prev = curr
            curr = tmp
            tmp = tmp.next
            length -= 1
        
        prev.next = curr.next
        return head

            



            


        

        