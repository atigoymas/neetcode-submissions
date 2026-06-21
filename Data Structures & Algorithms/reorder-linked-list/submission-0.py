# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        snd = slow.next
        prev = slow.next = None

        while snd:
            tmp = snd.next
            snd.next = prev
            prev = snd
            snd = tmp


        fst, snd = head, prev
        while snd:
            tmp1, tmp2 = fst.next, snd.next
            fst.next = snd
            snd.next = tmp1
            fst, snd = tmp1, tmp2



        

        
        