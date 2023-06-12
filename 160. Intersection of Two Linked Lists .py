# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        Set = set()
        List = headA

        while List:
            Set.add(List)
            List = List.next

        List = headB
        while List:
            if List in Set:
                return List
            List = List.next

        return None