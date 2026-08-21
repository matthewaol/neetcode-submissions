# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res
        minHeap = []

        for l in lists:
            while l:
                heapq.heappush(minHeap, l.val)
                l = l.next

        if not minHeap:
            return None

        root = ListNode(heapq.heappop(minHeap))
        curr = root
        while minHeap:
            curr.next = ListNode(heapq.heappop(minHeap))
            curr = curr.next

        return root
