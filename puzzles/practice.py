class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, num):
        self.num = 0
        self.head = None
        if num == 0:
            numStr = ''
        else:
            numStr = str(num)
        for i in range(len(numStr[i])):
            digit = int(numStr[i])
            
    def insert_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            next = self.head
            self.head = new_node
            new_node.next = next

    def insert_tail(self, value):
        new_node = Node(value)
        curr = self.head
        while curr:
            if self.tail is None:
                self.tail = new_node
            else:
                prev = self.tail
                self.tail = new_node
                new_node.next = None

    def __add__(self, num2):
        sum = LinkedList(0)
        a = self.head
        b = num2
        carry = 0
        while a or b or carry:
            digit_sum = 0
            if a:
                digit_sum += a.value
            if b:
                digit_sum += b.value
            digit_sum += carry
            carry = digit_sum // 10
            digit_sum = digit_sum % 10

            sum.insert_tail(digit_sum)
            if a:
                a = a.next
            if b:
                b = b.next

    def __str__(self, num):
        s = ''
        curr = self.head
        while curr:
            s = str(curr.value) + s
            curr = curr.next

        return s

num1 = LinkedList(666)
num2 = LinkedList(123)
num3 = num1 + num2 

# SURROUNDED REGIONS
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Ex2:
X O X X
X O O X
X X O X
X O X O 
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X O

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

from typing import List, Set, Tuple

def check_matrix(row: int, col: int, board: List[List[str]]) -> Set[Tuple[int, int]]:
    o_queue = []
    checked_spots = set([(row, col)])
    # to check if 'O's are on the edges
    is_surrounded = True
    # finding all the 'X' and 'O's
    for (new_row, new_col) in [(row, col - 1), (row, col + 1), (row -1, col), (row + 1, col)]:
        if new_row == -1 or new_col == -1 or new_row == len(board) or new_col == len(board[new_row]):
            is_surrounded = False
            continue
        if board[new_row][new_col] == '0' and (new_row, new_col) not in checked_spots:
            o_queue.append((new_row, new_col))
            print(o_queue)
            checked_spots.add((new_row, new_col))
            print(checked_spots)
    # finding all the 'O's
    while o_queue:
        (row, col) = o_queue.pop()
        for (new_row, new_col) in [(row, col - 1), (row, col + 1), (row -1, col), (row + 1, col)]:
             if new_row == -1 or new_col == -1 or new_row == len(board) or new_col == len(board[new_row]):
            is_surrounded = False
            continue
        if board[new_row][new_col] == '0' and (new_row, new_col) not in checked_spots:
            o_queue.append((new_row, new_col))
            print(o_queue)
            checked_spots.add((new_row, new_col))
            print(checked_spots)
    # Which 'O's to modify
    if is_surrounded:
        for (row, col) in checked_spots:
            board[row][col] = 'X'
    return checked_spots

# updating the matrix
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        checked_spots = set([])
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'O' and (row, col) not in checked_spots:
                    checked_spots.update(check_matrix(row, col, board))
                    print(checked_spots)
        return None

⛅️ Jumping on the Clouds 🌩
There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. 
The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.
For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

Example
c = [0,1,0,0,0,1,0]
Index the array from 0 to 6. The number on each cloud is its index in the list so the player must avoid the clouds at indices 1 and 5. They could follow these two paths: 0->2->4->6 or 0->2->3->4->6. 
The first path takes 3 jumps while the second takes 4. Return 3.

Sample Input 0   Sample Output 0: 4
7
0 0 1 0 0 1 0   
Explanation 0:
The player must avoid c[2] and c[5]. The game can be won with a minimum of 4 jumps:

Sample Input 1   Sample Output 0: 3
6
0 0 0 0 1 0
Explanation 1:
The only thundercloud to avoid is c[4]. The game can be won in 3 jumps.

# Iterate thru elems in the array
# Keep a jump count while iterating and filtering
# Filter if elem == '1'
# Find the min no of jumps

def jumpingOnClouds(c):
    # increment by 1 or 2
    # Always want to jump by 2 for shortest path
    # increment our jump count
    # check if it is a cumulus or thunderstorm cloud
    # if cumulus, jump by 2 else jump by 1
    jumpCount = 0 # no of jumps
    currentCloudIdx = 0 # keep track of current cloud idx
    # while loop over c(end it if currentCloudIdx > len(c))
    while currentCloudIdx < (len(c) - 1):
        # if currentCloudIdx + 2 >= len(c) and c[currentCloudIdx + 2] == 1:
            # currentCloudIdx += 1
            # num_jump += 1
        if currentCloudIdx + 2 < len(c) and c[currentCloudIdx + 2] == 0:
            currentCloudIdx += 2
        else: # if the cloud is thunderstorm, jump 1
            currentCloudIdx += 1
        jumpCount += 1

    return jumpCount += 1

def jumpingOnClouds2(c):
    num_jumps = 0
    current = 0
    while current < (len(c) - 1):
        two_jumps = current + 2
        if two_jumps >= len(c) and c[two_jumps] == 1: # if it is thundertorm
            # jump 1
            current += 1
            num_jumps += 1
        else:
            # if it is cumulus, jump 2
            current += 2
            num_jumps += 1

    return num_jumps 


