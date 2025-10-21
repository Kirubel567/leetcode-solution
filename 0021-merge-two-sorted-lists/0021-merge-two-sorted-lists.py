# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            v1 = list1.val
            v2 = list2.val 

            if (v1 >= v2): 
                curr.next = ListNode(v2)
                list2 = list2.next
            else:
                curr.next = ListNode(v1)
                list1 = list1.next 
            curr = curr.next

        while list1:
            val = list1.val
            curr.next = ListNode(val)
            curr = curr.next 
            list1 = list1.next
        while list2:
            val = list2.val
            curr.next = ListNode(val)
            curr = curr.next
            list2 = list2.next
         
        return dummy.next 
