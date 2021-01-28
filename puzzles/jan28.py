# 🌟🌟  Roman to Integer 🌟🌟 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "IV"
# Output: 4

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        r2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        lastDigit = 0

        for c in s:
            num += r2i[c]
            if lastDigit < r2i[c]:
                num -= 2 * lastDigit
            lastDigit = r2i[c]

        return num

# 🌟🌟 Search Insert Position 🌟🌟 
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # iterate thru list
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        
        return len(nums)