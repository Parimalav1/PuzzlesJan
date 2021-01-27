You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2

# If the amount is 0, return 0
# iterate and get the max/highest no in the list
# add the no to amount and check if the diff is in the list 
# keep a count of the steps/coins required to make amount and return the no of coins else return -1

class Solution:
    def coinChange(self, in_coins: List[int], amount: int) -> int:
        coins = sorted(in_coins)
        changes = []
        if amount == 0:
            return 0
        for i in range(len(coins) - 1, -1, -1):
            if coins[i] > amount:
                continue
            if coins[i] == amount:
                return 1
            smallerChange = self.coinChange(coins, amount - coins[i])
            if smallerChange == -1:
                continue
            changes.append(1 + smallerChange)
        if len(changes) == 0:
            return -1
        
        return min(changes)

from typing import List, Dict
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        my_queue = deque([(amount, 0)])
        already_checked = set([])
        while my_queue:
            amount, level = my_queue.popleft()
            if amount == 0:
                return level
            for coin in coins:
                diff = amount - coin
                if diff >= 0 and diff not in already_checked:
                    already_checked.add(diff)
                    my_queue.append((diff, level + 1))
        return -1

# Time/Space complexity of the algorithm
# It is O(n*m) time with n :coins and m: amount
# and  O(n) space as the set is being created  


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
  

class LinkedList:
    def __init__(self, head, tail):
        self.head = None
        self.tail = None
        self.length = 0

    def add_tail(self, value):
        # check if there is a tail:
        # if no tail,
        if not self.tail:
            # create a new node as the new tail.
            new_tail = Node(value, None)
            # set head and tail to new node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail, 
        else:
            new_tail = Node(value, None)
            # set the value to the current tail, next to None
            curr_tail = self.tail
            # set current tail pointer to new tail
            curr_tail.next = new_tail
            # set the tail to the new tail
            self.tail = new_tail
            self.length += 1

    def remove_head(self):
        # check if there is a head.
        # if no head, remove none
        current_head = self.head
        if current_head is None:
            return 0
        # If there is a head, check the length of the ll
        # if the length of ll == 1, remove the current single node
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value
        # if the length of ll > 1, remove head, next node becomes the head/current node, 
        # point head.next to next node
        else:
            current_head = self.head
            self.head = current_head.next
            self.length -= 1
            return current_head.value

    def remove_tail(self):
        current_tail = self.tail
        if not current_tail:
            return None
        if self.head == self.tail:
            current_tail = self.tail
            self.length -= 1
            return current_tail.value
                              ⭕️     
            ⭕️ ➡➡⭕️ ➡➡⭕️ ➡➡⭕️ ↗  ↘➡➡⭕️
        else:
            current_tail = self.tail
            self.tail = current_tail.prev
            self.tail -= 1
            return current_tail.value



# 🌟🌟 COUNT PRIMES 🌟🌟
# Count the number of prime numbers less than a non-negative number, n.
# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:
# Input: n = 0 or 1
# Output: 0

# write another function to check if the no is a prime no
# if no is <= 1, return 0
# iterate and check if the no is divisible by a no in the range, if there is a remainder

class Solution():
    def countPrimes(self, n):
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self, n):
        if n <= 1:
            return 0
        for no in range(2,n):
            if n % no == 0:
                return False
        
        return True

sol = Solution()
print(sol.countPrimes(5))
Complexity:
time: O(n * n)(function in a function)
space: O(1)

# 🌟🌟 GROUP ANAGRAMS 🌟🌟
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = ["a"]
# Output: [["a"]]

from typing import List
letter_map = {
    'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,'h':19,'i':23,
    'j':29,'k':31,'l':37,'m':41,'n':43,'o':47,'p':53,'q':59,'r':61,
    's':67,'t':71,'u':73,'v':79,'w':83,'x':89,'y':97,'z':101
}
class Solution:
    def groupAnagramsSorted(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]
        return list(anagram_map.values())
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sum = 1
            for letter in word:
                sum *= letter_map[letter]
            anagram_map[sum].append(word)
        return list(anagram_map.values())

# 🌟🌟 Champagne Tower 🌟🌟
# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.
# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  
# When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)
# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, 
# those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

# Example 1:
# Input: poured = 1, query_row = 1, query_glass = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). 
# There will be no excess liquid so all the glasses under the top glass will remain empty.

# Example 2:
# Input: poured = 2, query_row = 1, query_glass = 1
# Output: 0.50000
# Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. 
# The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

