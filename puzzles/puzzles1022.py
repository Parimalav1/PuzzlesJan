# 1.DECODE STRING
# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
# For example, there won't be input like 3a or 2[4].

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"


def decode_string(st):
    s = ''
    n = 0
    my_lst = []
    for ch in st:
        if ch.isdigit():
            n = n * 10 + int(ch)
            print(n)
        elif ch.isalpha():
            s += ch
        elif ch == '[':
            my_lst.append(s)
            my_lst.append(n)
            n = 0
            s = ''
        else:
            pre_n = my_lst.pop()
            pre_s = my_lst.pop()
            s = pre_s + pre_n * s
    return s

print(decode_string('3[a]2[bc]'))

# recursive solution
class Solution:
    i = -1
    # Recursive function that directly manipulates the string without having to create a dfs auxiliary function
    def decodeString(self, s):
        res, num = '', 0
        while self.i < len(s) - 1:
            self.i += 1
            if s[self.i].isdigit():
                num = num * 10 + int(s[self.i])
            elif s[self.i].isalpha():
                res += s[self.i]
            elif s[self.i] == '[':
                # Recursive call
                res += self.decodeString(s) * num
                num = 0
            elif s[self.i] == ']':
                return res
        return res


# 2.Merge two sorted list
# Merge two sorted linked lists and return it as a new sorted list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Example 1:
# Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]

# Example 2:
# Input: l1 = [], l2 = []
# Output: []

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next


class Solution3(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        run = True
        while run is True:
            # print('list one = |', l1,'|| list two = |',l2)
            if l1.next is None:
                print('None Next')
                run = False
            else:
                n = l1
                while n is not None:
                    print(n.val, " ")
                    print('next node ', n.next)
                    n = n.next
                run = False
