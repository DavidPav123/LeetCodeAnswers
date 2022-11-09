# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is not None and list2 is not None:
            l1node = list1
            l2node = list2

            if l1node.val > l2node.val:
                head_node = l2node
                cur_node = l2node
                l2node = l2node.next
            else:
                head_node = l1node
                cur_node = l1node
                l1node = l1node.next

            while l2node != None and l1node != None:
                if l1node.val < l2node.val:
                    cur_node.next = l1node
                    cur_node = l1node
                    l1node = l1node.next
                else:
                    cur_node.next = l2node
                    cur_node = l2node
                    l2node = l2node.next

            if l2node == None:
                cur_node.next = l1node
            else:
                cur_node.next = l2node

            return head_node

        elif list1 is not None:
            return list1
        elif list2 is not None:
            return list2
        else:
            return None
