# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            seen_vals = [head.val]
            pre_node = head
            cur_node = head.next
            while cur_node is not None:
                if cur_node.val not in seen_vals:
                    seen_vals.append(cur_node.val)
                    pre_node = cur_node
                    cur_node = cur_node.next
                else:
                    cur_node = cur_node.next
                    pre_node.next = cur_node
            return head
