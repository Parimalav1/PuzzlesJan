<!-- # with classes


class Parent:

    def __init__(self, name, child=None):

        self.name = name
        self.child = child

    def __str__(self):

        if self.child is not None:

            return f"My name is {self.name}. I'm the parent of {self.child}"

        else:

            return f"My name is {self.name}. I don't have a child"


class Child:

    def __init__(self, name, parent=None, age=0):

        self.name = name
        self.parent = parent
        self.age = age

    def __str__(self):

        return f"My name is {self.name}. My parent is {self.parent.name}"


parents = ["Ted", "Mosby", "Paul", "Nana", "Lira", "Nancy"]
children = [

    {
        "name": "Ben",
        "age": "12"
    },
    {
        "name": "Julie",
        "age": "35"
    },
    {
        "name": "Bart",
        "age": "1"
    },
    {
        "name": "Lisa",
        "age": "10"
    },
    {
        "name": "Mark",
        "age": "20"
    },
    {
        "name": "Katie",
        "age": "2"
    }

]


# Create a new parent for each element in parents list


parent_class = []

for p in parent_class:

    print(p)

"""
Should print:

My name is Ted. I don't have a child
My name is Mosby. I don't have a child
My name is Paul. I don't have a child
My name is Nana. I don't have a child
My name is Lira. I don't have a child
My name is Nancy. I don't have a child

"""


print("------------------")
print("")


# Create a new child with their parent being the one in the same index in parent_class list
# parent should be the class Parent you created


child_class = []

for c in child_class:

    print(c)

"""
Should print:

My name is Ben. My parent is Ted
My name is Julie. My parent is Mosby
My name is Bart. My parent is Paul
My name is Lisa. My parent is Nana
My name is Mark. My parent is Lira
My name is Katie. My parent is Nancy

"""

# Print out each element of the following array on a separate line:

# ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]
# You may use whatever programming language you'd like.

# Verbalize your thought process as much as possible before writing any code. 
# Run through the UPER problem solving framework while going through your thought process.

a = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]
b = [i for i in range(len(a))]
print(b[i])

<!-- def each_elem(a):
    for i in range(len(a)):
        print(a[i])


each_elem(a) --> 

def isPalindrome(s):
  # st = s.lower()
  ss = ''.join(s.lower().split(' '))
  my_lst = ''.join(reversed(ss))
  if ss == my_lst:
    return True
  else:
    return False
  # return ss
print(isPalindrome('Was It A Rat I Saw')) 

# flatten a list
def uncover_spy(n, trust):
  find_spy = []
  for sublst in trust:
      for item in sublst:
          find_spy.append(item)

  return find_spy
print(uncover_spy(2, [[1, 3], [2, 3], [3, 1]]))


#add 2 huge nums
def addTwoHugeNumbers(a, b):
    
    list_1 = list()
    list_2 = list()
    
    # traverse both llist
    
    cur = a
    
    while cur is not None:
        
        to_string = f"{'0' * (4 - len(str(cur.value))) + str(cur.value) }" if len(str(cur.value)) < 4 else str(cur.value)
      
        list_1.append(to_string)
       
        cur = cur.next
        
    cur = b
    
    while cur is not None:
        
        to_string = f"{'0' * (4 - len(str(cur.value))) + str(cur.value)}" if len(str(cur.value)) < 4 else str(cur.value)
        
        list_2.append(to_string)

        cur = cur.next
        
    joined_1 = int("".join([num for num in list_1]))
    joined_2 = int("".join([num for num in list_2]))
    
    sum_of_ll = joined_1 + joined_2
    
    # check if sum is 0
    if sum_of_ll == 0:
        
        node = ListNode(sum_of_ll)
        
        return node
   
    result = list()
     
    while sum_of_ll > 0:
        
        new_value = sum_of_ll % 10000
        
        result.append(new_value)
        
        sum_of_ll = sum_of_ll // 10000
    
    # reconstruct linked list
    reversed_result = result[::-1]
    
    new_head = None
    pointer = None
    
    for num in reversed_result:
        
        node = ListNode(num)
        
        if new_head is None:
            
            new_head = node
            pointer = new_head
            
            
        else:
            
            pointer.next = node
            pointer = pointer.next
            
            
    return new_head    

#interview
Print out each element of the following array on a separate line, but this time the input array can contain arrays nested to an arbitrarily deep level:

['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]
For the above input, the expected output is:

Bob
Slack
reddit
89
101
alacritty
(brackets)
5
375
0
{slice, owned}
22
You may use whatever programming language you'd like.

Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
        
            
# Implement functionality to reverse an input string. Print out the reversed string.

# For example, given a string "cool", print out the string "looc".

# You may use whatever programming language you'd like.

# Verbalize your thought process as much as possible before writing any code. 
# Run through the UPER problem solving framework while going through your thought process.

def reverse_string(s):
    a = ''
    for elem in reversed(s):
        a += elem

    return a 
s = 'cool'
print(reverse_string(s))

def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 

s = 'cool'
print(s[::-1])

a = "cool"

slice_obj = slice(-1, 0 - len(a) - 1, -1)

print(a[slice_obj])

def reverse(string): 
    string = "".join(reversed(string)) 
    return string 


"""
Using a WHILE LOOP, print out all of the numbers in the following array that are divisible by 3:

["85", "46", 27, "81", 94, "9", "27", 38, "43", "99", 37, 63, 31, "42", 14]
The expected output for the above input is:

27
81
9
27
99
63
42

You may use whatever programming language you wish.

Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.

Identify the runtime complexity of your solution.
"""


arr = ["85", "46", 27, "81", 94, "9", "27",
       38, "43", "99", 37, 63, 31, "42", 14]


def areFollowingPatterns(strings, patterns):
    s_dict = dict()
    p_dict = dict()
    
    s_set = set(strings)
    p_set = set(patterns)
    if len(s_set) != len(p_set):
        
        return False
    
    for i in range(len(strings)):
        
        if i + 1 <= len(strings) - 1:
            
            if strings[i] == strings[i + 1]:
                
                s_dict[i] = "same"
                
            else:
                
                s_dict[i] = "not same"
                         
    for i in range(len(patterns)):
        
        if i + 1 <= len(patterns) - 1:
            
            if patterns[i] == patterns[i + 1]:
                
                p_dict[i] = "same"
                
            else:
                
                p_dict[i] = "not same"        
                
    for key in s_dict:
        
        if s_dict[key] != p_dict[key]:
            
            return False
            
    return True