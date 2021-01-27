# can binary search help us in this case?
# 🛑 binary search requires us to know our target 🛑
# improved the runtime from O(n) to O(log n)
def find_smallest_missing(arr):
    if arr[0] != 0:
        return 0

    # add another check here to see if arr[-1] == len(arr) - 1
    if arr[-1] == len(arr) - 1:
        # no elements are missing 
        return len(arr)

    start = 0
    end = len(arr) - 1
    
    while start < end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            # toss out the left side
            # don't include the midpoint since we know 
            # it matches its index 
            start = mid + 1

        else:
            # toss out the right 
            # but do keep the midpoint, since we can't 
            # rule out that it might be the smallest missing
            end = mid 
    
    # we've narrowed it down to one element 
    # at this point start == end, so return either 
    return start
    
    # O(n) traversal through the entire array 
    # realizing that we're not taking advantage of the fact that 
    # the input is sorted, we can ask ourselves how to leverage 
    # that fact 
#    for i in range(len(arr) - 1):
#        if arr[i+1] != arr[i] + 1:
#            return arr[i] + 1
#
#    return arr[-1] + 1

A1 = [0,1,2,6,9,11,15]
A2 = [1,2,3,4,6,9,11,15]
A3 = [0,1,2,3,4,5,6]
A4 = [3,6,9,15,18]
A5 = [0,1,3,6,9,11,15]
A6 = [0,1,2,3,4,5,7,8]

print(find_smallest_missing(A1))
print(find_smallest_missing(A2))
print(find_smallest_missing(A3))
print(find_smallest_missing(A4))
print(find_smallest_missing(A5))
print(find_smallest_missing(A6))

🔵 Given the root of a binary tree where each node contains an integer, 🔵
determine the sum of all of the integer values in the tree.

Example:

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
The expected output given the above tree is 5 + 4 + 8 + 11 + 13 + 4 + 7 + 2 + 1, so your function should return 55.

def tree_paths_sum(root):
    pass

🟩 Sum Root to Leaf Numbers 🟩
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

EX:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

# Use recursion
# Keep a accumulator - a variable to store the sum of values that we've seen so for
# Check if there is not a lf or rt side, if no->this is a leaf 
# Now that we're on a leaf, v need to add the new root-to-leaf path no to the accumulator.
# V can keep track of the no that we've seen so far by passing them to a current_sum
# Do the same with lf and rt sides at root level.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sum_recursive(self, node, root_to_node_sum):
        root_to_node_sum += str(node.val)
        if not node.left or not node.right:
            # I'm at a leaf node
            self.current_sum += int(root_to_node_sum)
        elif node.left:
            self.sum_recursive(node.left, root_to_node_sum)
        elif node.right:
            self.sum_recursive(node.right, root_to_node_sum)

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        self.current_sum = 0
        if root.left:
            self.sum_recursive(root.left, str(root.val))
        if root.right:
            self.sum_recursive(root.right, str(root.val))

        return current_sum

🍀 Binary Search Tree : Lowest Common Ancestor 🍀
You are given pointer to the root of the binary search tree and two values v1 and v2. You need to return the lowest common ancestor (LCA) of v1 and v2 in the binary search tree.
EX:
     ⭕️      2
   ⭕️   ⭕️    1,3
      ⭕️  ⭕️  4,5
          ⭕️ 6
the lowest common ancestor of the nodes 4 and 6 is the node 3.

EX:
6
4 2 3 1 7 6
1 7
      ⭕️       4
   ⭕️    ⭕️    2,7
⭕️   ⭕️ ⭕️     1,3,6

v1 = 1 and v2 = 7
LCA of 1 and 7 is 4, the root in this case.
Return a pointer to the node.
# class Node:
#       def __init__(self,info): 
#           self.info = info  
#           self.left = None  
#           self.right = None 
#        // this is a node of the tree , which contains info as data, left , right

def lca(root, v1, v2):
# 3 cases and recursion
# 1. if root == either v1, or v2; or between v1, or v2
    if root.info >= min(v1,v2) and root.info <= max(v1,v2):
        return root
# 2. if v1, v2 < root 
    if v1 < root.info and v2 < root.info:
        return lca(root.left, v1, v2)
# move to the left
# call lca with root.left
# 3. if v1, v2 > root  
    if v1 > root.info and v2 > root.info:
        return lca(root.right, v1, v2)
# move to the right
# call lca with root.right
RT complexity: balanced BST- O(log(n)), one side - O(n)
Space complexity:O(n),(needs extra stack or memory for recursion)

def lca_iterative(root, v1, v2):
    curr = root
    while curr is not None:
        if curr.info >= min(v1,v2) and curr.info <= max(v1,v2):
            return curr
        if v1 < curr.info and v2 < curr.info:
            curr = curr.left
        if v1 > curr.info and v2 > curr.info:
            curr = curr.right

RT complexity: balanced BST- O(log(n)), one side - O(n)
Space complexity:O(1)
        
            



