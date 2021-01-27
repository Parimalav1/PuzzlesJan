'''
Input: an integer
Returns: an integer
'''

def eating_cookies_v1(n):
    # print(n)
    # Your code here
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return eating_cookies_v1(n-1) + eating_cookies_v1(n-2) + eating_cookies_v1(n-3)

def eating_cookies_v2(n):
    # print(n)
    # Your code here
    if n < 0:
        return 0
    elif n == 0:
        return 1
    
    return eating_cookies_v2(n-1) + eating_cookies_v2(n-2) + eating_cookies_v2(n-3)

# print('eating_cookies_v1(5)', eating_cookies_v1(5))
# print('eating_cookies_v2(5)', eating_cookies_v2(5))
# e(1) = e(0) + e(-1) + e(-2)
# e(2) = e(1) + e(0) + e(-1) = 2
# e(3) = e(2) + e(1) + e(0) = 4
# e(4) = e(3) + e(2) + e(1) = 4 + 2 + 1
# 1111, 112, 121, 112, 22, 13, 31

# e(5) = e(4) + e(3) + e(2)
#     = ( e(3) + e(2) + e(1) ) +

def eating_cookies(n, cache=None):
    # print(n)
    # Your code here
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i: 0 for i in range(n + 1)}
            cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]


# def eating_cookies_iterative(n):
#     value = 0
#     n

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


# Runtime complexilty
# O(3^n)
# with caching/memoization, it is O(n)-linear

Recursion: Davis' Staircase

Davis has a number of staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time. Being a very precocious child, 
he wonders how many ways there are to reach the top of the staircase. Given the respective heights for each of the  staircases in his house, 
find and print the number of ways he can climb each staircase.

For example, there is  staircase in the house that is  steps high. Davis can step on the following sequences of steps:
stepPerms has the following parameter(s):
n: an integer, the number of stairs 5 in the staircase 1.
1 1 1 1 1
1 1 1 2
1 1 2 1 
1 2 1 1
2 1 1 1
1 2 2
2 2 1
2 1 2
1 1 3
1 3 1
3 1 1
2 3
3 2
There are 13 possible ways he can take these 5 steps.

def stepPerms(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
   
    return  ways = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)  

def stepPerms1(n, cache=None):
    # print(n)
    # Your code here
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i: 0 for i in range(n + 1)}
            cache[n] = stepPerms(n - 1, cache) + stepPerms(n-2, cache) + stepPerms(n-3, cache)

    return cache[n]

def stepPerms2(n):
    memo = {}
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n+1):
        memo[i] = stepPerms[i-1] + stepPerms[i-2] + stepPerms[i-3]
    return memo[n]


memo = {0:1, 1:1, 2:2}
def stepPerms3(n):
    if n not in memo:
        memo[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)

    return memo[n]

# Runtime complexilty
# O(3^n)
# with caching/memoization, it is O(n)-linear, space complexity - O(n)
