# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node1 = l1
        cur_node2 = l2
        num1 = ""
        num2 = ""
        while cur_node1 is not None:
            num1 += str(cur_node1.val)
            cur_node1 = cur_node1.next      

        while cur_node2 is not None:
            num2 += str(cur_node2.val)
            cur_node2 = cur_node2.next

        final_val = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        head = ListNode(val=int(final_val[0]))
        prev_node = head
        for i in range(1, len(final_val)):
            next_node = ListNode(val=int(final_val[i]))
            prev_node.next = next_node
            prev_node = next_node

        return head