# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head
        arr=[]
        while fast:
            fast=fast.next.next
            arr.append(slow.val)
            slow=slow.next
        max_sum=0
        while slow:
            max_sum=max(max_sum,slow.val+arr.pop())
            slow=slow.next
        return max_sum


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def middle(self,head:Optional[ListNode])->int:
#         slow=fast=head
#         i=0
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#             i=i+1
#         return slow,i
#     def nreversed(self,head:Optional[ListNode])->int:
#         prev=None
#         curr=head
#         while curr:
#             no=curr.next
#             curr.next=prev
#             prev=curr
#             curr=no
#         return prev

#     def pairSum(self, head: Optional[ListNode]) -> int:
#         if head is None:
#             return
#         node,idx=self.middle(head)
#         rev=self.nreversed(node)
#         maxi=0
#         straight=head
#         reve=rev
#         for i in range(idx):
#             maxi=max(maxi,straight.val+reve.val)
#             straight=straight.next
#             reve=reve.next
#         return maxi
        