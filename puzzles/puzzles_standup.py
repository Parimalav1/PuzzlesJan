
print(710077 % 7)  # gives value 7 - last num
print(710077 // 7)   # gives value 71007 - nums except last num

"""
Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, 
except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. 

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), 
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

Try solving it with "n" as string

"""



def count8(n):

	pass
	
	
	
print(count8(8))  # 1
print(count8(818))  # 2
print(count8(8818))  # 4
print(count8(88188))  # 6

def count7(n):
    if n < 10:
        if n == 7:
            return 1
        else:
            return 0
    if n % 10 == 7:
        return 1 + count7(n // 10)
    else:
        return count7(n//10)


print(count7(710077))
print(count7(710077))


def v_count7(n):
    if type(n) == int:
        str_n = str(n)
    else:
        str_n = n
        if len(str_n) == 1:
            if str_n[0] == '7':
                return 1
            else:
                return 0
    test = str_n[0]
    if test = '7':
        return 1 + count7(str_n[1:])
    else:
        return count7(str_n[1:])


print(v_count7(710077))
print(v_count7(710077))
print(v_count7(710077))


def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]


print(reverse('LAMBDA'))


def is_palindrome(str):
    # If the string is of length 0 or 1, it is a palindrome.
    if len(str) <= 1:
        return True
    # Otherwise, compare the first and last characters.
    if str[0] == str[-1]:
        # If the first and last characters are equal, strip those characters and check if the remaining characters are a palindrome.
        return is_palindrome(str[1:-1])
    return False


print(is_palindrome('LAMBDA'))

import time
@functools.lru_cache

def fibonacci_iterative(n):
    value = [0 for i in range(n +1)]
    value[0] = 0
    value[1] = 1
    for i in range(n + 1):
        value[i] = value[i-1] + value[i-2]
    return value[n]

    
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


# cache = {}  # keys: n(parameters), values: nth fibonacci number/ return value from the function
def fibonacci_cache(n, cache):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in cache:
        return cache[n]

    result = fibonacci_cache(n-1, cache) + fibonacci_cache(n-2, cache)
    cache[n] = result
    return result


for n in [15, 20, 25, 30]:
    start = time.time()
    fibonacci(n)
    end = time.time()
    print(f'Calculating fib w/o cache for n={n} took {end - start}: seconds)

    start = time.time()
    fibonacci_cache(n, {})
    end = time.time()
    print(f'Calculating fib with cache for n={n} took {end - start}: seconds)

    print('-----------')

