__author__ = 'ay27'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x = y = 0
        px = py = 1
        while l1 is not None:
            x += px*l1.val
            px *= 10
            l1 = l1.next
        while l2 is not None:
            y += py*l2.val
            py *= 10
            l2 = l2.next
        z = x+y

        head = p = ListNode(z % 10)
        z //= 10
        while z != 0:
            q = ListNode(z % 10)
            p.next = q
            p = q
            z //= 10
        return head


ll1 = ListNode(9)
ll1.next = ListNode(9)
ll1.next.next = ListNode(2)
ll2 = ListNode(9)
ll2.next = ListNode(9)
ll2.next.next = ListNode(9)

l3 = Solution().addTwoNumbers(ll1, ll2)
print('finish')