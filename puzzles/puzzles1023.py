Write a function that receives as input the head node of a linked list and an integer k. 
Your function should remove the kth node from the end of the linked list and return the head node of the updated list.

For example, if we have the following linked list: 
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null

The head node would refer to the node (20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node (14).

After the function executes, the state of the linked list should be:
(20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null

If k is longer than the length of the linked list, the linked list should not be changed.

Can you implement a solution that performs a single pass through the linked list and doesn't use any extra space?
2 pointers curr & prevK, curr = head, currK = None, prev = None, counter i = 0, k = 4, advance current and increment i until k = 4, 
advance prev and currK, then remove currK node from the list when it reaches the end of the list.

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
    while current: # RT Complexity: O(n-k)
        # if head is the first node
        if i == 0:
            head = current.next
            break
        # node is found, previous node points to current/next node
        if j == i:
            previous.next = current.next
            break
        # if node is not found, the pointer/reference moves on to the next node
        else:
            previous = current
            current = current.next
            j += 1
            
    return head

Follow up improvement: O(n) + O(n-k) = O(2n-k) = O(n)
Time complexity is O(n). That is, perform deletion in one pass.
And, space complexity is O(1). That is, no other data structures are used.

# ✅  What does Big O notation mean?
# Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. 
# ... In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows.

# 🆎  What is Big O complexity?
# Big O notation is used in Computer Science to describe the performance or complexity of an algorithm. 
# Big O specifically describes the worst-case scenario, and can be used to describe the execution time required or 
# the space used (e.g. in memory or on disk) by an algorithm.

# 💙  What is difference between time complexity and space complexity?
# Time complexity of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the length of the input. 
# Similarly, Space complexity of an algorithm quantifies the amount of space or memory taken by an algorithm to run as a function of the length of the input. 
# ... Let each operation takes time.

# ⭐️  How can we reduce time complexity?
# To reduce time complexity you need to optimize your algorithm. It will most often come as a result of using proper data structure or algorithm. 
# So you will need to learn data structures and algorithms for being able to perform well. 

Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. 
If there is no such character, return '_'.
Example
For s = "abacabad", the output should be
first_not_repeating_character(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
first_not_repeating_character(s) = '_'.
d = {
    'a': [8, 0],
    'b': [4, 1],
    'c': [2, 3]
}

def first_not_repeating_character(s):
    d = {}
    for i, l in enumerate(s):
        if l not in d:
            d[l] = [1, i]
        else:
            d[l][0] += 1
    best_index = len(s)  # 8 for "abacabad"
    best_letter = '_'
    for k, v in d.items():
        if d[k][0] == 1: # if count = 1
            if d[k][1] < best_index:
                best_index = d[k][1]
                best_letter = k
                
    return best_letter
    # Time complexity: O(n)
    # Space complexity: O(n)

# "abacabad"
# "abacabaabacaba"
# 'bcb'
# "abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"

Given a package with a weight limit limit and an array of integers items of where each integer represents the weight of an item, 
implement a function merge_packages that finds the first two items in the items array whose sum of weights equals the given weight limit limit.
Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.

Examples:
Input: items = [4, 6, 10, 15, 16], limit = 21
Output: [3, 1]
Explanation: The weight of the items at indices 3 and 1 sum up to the specified l

Input: items = [1, 3, 15, 5, 7, 16, 9, 5, 22], l = 10
Output: [4, 1] not [6,0]

def merge_packages(items, limit):
    candidates = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] + items[j] == limit:
                if i > j:
                    candidates.append([i, j])  # tuple
                else:
                    candidates.append([j, i])  # tuple
    best_candidate = []
    best_sum = 2 * len(items)  # 18 for [1, 3, 15, 5, 7, 16, 9, 5, 22], l = 10
    for i in range(len(candidates)):
        sum = candidates[i][0] + candidates[i][1]  # candidates[i][0] = i and candidates[i][1] = j, [4, 1] = 4+1 = 5, [6,0] = 6+0 = 6
        if sum < best_sum:  # 5 < 18
            best_sum = sum
            best_candidate = candidates[i]  # (i,j)
    return best_candidate
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)

def get_indices_of_item_weights(arr, limit):    
    for idx, i in enumerate(arr):
        diff = limit - i          
        if diff in arr[idx+1:]:   # constant lookup
            for idx2, j in enumerate(arr[idx+1:]):
                if j == diff:
                    return [idx+idx2+1, idx]
    return []

def get_indices_of_item_weights2(arr: list, limit: int) -> list:
    length = len(arr)
    hashmap = dict()

    if length <= 1:
        return []
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Traverse arr only once. For each weight w in arr compute its complement limit - w and check whether that
    # complement is hashed so far. If found the complement in the map, return a pair that consists of
    # w’s and limit - w’s indices. if not, hash w while using the weight as the hash key and its array index as the hash
    # value. Even if the same weight is found more than once it doesn’t matter because at the time of the lookup we only
    # need one item with that weight
    for i in range(length):
        weight = arr[i]
        if weight in hashmap:           # [1, 3, 15, 5, 7, 16, 9, 5, 22], l = 10
            value = hashmap[weight]  # d = {1: 0, 3: 1, 15: 2, 5: 3}, so complement to 3 is 7 => return [4, 1]
            return [i, value]
        diff = limit - weight
        hashmap[diff] = i
    return []

# items: [1, 2, 3],  limit: 1, Expected Output:[]
# items: [1, 3, 15, 5, 7, 16, 9, 5, 22],  limit: 10,  Expected Output:[4, 1] not [6, 0]

def remove_kth_from_end2(head, k):
    l = 0
    current = head
    while current:
        l += 1
        current = current.next
    i = l - k
    previous = None
    j = 0
    current = head
    while current:
        if i == 0:
            head = current.next
            break
        if j == i:
            previous.next = current.next
            break
        else:
            previous = current
            current = current.next
            j += 1

# FIND THE DUPLICATE NUMBER
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one duplicate number in nums, return this duplicate number.

Follow-ups:
How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1

#  converting integer to roman
def intToRoman(num):
    result = ''
    mapping = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
     50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
 
    while num != 0:
        for k, v in mapping.items():
            if num >= k:
                dividend = int(num/k)
                num %= k
                result += dividend*v
    return result

# find the end city
def path_end(paths):
  # make 2 sets
  starts, ends = set(), set()
  for path in paths:
    start, end = path
    starts.add(start)
    ends.add(end)

  end_only = ends - starts
  return end_only
print(path_end([["B","C"]]))
# [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]] -> "Sao Paulo"
# [["B","C"],["D","B"],["C","A"]] -> "A"

#merge two arrays of nums without zeroes in sorted
def merge(nums1, nums2):
  not_zero = len(nums1) - len(nums2)
  # print(not_zero)
  del nums1[not_zero:]
  for num in nums2:
    nums1.append(num)

  nums1.sort()
merge2([1,2,3,0,0,0], [2,5,6])

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = 0
        pointer2 = 0
        lastZero = len(nums1) - len(nums2) -1
        while pointer2 < len(nums2) and pointer1 < len(nums1):
            a = nums1[pointer1]
            b = nums2[pointer2]
            if a == 0 and pointer1 > lastZero:
                nums1[pointer1] = b
                pointer1 += 1
                pointer2 += 1
            elif a <= b:
                pointer1 += 1
            elif a > b:
                c = a
                nums1[pointer1] = b
                nums2[pointer2] = c
                nums2 = sorted(nums2)
                pointer1 += 1

def int_sum(lst, s):
    rv = []
    d = {}
    for i in range(len(lst)):
        if s - d[i] not in d:
            rv.append([lst[i], s-lst[i]])
        else:
            d[l[i]] = True

    return rv
print(int_sum([3, 5, 2, -4, 8, 11], 7))