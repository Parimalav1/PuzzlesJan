Search in Rotated Sorted Array
You are given an integer array nums sorted in ascending order, and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
If target is found in the array return its index, otherwise, return -1.
 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4


# 2. Print out all of the strings in the following array in alphabetical order sorted by the middle letter of each string, 
# each on a separate line. If the word has an even number of letters, choose the later letter, 
# i.e. the one closer to the end of the string.
# ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
# 'Cha Cha'
# 'Paso Doble'
# 'Viennese Waltz'
# 'Waltz'
# 'Samba'
# 'Rumba'
# 'Tango'
# 'Foxtrot'
# 'Jive'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. 
# Run through the UPER problem solving framework while going through your thought process.

def sort_alphabet(lst):
#     for elem in lst:
#         letters = list(elem)
#         print(letters)
#         if len(elem) % 2 != 0:
#             if len(elem) >= 6:
#                 for i in range(len(letters)):
#                     middle_letter = len(letters) // 2
#             elif len(elem) < 6:
#                 for i in range(len(letters)):
#                     middle_letter = len(letters) // 2
            
#             print(letters[middle_letter])
#         else:
#             print(letters[middle_letter + 1])

#     print(sorted(lst[middle_letter]))


    a = sorted(lst, key=lambda item: item[len(item)//2])
    for elem in a:
        print(elem)


sort_alphabet(['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive'])

# """
# 1. Add up and print the sum of the all of the minimum elements of each inner array. 
# Each array may contain additional arrays nested arbitrarily deep, 
# in which case the minimum value for the nested array should be added to the total.

# [
#   [8, [4]], 
#   [[90, 91], -1, 3], 
#   [9, 62], 
#   [[-7, -1, [-56, [-6]]]], 
#   [201], 
#   [[76, 0], 18],
# ]
# The expected output for the above input is:

# 8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260
# You may use whatever programming language you'd like.

# Verbalize your thought process as much as possible before writing any code. 
# Run through the UPER problem solving framework while going through your thought process.

# """

# """
# 3. Given an object/dictionary with keys and values that consist of both strings and integers, 
# design an algorithm to calculate and return the sum of all of the numeric values.

# For example, given the following object/dictionary as input:

# {
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }

# Your algorithm should return 41, the sum of the values 23 and 18.

# You may use whatever programming language you'd like.

# Verbalize your thought process as much as possible before writing any code. 
# Run through the UPER problem solving framework while going through your thought process.

# """

def values_keys(dt):
    sum = 0
    y = list(dt.values())
    for i in range(len(y)):
        if type(y[i]) == int:
            sum += y[i]

    return sum


ob = {
    "cat": 10,
    "dog": 23,
    19: 18,
    90: "fish"
}

print(values_keys(ob))
# """
# 4. Given a hashmap where the keys are integers, print out all of the values of the hashmap in reverse order, 
# ordered by the keys.

# For example, given the following hashmap:

# {
#   14: "vs code",
#   3: "window",
#   9: "alloc",
#   26: "views",
#   4: "bottle",
#   15: "inbox",
#   79: "widescreen",
#   16: "coffee",
#   19: "tissue",
# }

# The expected output is:

# widescreen
# views
# tissue
# coffee
# inbox
# vs code
# alloc
# bottle
# window

# since "widescreen" has the largest integer key, "views" has the second largest, etc.

# You may use whatever programming language you'd like.

# Verbalize your thought process as much as possible before writing any code. 
# Run through the UPER problem solving framework while going through your thought process.

# """

def values_keys2(dt):
    # y = sorted(dt.keys(), reverse=True)
    for elem in sorted(dt.keys(), reverse=True):
    # x = dt.values()
    # for elem in y:
        print(dt[elem])


ob = {
    14: "vs code",
    3: "window",
    9: "alloc",
    26: "views",
    4: "bottle",
    15: "inbox",
    79: "widescreen",
    16: "coffee",
    19: "tissue"
}

values_keys2(ob)

# def addTwoHugeNumbers(a, b):
    
    
#     list_1 = list()
#     list_2 = list()
    
    
#     # traverse both llist
    
#     cur = a
    
#     while cur is not None:
        
#         to_string = f"{'0' * (4 - len(str(cur.value))) + str(cur.value) }" if len(str(cur.value)) < 4 else str(cur.value)
      
#         list_1.append(to_string)
       
#         cur = cur.next
        
#     cur = b
    
#     while cur is not None:
        
#         to_string = f"{'0' * (4 - len(str(cur.value))) + str(cur.value)}" if len(str(cur.value)) < 4 else str(cur.value)
        
#         list_2.append(to_string)

#         cur = cur.next
    
    
        
#     joined_1 = int("".join([num for num in list_1]))
#     joined_2 = int("".join([num for num in list_2]))
    
#     sum_of_ll = joined_1 + joined_2
    
#     # check if sum is 0
#     if sum_of_ll == 0:
        
#         node = ListNode(sum_of_ll)
        
#         return node
   
#     result = list()
     
#     while sum_of_ll > 0:
        
#         new_value = sum_of_ll % 10000
        
#         result.append(new_value)
        
#         sum_of_ll = sum_of_ll // 10000
    
  
    
    
#     # reconstruct linked list
#     reversed_result = result[::-1]
    
#     new_head = None
#     pointer = None
    
#     for num in reversed_result:
        
#         node = ListNode(num)
        
#         if new_head is None:
            
#             new_head = node
#             pointer = new_head
            
            
#         else:
            
#             pointer.next = node
#             pointer = pointer.next
            
            
#     return new_head

# You are given an integer array nums sorted in ascending order, and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# If target is found in the array return its index, otherwise, return -1.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
# Accepted
# 815,797
# Submissions
# 2,330,735

