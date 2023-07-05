'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.



Constraints:

    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100
'''
#Much cleaner solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    class Solution:
        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            middle = end = head
            while end.next:
                middle = middle.next  # Advance by 1 step
                if end.next.next:
                    end = end.next.next  # Advance by 2 steps
                else:
                    break
            return middle

#Really bad, no good solution
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals=[]
        i=0
        while head.next!=None:
            vals.append({head.next.val:head.next})
            head.next=head.next.next
            i+=1
        if i%2==0:
            mid=i//2
        else:
            mid=i//2+1
        answer=ListNode()
        if len(vals)!=0:
            keys=list(vals[mid-1].keys())
            answer.val=keys[0]
            answer.next=vals[mid-1][keys[0]].next
        else:
            answer.val=head.val
            answer.next=head.next
        return answer