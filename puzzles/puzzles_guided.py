Once upon a time, in a kingdom far, far away, there lived a King Byteasar I. As a kind and wise ruler, he did everything in his (unlimited) power to make life for his subjects comfortable 
and pleasant. One cold evening a messenger arrived at the king's castle with the latest news: all kings in the Kingdoms Union had started enforcing traffic laws! In order to not lose his membership in the Union,
King Byteasar decided he must do the same within his kingdom. But what would the citizens think of it?

The king decided to start introducing the changes with something more or less simple: change all the roads in the kingdom from two-directional to one-directional (one-way). 
He personally prepared the roadRegister of the new roads, and now he needs to make sure that the road system is convenient and there will be no traffic jams, 
i.e. each city has the same number of incoming and outgoing roads. As the Hand of the King, you're the one who he has decreed must check his calculations.

Example
For
roadRegister = [[false, true,  false, false],
                [false, false, true,  false],
                [true,  false, false, true ],
                [false, false, true,  false]]
the output should be
newRoadSystem(roadRegister) = true.

The cities will be connected as follows:


Cities 0, 1 and 3 (0-based) have one incoming and one outgoing road, and city 2 has two incoming and two outgoing roads. Thus, the output should be true.

For
roadRegister = [[false, true,  false, false, false, false, false],
                [true,  false, false, false, false, false, false],
                [false, false, false, true,  false, false, false],
                [false, false, true,  false, false, false, false],
                [false, false, false, false, false, false, true ],
                [false, false, false, false, true,  false, false],
                [false, false, false, false, false, true,  false]]
the output should be
newRoadSystem(roadRegister) = true.

The cities will be connected as follows:


Each city has one incoming and one outgoing road.

For
roadRegister = [[false, true,  false],
                [false, false, false],
                [true,  false, false]]
the output should be
newRoadSystem(roadRegister) = false.

The cities will be connected as follows:


City 1 has one incoming and no outgoing roads, and city 2 has one outgoing and no incoming roads.


def newRoadSystem(roadRegister):
    # for each node/vertex, count incoming and outgoing edges,if there is a difference, return false else return true
    incoming = 0
    for row in roadRegister:  # RT complexity: O(n)
        if row[i]:  # getting single index in a row
            incoming += 1
    print(incoming)

    outgoing = 0
    for i in range(len(roadRegister)):  # RT complexity: O(n) * O(n) = O(n ** 2)
        for v in roadRegister[i]:
            if v:
                outgoing += 1
        print(outgoing)
        
    if incoming != outgoing:
        return False
    return True                  # RT complexity: O(n ** 2)


def newRoadSystem2(roadRegister):
    for x, y in zip(map(sum, roadRegister)):
        map(sum, zip(*roadRegister)):
            if x != y:
                return False
            return True



Once upon a time, in a kingdom far, far away, there lived a King Byteasar II. There was nothing special about him or his kingdom. As a mediocre ruler, 
he preferred hunting and feasting over doing anything about his kingdom's prosperity.

Luckily, his adviser, the wise magician Bitlin, worked for the kingdom's welfare day and night. However, since there was no one to advise him, 
he completely forgot about one important thing: the roads! Over the years most of the two-way roads built by Byteasar's predecessors were forgotten and no longer traversable. 
Only a few roads can still be used.

Bitlin wanted each pair of cities to be connected, but couldn't find a way to figure out which roads are missing. Desperate, he turned to his magic crystal ball for help. 
The crystal showed him a programmer from the distant future: you! Now you're the only one who can save the kingdom. Given the existing roads and the number of cities in the kingdom, 
you should use the most modern technologies and find out which roads should be built again to connect each pair of cities. Since the crystal ball is quite old and meticulous, 
it will only transfer the information if it is sorted properly.
The roads to be built should be returned in an array sorted lexicographically, with each road stored as [cityi, cityj], where cityi < cityj.
Example
For cities = 4 and roads = [[0, 1], [1, 2], [2, 0]],
the output should be
roadsBuilding(cities, roads) = [[0, 3], [1, 3], [2, 3]].

See the image below: the existing roads are colored black, and the ones to be built are colored red.


def roadsBuilding(cities, roads):
    existing = set()
    to_build = []
    
    for s, d in roads:
        if s > d:
            s,d = d,s  # swap
            
        t = (s, d)
        
        existing.add(t)

    for i in range(cities):
        for j in range(i+1, cities):
            if (i, j) not in existing:
                to_build.append([i, j])

    return to_build

# get steps
def get_num(num): # 14
  steps = 0 
  while num > 0:
    if num % 2 == 0:
      num = num / 2
      # steps += 1
    else:
      num = num - 1
      # steps += 1
    steps += 1

  return steps
print(get_num(14))

def letter_count(s):
    d = {}

    for c in s:
        if not c.isalpha():
            continue

        """
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
        """
        if c not in d:
            d[c] = 0

        d[c] += 1

    return d

print(letter_count("abb baaaa^&* ccaddadada"))

def pod(total, podcasts):
    podcast_len = {}

    for p in podcasts:
        podcast_len[p] = True

    """
    # Set version equivalent to dict, above
    podcast_len = set()

    for p in podcasts:
        podcast_len.add(p)
    """

    for p0 in podcasts:
        other_podcast_len = total - p0
        # is there a podcast of total - p0 minutes?
        if other_podcast_len in podcast_len:
            return True

    return False


"""
total == 60
p0 == 27
p1 == 60 - 27 == total - p0 == 33
"""


import hashlib
import random

def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff

def how_many_before_collision(buckets, loops):
    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = random.random()

            index = hash_function(random_key) % buckets

            if index not in tried:
                tried.add(index)
                tries += 1

            else:
                break

        print(f"{buckets} buckets, {tries} hashes before collision, ({tries / buckets * 100}% full)")

how_many_before_collision(32768, 10) 

# cache/memoization
# 0 1 1 2 3 5 8 13 21 34 55 ...
#
# fib(0): 0
# fib(1): 1
# fib(n): fib(n-1) + fib(n-2)
#
cache = {}

def fib(n):
	if n <= 1: return n

	if n not in cache:
		cache[n] = fib(n-1) + fib(n-2)

	return cache[n]

for i in range(100):
	print(f'{i:3} {fib(i)}')


"""
def foo(a, x, b):

	cache[(a,x,b)] = ...
"""
# eating cookies
# what is the runtime of this implementation?
# O(3^n) 
# Using caching/memoization, the runtime is now O(n)
def eating_cookies(n, cache=None):
    # what are our base cases?     
    if n < 0:
        return 0 
    # this represents there being a number of cookies where we can just take
    # that many cookies
    elif n == 0:
        return 1 
    # check the cache to see if the answer is stored in there 
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            # init an empty cache
            cache = {i: 0 for i in range(n+1)}
        # store answers in our cache 
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]        

print(eating_cookies(100))


# can binary search help us in this case?
# binary search requires us to know our target
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

# input: array of numbers where there is one number that 
# is not a duplicate; every other number has a duplicate 
# O(n^2)
#def single_number(arr):
#    for num in arr: # O(n)
#        if arr.count(num) == 1: # O(n)
#            return num
#

# O(n)
def single_number(arr):
    # sets are a closely-related cousin to dicts 
    # they don't associate values with keys 
    # they're useful for when you need the uniqueness
    # property of dicts
    s = set()
    # s = []

    for num in arr: # O(n)
        if num in s: # O(1)
            s.remove(num) # O(1)
        else:
            s.add(num) # O(1)

    # at this point, the only element in the set 
    # is our odd-element-out
#    return list(s)[0] # O(1)
    return s.pop()