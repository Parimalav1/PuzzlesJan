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

# 🌟🌟 Integer to Roman 🌟🌟 
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Given an integer, convert it to a roman numeral.

# /**
#  * @param {number} num
#  * @return {string}
#  */
var intToRoman = function(num) {
    let changeableNum = num;
    let intToRoman = {
        1000: "M",
        500: "D",
        100: "C",
        50: "L",
        10: "X",
        5: "V",
        1: "I"
    }
    let roman = "";
    let keys = Object.keys(intToRoman);
    for (i = 0; i < keys.length; i++) {
        if (changeableNum.toString()[0] == "4") {
            roman += intToRoman[1 * (10 ** (changeableNum.toString().length - 1))] + intToRoman[5 * (10 ** (changeableNum.toString().length - 1))];
            changeableNum -= 4 * (10 ** (changeableNum.toString().length - 1));
        } else if (changeableNum.toString()[0] == "9") {
            roman += intToRoman[1 * (10 ** (changeableNum.toString().length - 1))] + intToRoman[10 * (10 ** (changeableNum.toString().length - 1))];
            changeableNum -= 9 * (10 ** (changeableNum.toString().length - 1));
        } else if (changeableNum - keys[keys.length - i - 1] >= 0) {
            changeableNum-=keys[keys.length - i - 1];
            roman+=intToRoman[keys[keys.length - i - 1]];
            i--;
        }
    }
    return roman;
};

class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        inv_d = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        romanDigits = [1000, 100, 10, 1]
        fiveDigits = [None, 'D', 'L', 'V']
        remainder = num
        i = 0
        rv = ""
        while remainder > 0:
            quotient = remainder // romanDigits[i]
            remainder = remainder % romanDigits[i]
            #print('i: ', i, 'q: ', quotient, 'remainder: ', remainder)
            if quotient <= 3:
                rv = rv + inv_d[romanDigits[i]] * quotient            
            elif quotient == 4:
                rv = rv + inv_d[romanDigits[i]] + fiveDigits[i]
            elif quotient == 5:
                rv = rv + fiveDigits[i]
            elif quotient >= 6 and quotient <= 8:
                rv = rv + fiveDigits[i] + inv_d[romanDigits[i]] * (quotient - 5)
            elif quotient == 9:
                rv = rv + inv_d[romanDigits[i]] + inv_d[romanDigits[i-1]]

            i += 1
            
        return rv


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