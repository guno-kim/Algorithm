# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp=ListNode(-1,head)
        left=temp
        right=temp
        for _ in range(n):
            right=right.next
        while right.next!=None:
            right=right.next
            left=left.next
        left.next=left.next.next

        return temp.next

        