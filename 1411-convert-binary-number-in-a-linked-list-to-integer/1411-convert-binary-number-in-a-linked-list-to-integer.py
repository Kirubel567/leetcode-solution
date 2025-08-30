# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head 
        output = ""
        while temp: 
            output += str(temp.val)
            temp = temp.next
        num = int(output, 2)

        return num
        