ADDIND TWO NUMBERS USING LL
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# num 342 starts with LL and the digits are stored in 3 nodes(243), one for each in reverse direction
class LinkedList:
    def __init__(self, num):
        self.head = None
        self.num = 0
        if num == 0:
            numStr = ''
        else:
            numStr = str(num)
        for i in range(len(numStr[i])):
            digit = int(numStr[i])
            self.insert_head(digit)

    def insert_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            next = self.head
            self.head = new_node
            new_node.next = next

    def insert_tail(self, value):
        new_node = Node(value)
        current = self.head
        while current:
            if self.head is None:
                self.head = new_node
            else:
                self.head.next = new_node
                self.head = new_node


    def __add__(self, num2):
        sum = LinkedList(0)
        # a, b are pointers to self.head(num1) & num2 resp
        a = self.head
        b = num2
        carry = 0
        while a or b or carry:
            digit_sum = 0
            if a:
                digit_sum += a.value
            if b:
                digit_sum += b.value
            digit_sum += carry

            carry = digit_sum // 10
            digit_sum = digit_sum % 10

            sum.insert_tail(digit_sum)
            if a:
                a = a.next
            if b:
                b = b.next

    def __str__(self, num):
        s = ''
        current = self.head
        while current:
            s = str(current.value) + s
            current = current.next

        return s

num1 = LinkedList(342)
num2 = LinkedList(465)
num3 = num1 + num2

# REMOVE Kth NODE
Write a function that receives as input the head node of a linked list and an integer k. 
Your function should remove the kth node from the end of the linked list and return the head node of the updated list.

For example, if we have the following linked list: 
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null

The head node would refer to the node (20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node (14).

After the function executes, the state of the linked list should be:
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null

If k is longer than the length of the linked list, the linked list should not be changed.

Can you implement a solution that performs a single pass through the linked list and doesn't use any extra space?

def remove_kth_from_end(head, k):
    len_ll = 0
    current = head
    # finding the length of linked list
    while current:
        if current:
            len_ll += 1
            current = current.next
    # finding the node number from the end of the linked list
    i = len_ll - k
    previous = None
    j = 0
    current = head
    while current:
        # if head is the first node
        if i == 0:
            head = current.next
            break
        # node is found, previous node points to current/next node
        if j == i:
            previous.next = current.next
            break
        # if node is not found, the node moves on to the next node
        else:
            previous = current
            current = current.next
            j += 1
            
    return head

# remove duplicate number and return the linked list
Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. 
Your function should return a reference to the head of the updated linked list.

Example:
Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.


def condense_linked_list(node):
    current = node
    pass

def condense_linked_list2(node):
    data = {}
    new_head = node
    prev = None
    curr = node
    while curr:
        if curr.value in data:
            prev.next = curr.next
            curr = curr.next
        else:
            data[curr.value] = True
            prev = curr
            curr = curr.next
    return new_head

👍 Find Merge Point of Two Lists 👍
Given pointers to the head nodes of  linked lists that merge together at some point, find the node where the two lists merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's  value.
Note: After the merge point, both lists will share the same node pointers.

Example
In the diagram below, the two lists converge at Node x:

[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q

Ex:
1
  \
   2--->3--->NULL
  /
 1
 1--->2
      \
       3--->Null
      /
     1                     return 2,3

Function Description
Complete the findMergeNode function in the editor below.

findMergeNode has the following parameters:
SinglyLinkedListNode pointer head1: a reference to the head of the first list
SinglyLinkedListNode pointer head2: a reference to the head of the second list

Returns
int: the  value of the node where the lists merge(2,3)

# if heads are null, exchange
# Iterate thru list1 and list2 and compare node.value
# if node.value is same in both lists, return the value(data) of the node where the lists merge

def findMergeNode(head1, head2):
    curr1 = head1
    curr2 = head2
while curr1 and curr2:
    if id(curr1) == id(curr2):
        return curr1.data
    curr1 = curr1.next;
    curr2 = curr2.next;
    if curr1 is None:
        curr1 = head2
    if curr2 is None:
        curr2 = head1



