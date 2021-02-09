# 🌟🌟 Codewars - Replace With Alphabet Position 🌟🌟
# Level: 6kyu
'''
Problem Description: Welcome. In this kata you are required to, given a string, replace every letter 
with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return 
it. a being 1, b being 2, etc. As an example:
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (As a string.)
'''
def alphabet_position(text):
	  ans = ''
	  inp = list('abcdefghijklmnopqrstuvwxyz')
	  for ch in text:
		  if ch.isalpha():
			  ans += str(inp.index(ch.lower()) + 1) + ' '
	  return ans[0:len(ans)-1]

print(alphabet_position("The sunset sets at twelve o' clock."))

# JavaScript
const alphaPosition = str => [...str]
  .filter(letter => letter.toLowerCase().charCodeAt(0) - 96 > 0)
  .map(letter => letter.toLowerCase().charCodeAt(0) - 96)
  .reduce((s, pos) => s += `${pos} `, '')
  .trim();

# 🌟🌟 Truck Tour -- hackerrank 🌟🌟 
# Suppose there is a circle. There are  petrol pumps on that circle. Petrol pumps are numbered  to  (both inclusive). You have two pieces of information corresponding to each of the petrol pump: 
# (1) the amount of petrol that particular petrol pump will give, and (2) the distance from that petrol pump to the next petrol pump. Initially, you have a tank of infinite capacity carrying no petrol. 
# You can start the tour at any of the petrol pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps. 
# The truck will move one kilometer for each litre of the petrol.
# 🌟🌟  CIRCULAR QUEUE or RING BUFFER 🌟🌟 

# Input Format, Sample Input 1 5
#                            10 3
#                            3 4
# The first line will contain the value of N.
# The next N lines will contain a pair of integers each, i.e. the amount of petrol that petrol pump will give and the distance between that petrol pump and the next petrol pump.

# Output Format, Sample Output: 1
# An integer which will be the smallest index of the petrol pump from which we can start the tour.

def truckTour(petrolpumps):
    # start is the starting index of petrol pump
    # current is the index of petrol pump where the vehicle is
    # petrol is litres of petrol 
    # petrolpumps is no of petrol pumps
    start = 0
    current = 0
    petrol = 0
    while start <= len(petrolpumps):
        petrol += petrolpumps[current][0] #amount of petrol intially
        petrol -= petrolpumps[current][1] #amount of petrol after travelling for distance- current[1]
        if petrol < 0:              # when there is no petrol
            start = current + 1 #amount of petrol<0, then try from next index
            current = start
            petrol = 0
            continue
        
        current += 1 #amount of petrol<0, then start from next index
        if current >= len(petrolpumps):# if the vehicle travelled thru all pumps, then # # there is nothing to travel, return current = 0
            current = 0
        if current == start:# when the vehicle circled/travelled thru all pumps, return # starting index
            return start
        
    return None

# 🌟🌟  Two Strings 🌟🌟 
# Given two strings, determine if they share a common substring. A substring may be as small as one character.
# Returns
# string: either YES or NO

# Sample Input: Sample Output: YES(o, l)
# hello
# world
# Sample Output: NO
# hi
# world

def twoStrings(s1, s2):
    # create a dict
    # iterate thru elems in s1, and if elem not in dict, count as 1
    # if s1[value] that is key in s2, return true else false
		set2 = set()   # Hashset 👈 👈 👈  {"a","b","c"}
    for elem in s2:
        set2.add(elem)
    for ke in s1:
        if ke in set2:
            return "YES"
    return "NO"
# time complexity: O(m + n)  👈 👈
def twoStrings(s1, s2):
    d = {}       # Hashmap  👈 👈 👈   {"a": True,"b": True,"c": True}
    for elem in s1:
        if elem not in d:
            d[elem] = True
    for ke in d.keys():
        if ke in s2:
            return "YES"
    return "NO"
# Hashset- it's a function that stores either keys or values not both.
# Hashmap- it's a hashing function mapping keys to values(buckets) for lookup or search, it stores key and value both.
# Time complexity of 'in' operator or keyword in Python  👈 👈 👈
# For a list: O(n)
# set/dict - O(1) , worst case: O(n)
def singleCommonSubstring(s1, s2):
		set2 = set()   # Hashset 👈 👈 👈
		set3 = set()
    for elem in s2:
        set2.add(elem)
    for ke in s1:
        if ke in set2:
					 set3.add(ke)
				return set3

