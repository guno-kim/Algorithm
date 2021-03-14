class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA=headA
        nodeB=headB
        lenA=1;lenB=1;
        while nodeA.next==None:
            nodeA=nodeA.next
            lenA+=1
        while nodeB.next==None:
            nodeB=nodeB.next
            lenB+=1
        if nodeA!=nodeB:
            return null
            
        nodeA=headA
        nodeB=headB
        if lenA>lenB:
            for _ in range(lenA-lenB):
                nodeA=nodeA.next
        else:
            for _ in range(lenB-lenA):
                nodeB=nodeB.next
        nodeA=headA
        nodeB=headB
        while nodeA!=nodeB:
            nodeA=nodeA.next
            nodeB=nodeB.next
        return nodeA.value

