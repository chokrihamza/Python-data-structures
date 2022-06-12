# In this assignment, we will
"""
1-implement hash tables from scratch in Python
2-Handle hashing collisions using linear probing
3-Replicate the functionality of Python dictionaries
"""
#Problem Statement - Python Dictionaries and Hash Tables
"""
in this assignment, 
you will recreate Python dictionaries from scratch
using data structure called hash table.
Dictionaries in Python are used to store key-value pairs.
Keys are used to store and retrieve values. 
For example, here's a dictionary for storing and retrieving 
phone numbers using people's names.

"""
# python dictionaries

phone_numbers={
    'hamza':"200552155",
    'jhon':"2015525989",
    'alex':"205567887"

}

print(phone_numbers,phone_numbers['hamza'])
print(phone_numbers.values())
print(phone_numbers.keys())
print(phone_numbers.items())

for name in phone_numbers:
    print('Name: '+name+'/ Phone Number: '+phone_numbers[name])
"""
Dictionaries in Python 
are implemented using a data structure called hash table.
A hash table uses a list/array to store the key-value pairs,
and uses a hashing function to determine the index for storing 
or retrieving the data associated with a given key.

---------------------------------------------------------------
The objective in this assignment is to implement a 
HashTable class which supports the following operations:

1-Insert: Insert a new key-value pair
2-Find: Find the value associated with a key
3-Update: Update the value associated with a key
4-List: List all the keys stored in the hash table
The HashTable class will have the following structure
 (note the function signatures):
"""

class HashTable:
    def insert(self,key,value):
        """ insert a new key value pair"""
        pass

    def find(self,key):
        """Find the value associated with the key"""
        pass
    def update(self,key,value):
        """change the value associated with the key"""
        pass
    def list_all(self):
        """List all the keys"""
        pass

# to start the creation of our hashtable
# first we create a List Data and we fix the size of the list

MAX_HASH_TABLE_SIZE=4096

data_list=[None]*4096

#print(len(data_list)==4096)

""" 
Hashing Function
A hashing function is used to convert strings
and other non-numeric data types into numbers,
which can then be used as list indices. For instance,
if a hashing function converts the string "Hamza" into the number 4,
then the key-value pair ('Hamza', '2015245855') 
will be stored at the position 4 within the data list.

Here's a simple algorithm for hashing, which can convert strings into numeric list indices.

1-Iterate over the string, character by character
2-Convert each character to a number using Python's built-in ord function.
3-Add the numbers for each character to obtain the hash for the entire string
4-Take the remainder of the result with the size of the data list


"""
# let's create a simple hash function using ASCII code
def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = 0

    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number

    # Take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index


print(get_index(data_list, '')==None )

#Insert
#To insert a key-value pair into a hash table,
# we can simply get the hash of the key,
# and store the pair at that index in the data list.

data_list[get_index(data_list,'hamza')]=('hamza','202154215')
data_list[get_index(data_list,'alex')]=('alex','245225882')
#print(data_list[104])

#Find
#The retrieve the value associated with a pair,
# we can get the hash of the key and look up that index in the data list.
idx = get_index(data_list, 'hamza')
key, value = data_list[idx]
#print(value)

#List
#To get the list of keys, we can use a simple list comprehension.
# get the list of keys
pairs = [kv[0] for kv in data_list if kv is not None]

#print(pairs)

""" 
Basic Hash Table Implementation

We can now use the hashing function defined above to implement a basic hash table in Python.

QUESTION 3: Complete the hash table implementation below by following the instructions in the comments.

Hint: Insert and update can have identical implementations.

"""


class BasicHashTable:
        def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
             # 1. Create a list of size `max_size` with all values None
             self.data_list = [None]*max_size

        def insert(self, key, value):
            # 1. Find the index for the key using get_index
            idx = get_index(self.data_list, key)

            # 2. Store the key-value pair at the right index
            self.data_list[idx] = (key,value)

        def find(self, key):
            # 1. Find the index for the key using get_index
            idx = get_index(self.data_list, key)

            # 2. Retrieve the data stored at the index
            kv = self.data_list[idx]

            # 3. Return the value if found, else return None
            if kv is None:
                return None
            else:
                key, value = kv
                return value

        def update(self, key, value):
            # 1. Find the index for the key using get_index
            idx = self.get_index(self.data_list, key)

            # 2. Store the new key-value pair at the right index
            self.data_list[idx] = (key,value)

        def list_all(self):
            # 1. Extract the key from each key-value pair
            return [kv[0] for kv in self.data_list if kv is not None]


#Handling Collisions with Linear Probing
# example
print(get_index(data_list,'listen'))
print(get_index(data_list,'silent'))

# we have the same index returned by the hash function (Collisions)

""" 
As you can see above, 
the value for the key listen was overwritten by the value for the key silent.
 Our hash table implementation is incomplete because it does not handle collisions correctly.

To handle collisions we'll use a technique called linear probing. Here's how it works:

1-While inserting a new key-value pair if the target index for a key is occupied 
by another key, then we try the next index, followed by the next and so on
 till we the closest empty location.

2- While finding a key-value pair, 
we apply the same strategy, but instead of searching for an empty location,
 we look for a location which contains a key-value pair with the matching key.

3-While updating a key-value pair, we apply the same strategy, 
but instead of searching for an empty location, we look for a location which contains
a key-value pair with the matching key, and update its value.

3-We'll define a function called get_valid_index,
which starts searching the data list from the index
determined by the hashing function get_index and returns
the first index which is either empty or contains a key-value pair
matching the given key.
"""

#QUESTION 4: Complete the function get_valid_index below by following the instructions in the comments.
def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list,key)

    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]

        # If it is None, return the index
        if kv is None:
            return idx

        # If the stored key matches the given key, return the index
        k, v = kv
        if k==key:
            return idx

        # Move to the next index
        idx += 1

        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0



""" 
Hash Table with Linear Probing
We can now implement a hash table with linear probing.

QUESTION 5: Complete the hash table (with linear probing) 
implementation below by following the instructions in the comments.
"""


class ProbingHashTable:
        def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
             # 1. Create a list of size `max_size` with all values None
             self.data_list = [None]*max_size

        def insert(self, key, value):
            # 1. Find the index for the key using get_valid_index
            idx = get_valid_index(self.data_list, key)

            # 2. Store the key-value pair at the right index
            self.data_list[idx] = key,value

        def find(self, key):
            # 1. Find the index for the key using get_valid_index
            idx = get_valid_index(self.data_list, key)

            # 2. Retrieve the data stored at the index
            kv = self.data_list[idx]

            # 3. Return the value if found, else return None
            return None if kv is None else kv[1]

        def update(self, key, value):
            # 1. Find the index for the key using get_valid_index
            idx = get_valid_index(self.data_list, key)

            # 2. Store the new key-value pair at the right index
            self.data_list[idx] = key ,value

        def list_all(self):
            # 1. Extract the key from each key-value pair
            return [kv[0] for kv in self.data_list if kv is not None]

