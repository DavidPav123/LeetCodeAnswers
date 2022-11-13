# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        else:
            vals = []
            cur_node = head
            while cur_node != None:
                vals.append(cur_node.val)
                cur_node = cur_node.next
            new_head = ListNode(val=vals.pop())
            prev_node = new_head
            while len(vals) > 0:
                cur_node = ListNode(val=vals.pop())
                prev_node.next = cur_node
                prev_node = cur_node
            return new_head
