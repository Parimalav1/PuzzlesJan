#🌟🌟 Reverse Integer: REVERSE 🌟🌟
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
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


             

