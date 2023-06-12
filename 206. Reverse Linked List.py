# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        List = head
        new_list = None
        while List:
            list_node = List.next
            List.next = new_list
            new_list = List
            List = list_node
        return new_list