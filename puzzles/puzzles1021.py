# In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

# The spy, if it exists:

# Does not trust anyone else.
# Is trusted by everyone else (he's good at his job).
# Works alone; there are no other spies in the city-state.
# You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

# If the spy exists and can be found, return their identifier. Otherwise, return -1.

# Example 1:

# Input: n = 2, trust = [[1, 2]]
# Output: 2
# Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.
# Example 2:

# Input: n = 3, trust = [[1, 3], [2, 3]]
# Output: 3
# Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3, but Person 3 does not trust either Person 1 or Person 2. Thus, Person 3 is the spy.
# Example 3:

# Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
# Output: -1
# Explanation: Person 1 trusts Person 3, Person 2 trusts Person 3, and Person 3 trusts Person 1. Since everyone trusts at least one other person, there is no spy.
# Example 4:

# Input: n = 3, trust = [[1, 2], [2, 3]]
# Output: -1
# Explanation: Person 1 trusts Person 2, and Person 2 trusts Person 3. However, in this situation, we don't have any one person who is trusted by everyone else. So we can't determine who the spy is in this case.
# Example 5:

# Input: n = 4, trust = [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]]
# Output: 3
# Explanation: Person 1 trusts Person 3 and Person 4, Person 2 trusts Person 3 and Person 4, Person 4 trusts Person 3. Everyone trusts Person 3 but Person 3 does not trust anyone, so they are the spy.


def uncover_spy(n, trust):  # [[1, 3], [2, 3], [3, 1]]
    # find_spy = []
    # for sublst in trust:
    #     for item in sublst:
    #         find_spy.append(item)  # [1, 3, 2, 3, 3, 1]

    peopleTrusted = {}
    peopleSeen = []
    people = 0
    for i in trust:
        if i[0] not in peopleSeen:
            people += 1
            peopleSeen.append(i[0])
        if i[1] not in peopleSeen:
            people += 1
            peopleSeen.append(i[1])
    # [[1,3],[2,3],[3,5],[4,5],[5,1]]
    # [[1,4],[2,4],[3,1]]
    # [[1,3],[2,3],[3,4]]
    # [[]]
    # to keep a count of persons trusted by others
    for elem in trust:
        if elem[1] in peopleTrusted:
            peopleTrusted[elem[1]] += 1
        else:
            peopleTrusted[elem[1]] = 1
    max = 0
    # to find the person trusted most, by others
    for key in peopleTrusted:
        if peopleTrusted[key] > max:
            max = key
    #print(max)
    # to check if that person trusts others
    for elem in trust:
        if elem[0] == max:
            return -1
    # if that person doesn't trust anyone, 
    # checking to see if everyone else trusts him/her(except the spy, so it is (n-1) => (people -1))
    #print(people)
    if people - 1 == peopleTrusted[max]:
        return max
    else:
        return -1


assert(2 == uncover_spy(2, [[1, 2]]))
assert(3 == uncover_spy(3, [[1, 3], [2, 3]]))
assert(-1 == uncover_spy(3, [[1, 3], [2, 3], [3, 1]]))
assert(-1 == uncover_spy(3, [[1, 2], [2, 3]]))
assert(3 == uncover_spy(5, [[1, 3], [1, 4],[ 2, 3], [2, 4], [4, 3]]))


def uncover_spy2(n, trust):
    trusted_by = {}
    for i in range(1, n+1):
        trusted_by[i] = set()
        # print(trusted_by)
    for item in trust:
        trusted_by[item[1]].add(item[0])
        # print(trusted_by)
    candidates = []
    for i in range(1, n+1):
        if len(trusted_by[i]) == n-1:
            candidates.append(i)
        # print(candidates)
    
    if len(candidates) != 1:
        return -1
        
    candidate = candidates[0]
    for item in trust:
        if item[0] == candidate:
            return -1
    # print(item[0], candidate)
    return candidate


# def uncover_spy3(n, trust):
#     # idea 1:
#     # create a cache for each person and they people they trust
#     cache = {}
#     # set up cache with default of set()
#     for citizen in range(1, n + 1):
#         cache[citizen] = set()

#     for citizen, trusted in trust:
#         cache[citizen].add(trusted)

#     possible_spies = []
#     # maybe use dft?
#     for key, value in cache.items():
#         if len(value) == 0:
#             possible_spies.append(key)

#     if len(possible_spies) == 0 or len(possible_spies) > 1:
#         return -1

#     trusted_by = 0
#     for value in cache.values():
#         if possible_spies[0] in value:
#             trusted_by += 1

#     if trusted_by == n - 1:
#         return possible_spies[0]
#     return -1


Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. 
Your function should return a reference to the head of the updated linked list.

Example:
Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.


def condense_linked_list(node):
    current = node
    pass


def condense_linked_list2(node):
    data = {}
    new_head = node
    prev = None
    curr = node
    while curr:
        if curr.value in data:
            prev.next = curr.next
            curr = curr.next
        else:
            data[curr.value] = True
            prev = curr
            curr = curr.next
    return new_head



Given the root of a binary tree where each node contains an integer, determine the sum of all of the integer values in the tree.

Example:

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
The expected output given the above tree is 5 + 4 + 8 + 11 + 13 + 4 + 7 + 2 + 1, so your function should return 55.

def tree_paths_sum(root):
    pass

Algorithm
Define Node class which has three attributes namely: data left and right. Here, left represents the left child of the node and right represents the right child of the node.
When a node is created, data will pass to data attribute of the node and both left and right will be set to null.
Define another class which has an attribute root.
Root represents the root node of the tree and initialize it to null.
calculateSum() will calculate the sum of nodes present in the binary tree:
It checks whether the root is null, which means that the tree is empty.
If the tree is not empty, traverse through left subtree, calculate the sum of nodes and store it in sumLeft.
Then, traverse through the right subtree, calculate the sum of nodes and store it in sumRight.
Finally, calculate total sum = temp.data + sumLeft + sumRight.

#Represent a node of binary tree  
class Node:  
    def __init__(self,data):  
        #Assign data to the new node, set left and right children to None  
        self.data = data;  
        self.left = None;  
        self.right = None;  
   
class SumOfNodes:  
    def __init__(self):  
        #Represent the root of binary tree  
        self.root = None;  
      
    #calculateSum() will calculate the sum of all the nodes present in the binary tree  
    def calculateSum(self, temp):  
        sum = sumRight = sumLeft = 0;  
          
        #Check whether tree is empty  
        if(self.root == None):  
            print("Tree is empty");  
            return 0;  
        else:  
            #Calculate the sum of nodes present in left subtree  
            if(temp.left != None):  
                sumLeft = self.calculateSum(temp.left);  
              
            #Calculate the sum of nodes present in right subtree  
            if(temp.right != None):  
                sumRight = self.calculateSum(temp.right);  
              
            #Calculate the sum of all nodes by adding sumLeft, sumRight and root node's data  
            sum = temp.data + sumLeft + sumRight;   
        return sum;  
   
bt = SumOfNodes();  
#Add nodes to the binary tree  
bt.root = Node(5);  
bt.root.left = Node(2);  
bt.root.right = Node(9);  
bt.root.left.left = Node(1);  
bt.root.right.left = Node(8);  
bt.root.right.right = Node(6);  
   
#Display the sum of all the nodes in the given binary tree  
print("Sum of all nodes of binary tree: " + str(bt.calculateSum(bt.root)));  