"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None:None}

        cur = head
        while cur:
            node = Node(cur.val)
            mp[cur] = node
            cur = cur.next
        
        cur = head
        while cur:
            node = mp[cur]
            node.next = mp[cur.next]
            node.random = mp[cur.random]
            cur = cur.next
        return mp[head]

        

        
        