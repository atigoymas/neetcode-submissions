# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        nextNode, prevNode = None, None

        while temp != None:
            kthNode = self.findKth(temp, k)
            if not kthNode:
                if prevNode:
                    prevNode.next = temp
                break

            nextNode = kthNode.next
            kthNode.next = None
            newHead = self.reverse(temp)
            if temp == head:
                head = newHead
            else:
                prevNode.next = newHead

            prevNode = temp
            temp = nextNode
        return head
    
    def findKth(self, node, k):
        k -= 1
        while node and k > 0:
            node = node.next
            k -= 1
        return node
    
    def reverse(self, node):
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev
            
    
        







        