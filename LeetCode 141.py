# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        temp=ListNode(0,head)
        left=head
        right=head
        cnt=0
        if head==None:
            return False
        while right.next!=None:
            left=head
            right=right.next
            cnt+=1
            for _ in range(cnt-1):
                left=left.next
                if left==right:
                    return True

        if cnt<10000:
            return False