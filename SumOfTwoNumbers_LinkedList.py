# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807..


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res= ListNode(0)
        tmp=res 
        # var for sum
        s=0
        # var for carryforward
        cf=0
        # till the time l1  exist or l2 exist or there is a carryforward
        while l1 or l2 or cf:
            if l1 :
                s+=l1.val
                l1=l1.next
            if l2:
                s+=l2.val
                l2=l2.next
            s+=cf
            # set the next node with value
            tmp.next=ListNode(s%10)
            cf=s/10
            s=0
            # iterate to next node
            tmp=tmp.next
        return res.next          
        


# Runtime: 68 ms, faster than 14.23% of Python online submissions for Add Two Numbers.
# Memory Usage: 12 MB, less than 12.50% of Python online submissions for Add Two Numbers.
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        