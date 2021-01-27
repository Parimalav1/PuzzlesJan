# mutate array
def mutateArray(n, a):
  b = []
  for i in range(n):
    if  i == 0:
      c = a[i] + a[i + 1]
    elif i == (n-1):
      c = a[i - 1] + a[i]
    else:
      c = a[i - 1] + a[i] + a[i + 1]
    b.append(c)

  return b
print(mutateArray(5, [4,0,1,-2,3]))
[4,5,-1,2,1] 

# get the pattern k occurences
s = 'ababaaabbccaaababab'
words = ['ba', 'bc', 'ca', 'a']
def sequence_words2(sequence, words):
  rv = []
  for word in words:
    for i in (range(len(sequence)) // len(word)):
      word_ext = word * (1 + i)
      try:
        sequence.index(word_ext)
      except ValueError:
        rv.append(i)
        break
print(sequence_words(s, words)) 

#valid parentheses
def validParantheses(s):
  openParan = ['(', '[', '{']
  closeParan = [')', ']', '}']
  backwards = []
  countf = 0
  countb = 0
  for i in range(len(s)):
    if s[i] in openParan:
      for x in range(len(openParan)):
        if openParan[x] == s[i]:
          backwards.insert(0, closeParan[x])
          countf += 1
          break
    elif s[i] in closeParan:
      for x in range(len(closeParan)):
        if len(backwards) >= 1:
          if closeParan[x] == backwards[0]:
            backwards.remove(backwards[0])
            countb += 1
            break
          else:
            return False
        else:
          return False
  if countf == countb:
    return True
  else:
    return False
  
print(validParantheses(''))

#duplicates- True/false
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
def duplicates(lst):
  for i in range(len(lst)):
    for j in range(i+1, len(lst)):
      if lst[i] == lst[j]:
        return True
  return False

print('duplicates:', duplicates([1,1,1,3,3,4,3,2,4,2]))
print('duplicates:', duplicates([1,2,3,4]))

def duplicates2(lst):
  d = {}
  boolean = False
  for elem in lst:
    if elem not in d:
      d[elem] = 1
    else:
      d[elem] += 1
  for key in d:
    if d[key] >= 2:
      boolean = True

  if boolean:
    return True, d
  return False, d
print(duplicates2([1, 2, 3, 4, 5, 6]))

def duplicate_num(lst):
    d = {}
    for n in lst:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    for k, v in d.items():
        if d[k] != 1:
            return k

#to find prefixes and shortest string
def shortestStr(lst):
  shortestStr = None
  prefix = '';
  for elem in lst:
    if shortestStr == None or len(elem) < len(shortestStr):
      shortestStr = elem
  for char in shortestStr:
    if len(prefix) != 2:
      prefix += char
  
  return prefix, shortestStr

print(shortestStr(['alpha', 'abc', 'a']))

# RECURSIVE COUNT
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    if len(word) < 2:
        return 0

    if word[0:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])


You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
 

Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of:
 "London" -> "New York" -> "Lima" -> "Sao Paulo".

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