# Example 3:
# Input: poured = 100000009, query_row = 33, query_glass = 17
# Output: 1.00000

from functools import reduce
from typing import List

def overflow(top_row: List[float], bottom_row: List[float]) -> List[float]:
    # March through the glasses in the top row
    # I'll need to figure out how much goes into the glasses below it in the bottom
    for glass_position, amount in enumerate(top_row):
        overflow = max(0, (amount - 1)/2)
        bottom_row[glass_position] += overflow
        bottom_row[glass_position + 1] += overflow
    return bottom_row
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        champagne_tower = [[0 for glass in range(row)] for row in range(1, query_row + 2)]
        champagne_tower[0][0] = poured
        final_row = reduce(overflow, champagne_tower)
        return min(1, final_row[query_glass])
class SolutionWithoutReduce:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_row = [poured]
        for row in range(query_row):
            new_row = [0 for cup in range(row + 2)]
            current_row = overflow(current_row, new_row)
        return min(1, current_row[query_glass])

# 🌟🌟 MARK AND TOYS 🌟🌟
# Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices.
# Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.
# **  Note Each toy can be purchased only once. **

# Example1:
# Input: prices: [1, 2, 3, 4]; k = 7
# Output: 3
# He can buy items that cost [1, 2, 3] for 6, or [3, 4] for 7 units. The maximum is 3 items.

# Example2:
# Input: prices: [1 12 5 111 200 1000 10]; k = 50
# Output: 4
# Explanation:
# He can buy only 4 toys at most. These toys have the following prices: 1, 12, 5, 10.


def maximumToys(prices, k):
    basketSum = 0
    basketSize = 0
    pricesSorted = sorted(prices)
    for i in range(len(pricesSorted)):
        if basketSum + pricesSorted[i] < k:
            basketSum += pricesSorted[i]
            basketSize += 1
        else:
            break
        
    return basketSize

# sort the prices so that smallest price is first
# iterate thru prices- keep substracting the toy price
# increment the counter for a toy bought
# Once we are out of money, we're done
# return the counter

def maximumToys2(prices, k):
    pricesSorted = sorted(prices) #nlogn
    #prices.sort()
    count = 0
    for price in prices:
        if k >= price:
            k -= price
            count += 1
        else:
          break
    return count

# 🌟🌟 COMPARATORS 🌟🌟
# Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields:
# name : a string.
# score : an integer.
# Given an array of  Player objects, write a comparator that sorts them in order of decreasing score. If  or more players have the same score, sort those players alphabetically ascending by name. 
# To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method. 
# In short, when sorting in ascending order, a comparator function returns -1 if a<b , 0 if a=b, and  1 if a>b.

# Sample Input: 5
# amy 100
# david 100
# heraldo 50
# aakansha 75
# aleksa 150

# Sample Output:
# aleksa 150
# amy 100
# david 100
# aakansha 75
# heraldo 50

# Explanation:
# The players are first sorted descending by score, then ascending by name.


from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return ""
    def comparator(a, b):
        if a.score < b.score:
          return -1
        elif a.score >  b.score:
          return 1
        
        if a.name < b.name:
          return 1
        elif a.name > b.name:
          return -1

        return 0

# 🌟🌟 PAIRS 🌟🌟
# You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.
# For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition:[2,1] ,[3,2] , and [4,3].

# Function Description:
# Complete the pairs function below. It must return an integer representing the number of element pairs having the required difference.
# pairs has the following parameter(s):
# k: an integer, the target difference
# arr: an array of integers

# Sample Input:
# 5 2  
# 1 5 3 4 2 

# Sample Output: 3
# Explanation:
# There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1].

def pairs2(k, arr):
    count = 0
    d = set(arr) 
    print(d)
    for num in arr:
        if num + k in d:
            count += 1

    return count
print(pairs2(2, [1,5,3,4,2]))

complexity:
time: O(n)
space: O(n)

def pair(k, arr):
    count = 0
    arr.sort()
    for num in arr:
        search_num = num - k
        is_found = binary_search(arr, search_num)
        if is_found:
            count += 1

    return count
    
    def binary_search(arr, target):
        if len(arr) == 0:
            return False
        midpoint = len(arr) // 2
        if arr[midpoint] < target:
            return binary_search(arr[midpoint + 1:], target)
        elif arr[midpoint] > target:
            return binary_search(arr[:midpoint], target)
        else:
          return True

print(pair(2, [1,5,3,4,2]))

