
##########################################
# LeetCode – Plus One Linked List (Java)
##########################################


# Given a non-negative number represented as a singly linked list of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.
# Example:

# Input:
# 1->2->3

# Output:
# 1->2->4



# V1 : dev 
# def add_one_list(list_):
#     extra = 0 
#     count = 0 
#     output = []
#     for i in list_[::-1]:
#         print ('i : ', i)
#         if count==0:
#             i = i + 1 + extra         
#         i = i + extra
#         if i >= 10:
#             i = i%10 
#             extra = 1  
#         else:
#             extra = 0 
#         output.append(i)
#         count = count + 1
#     if extra==1:
#         output.append(1)
#     return  output[::-1]

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        my_list = []
        while head:
            my_list.append(head.val)
            head = head.next 
        extra = 0 
        count = 0 
        output = []
        for i in list_[::-1]:
            if count==0:
                i = i + 1 + extra         
            i = i + extra
            if i >= 10:
                i = i%10 
                extra = 1  
            else:
                extra = 0 
            output.append(i)
            count = count + 1
        if extra==1:
            output.append(1)
        return  output[::-1]

# V2 
# https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/369.Plus%20One%20Linked%20List.md
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = []
        cur = head 

        while cur:
            lst.append(cur)
            cur = cur.next

        carry = 1
        for i in range(len(lst)-1,-1,-1):
            lst[i].val += carry
            if lst[i].val < 10:
                carry = 0
                break
            else:
                lst[i].val -= 10

        if carry == 1:
            node = ListNode(1)
            node.next = head
            return node
        else:
            return head 

# V3 
# Time:  O(n)
# Space: O(1)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Two pointers solution.
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        left, right = dummy, head
        while right.next:
            if right.val != 9:
                left = right
            right = right.next

        if right.val != 9:
            right.val += 1
        else:
            left.val += 1
            right = left.next
            while right:
                right.val = 0
                right = right.next

        return dummy if dummy.val else dummy.next


# V4 
# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverseList(head):
            dummy = ListNode(0)
            curr = head
            while curr:
                dummy.next, curr.next, curr = curr, dummy.next, curr.next
            return dummy.next

        rev_head = reverseList(head)
        curr, carry = rev_head, 1
        while curr and carry:
            curr.val += carry
            carry = curr.val / 10
            curr.val %= 10
            if carry and curr.next is None:
                curr.next = ListNode(0)
            curr = curr.next

        return reverseList(rev_head)