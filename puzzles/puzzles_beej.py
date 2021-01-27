import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            #print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            #print("WARNING: Friendship already exists")
            return False

        self.friendships[user_id].add(friend_id)
        self.friendships[friend_id].add(user_id)
        return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph_1(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(num_users):
            self.add_user(f"User {i+1}")

        """
        possible_friendships = []
        friendship_used = set()

        for user_id in self.users:
            for friend_id in self.users:

                if user_id == friend_id: continue
                if (user_id, friend_id) in friendship_used: continue

                possible_friendships.append((user_id, friend_id))
                friendship_used.add((friend_id, user_id))
        """
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        #print(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
            #self.add_friendship(*friendship)

    def populate_graph_2(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(num_users):
            self.add_user(f"User {i+1}")

        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0 

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else: 
                collisions += 1

        print(collisions)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    #sg.populate_graph_1(100, 98)
    #sg.populate_graph_1(1000, 98)
    #sg.populate_graph_1(1000, 2)
    #sg.populate_graph_1(5000, 2)
    #sg.populate_graph_2(10000, 2)  

    #sg.populate_graph_1(500, 498)  # 0.8 s
    #sg.populate_graph_2(500, 498)  # 4.5 s
    #sg.populate_graph_1(5000, 2)   # 34.5 s
    sg.populate_graph_2(5000, 500)   # 0.2 s
    #print(sg.friendships)
    #connections = sg.get_all_social_paths(1)
    #print(connections)

    """
WORD LADDER
Given two words (begin_word and end_word), and a dictionary's word list, return
the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.

Each transformed word must exist in the word list. Note that begin_word is not
a transformed word.

Note:

Return None if there is no such transformation sequence.
All words (starting, ending, and dictionary) contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Sample:

begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']

hit
hot
cot
cog

begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

beginWord = "hungry"
endWord = "happy"
None
"""

words = set()

with open("words.txt") as f:
    for w in f:
        w = w.strip()
        words.add(w)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def get_neighbors_1(word):
    neighbors = []

    for w in words:  # O(26680) _over the number of words_
        if len(w) == len(word):
            diff_count = 0

            for i in range(len(w)):  # O(n) over the length of the word
                if w[i] != word[i]:
                    diff_count += 1

                if diff_count > 1:
                    break

            if diff_count == 1:
                neighbors.append(w)

    return neighbors

import string

def get_neighbors(word):
    neighbors = []

    letters = list(string.ascii_lowercase)  # 'a' .. 'z'

    word_letters = list(word)

    for i in range(len(word_letters)):   # O(n) over the length of the word
        for l in letters:  # O(26)
            word_letters_copy = list(word_letters)
            word_letters_copy[i] = l
            candidate_word = "".join(word_letters_copy)

            if candidate_word != word and candidate_word in words:
                neighbors.append(candidate_word)

    return neighbors

def bfs(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in get_neighbors(v):
                path_copy = path + [neighbor]
                q.enqueue(path_copy)

#Queue front->[hit,dit] [hit,bit] [hit,sit] [hit,hat] [hit,hot]

print(bfs('hit', 'cog'))
#print(bfs('sail', 'boat'))

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}


def encode(s):
    r = ''
    for c in s:
        r += encode_table[c]

    return r


print(encode('HELLO'))

decode_table = {}
for k, v in encode_table.items():
    decode_table[v] = k


def decode(s):
    r = ''
    for c in s:
        r += decode_table[c]

    return r


print(decode('DOGGE'))