complexity:
time: nlog(n)
space: O(1)

Recursive function:
complexity:
time: n!(n factorial)
space: O(n)( like stacking)

# 🌟🌟 Recursive Digit Sum 🌟🌟 RECURRENCE RELATION
# We define super digit of an integer  using the following rules:
# Given an integer, we need to find the super digit of the integer.
# If x has only 1 digit, then its super digit is x.
# Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
# For example, the super digit of 9875 will be calculated as:

# Example1: n ='9875', k = 4
# Output: 8
# superDigit(p) = superDigit(9875987598759875)
#                   5+7+8+9+5+7+8+9+5+7+8+9+5+7+8+9 = 116
#     superDigit(p) = superDigit(116)
#                   1+1+6 = 8
#     superDigit(p) = superDigit(8)
# All of the digits of p sum to 116. The digits of 116 sum to 8. 8 is only one digit, so it is the super digit.

# Example2: n ='148', k = 3, so P= 148148148
# Output: 3
# super_digit(P) = super_digit(148148148) 
#                = super_digit(1+4+8+1+4+8+1+4+8)
#                = super_digit(39)
#                = super_digit(3+9)
#                = super_digit(12)
#                = super_digit(1+2)
#                = super_digit(3)
#                = 3.

# Example3: n ='123', k = 3, P= 123123123
# Output: 9
# super_digit(P) = super_digit(123123123) 
#                = super_digit(1+2+3+1+2+3+1+2+3)
#                = super_digit(18)
#                = super_digit(1+8)
#                = super_digit(9)
#                = 9

# concatenate (string n) k times to make P
# convert string to integer

def superDigit(n, k):
    # lst = list(map(int, n)) # number to list of integers
  super_num = sum_digits(n)
  product = int(super_num) * k
  return super_digits(str(product))

  def sum_digits(n):
      total = 0
      for ch in n:
          if len(n) == 1:
              return n

          total += int(ch)

      return total

# complexity:
# time: log(n)

🌟🌟 Reverse Integer: REVERSE 🌟🌟
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Sample Input: 123 
# Sample Output: 321

# Sample Input: 1200 
# Sample Output: 21

# Sample Input: -1897 
# Sample Output: -7981

# Sample Input: 21474836473 (if it is > 2147483647, 32 bit integer) 
# Sample Output: 0

def reverse3(x):
  if x > 0:
    num = str(x)[0]
  elif x < 0:
    num = '-'
  else:
    return 0
  for i in range(0, len(str(x)) -1):
    num = num[0:-1] + str(x)[len(str(x)) - i -1] + num[-1]
  if int(num) > 2147483647 or int(num) < -2147483647:
    return 0
  return int(num)

print(reverse3(-128))

# Palindrome Number
# Given an integer x, return true if x is palindrome integer.

# Example 1:
# Input: x = 121
# Output: true

# Example 3:
# Input: x = 0
# Output: true

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # y = str(x)
        # int to str
        # iterate thru ch in str(s1)
        # iterate thru last idx to 0 in str(s2), if s2(elem) == s1(ch), return true else false
        # if x <= 0:
        #     return False
        # for i in range(len(y)):
        #     for j in range(len(y) -1 -1):
        #         if y[i] == y[j]:
        #             return True
                    
        # return False
        if x < 0:
            return False
        
        return str(x) == str(x)[::-1]

# Repeated DNA Sequences - LeetCode
# All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". 
# When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

# Analysis:
# This problem is straightforward (no need to think about KMP algorithm), only dictionary (hashmap) can pass the OJ.
# Since there are many restrictions in this problem, it becomes much easier. E.g., only four chars are occurred in the sequence (A,T,C,and G), only length-10 substr is needed.
# So the algorithm goes as follows:
# 1. Search from the start of the string, get every substr with length 10.
# 2. Construct and look up a hashmap, add 1 to the value.
# 3. After the whole search, check every entry in the hashmap, if the value is greater than 1, output.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        res = []
        for i in range(len(s)):
            subst = s[i : i + 10]
            if subst not in d: # d[subst] = d.get(subst, 0) + 1
                d[subst] = 1   #
            else:              #
                d[subst] += 1  #
        for k, v in d.items():
            if v>1:
                res.append(k)

        return res

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        winners = set([])
        if len(s) < 10:
            return []
        subsequences = set([])
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub in subsequences:
                winners.add(sub)
            subsequences.add(sub)
        return [sub for sub in winners]


             

