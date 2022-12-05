# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
import math


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total_size = 0
        cur_node_count =0
        cur_node = head
        while cur_node != None:
            total_size += 1
            cur_node = cur_node.next
        cur_node = head
        while cur_node_count != math.ceil(total_size/2):
            cur_node = cur_node.next
            cur_node_count += 1
        return cur_node