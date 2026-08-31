class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        prev = head
        curr = head.next

        index = 1
        first = -1
        last = -1

        minDist = float('inf')
        maxDist = -1

        while curr.next:

            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):

                # current node is critical
                if first == -1:
                    first = index
                else:
                    minDist = min(minDist, index - last)
                    maxDist = index - first

                last = index

            prev = curr
            curr = curr.next
            index += 1

        if maxDist == -1:
            return [-1, -1]

        return [minDist, maxDist]