def commonSubstrings(s1, s2):	
		common = set()
		subst1 = findSubstrings(s1)
		subst2 = findSubstrings(s2)
		for sub in subst1:
				if sub in subst2:
						common.add(sub)

		return common
		# find substrings in s1
def findSubstrings(s):
		subs = set()
		for i in range(len(s)):
				for j in range(i+1, len(s)+1):
						subs.add(s[i:j])

		return subs

commonSubstrings("abcd", "abcef")

🌟🌟 Frequency Queries 🌟🌟 
You are given q queries. Each query is of the form two integers described below:
- 1 x : Insert x in your data structure.
- 2 y : Delete one occurence of y from your data structure, if present.
- 3 z: Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.
The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation, and
queries[i][1] contains the data element. For example, you are given array . 
queries = [(1,1),(2,2),(3,2),(1,1),(1,1),(2,1) ],(3,2)]. The results of each operation are:
Operation   Array   Output:[0,1]
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1

Input Format
The first line contains of an integer q, the number of queries.
Each of the next q lines contains two integers denoting the 2-d array queries.

Output Format
Return an integer array consisting of all the outputs of queries of type 3.

Sample Input 0, Sample Output 0: [0,1]                           
8                                
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2
Sample Input 2, Sample Output 2: [0,1,1]
10                               
1 3                              
2 3
3 2
1 4
1 5
1 5
1 4
3 2
2 4
3 2

from collections import Counter

def freqQuery(queries):
		answer = [] #  O(n)   space complex: O(n) + O(n)+O(n) = O(3n) -> O(n)
		valueFreq = Counter() # counter is a dict - O(n); time: O(1)
		freqCount = Counter() # counter is a dict - O(n); time: O(1)
		for query in queries: # O(n)
				if query[0] == 1:
						if valueFreq[query[1]] > 0: # O(1)
								freqCount[valueFreq[query[1]]] -= 1
						valueFreq[query[1]] += 1
						freqCount[valueFreq[query[1]]] += 1
				elif query[0] == 2:
						if valueFreq[query[1]] > 0: 
								freqCount[valueFreq[query[1]]] -= 1
								valueFreq[query[1]] -= 1
								freqCount[valueFreq[query[1]]] += 1
				else:
						if freqCount[query[1]] > 0:
								answer.append(1)
						else:
							answer.append(0)
		return answer
# time complexity: O(n) + O(1)  -> O(n)  
# space complexity: O(n)

🌟🌟 Maximum Product Subarray - LeetCode 🌟🌟

from typing import List
from functools import reduce

def array_multiplyer(nums: List[int]) -> int:
    return reduce(lambda x, y: x*y, nums)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # recursively compute the solution to smaller and smaller subsets
        print(f"solving: {nums}")
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return None
        max_result = max(
            nums[0],
            nums[-1],
            self.maxProduct(nums[1:]),
            self.maxProduct(nums[0:-1]),
            array_multiplyer(nums)
        )
        print(f"solution to {nums} is {max_result}")
        return max_result
class CachedSolution:
    def __init__(self):
        self.cache = {}
    def maxProduct(self, nums: List[int]) -> int:
        self.nums = nums
        return self.maxProductRecurse(0, len(nums) - 1)
    def maxProductRecurse(self, left: int, right: int) -> int:
        if (left, right) in self.cache:
            return self.cache[(left, right)]
        if left == right:
            return self.nums[left]
        if left > right:
            return None
        max_result = max(
            self.nums[left],
            self.nums[right],
            self.maxProductRecurse(left, right - 1),
            self.maxProductRecurse(left + 1, right),
            array_multiplyer(self.nums[left: right + 1])
        )
        self.cache[(left, right)] = max_result
        return max_result
class CleverSolution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        global_max = max(nums)
        current_max, current_min = 1, 1
        for num in nums:
            # want to find the current max and current min of the 
            # step that I'm on
            mx = num * current_max
            mn = num * current_min
            current_max = max(mx, mn, num)
            current_min = min(mx, mn, num)
            global_max = max(global_max, current_max)
        return global_max
