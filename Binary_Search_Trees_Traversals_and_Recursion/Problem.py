"""
Problem
In this notebook, we'll focus on solving the following problem:

QUESTION 1: As a senior backend engineer at Jovian,
 you are tasked with developing a fast in-memory data structure
  to manage profile information (username, name and email) for 100 million users.
  It should allow the following operations to be performed efficiently:

-Insert the profile information for a new user.
-Find the profile information of a user, given their username
-Update the profile information of a user, given their usrname
-List all the users of the platform, sorted by username
You can assume that usernames are unique.

Along the way, we will also solve several other questions related
 to binary trees and binary search trees that are often asked in
  coding interviews and assessments.
"""
"""
The Method
Here's a systematic strategy we'll apply for solving problems:

State the problem clearly. Identify the input & output formats.
Come up with some example inputs & outputs. Try to cover all edge cases.
Come up with a correct solution for the problem. State it in plain English.
Implement the solution and test it using example inputs. Fix bugs, if any.
Analyze the algorithm's complexity and identify inefficiencies, if any.
Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
"""

# first let's just create a a class User

class User:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email
        print('User created!')
    def introduce_yourself(self,guest_name):
        print("Hi {}, I'm {}! Contact me at {} .".format(guest_name, self.name, self.email))

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()




class UserDatabase:
    def __init__(self):
        self.users=[]

    def insert(self, user):
        i=0
        while i<len(self.users):
        # Find the first username greater than the new user's username
           if self.users[i].username>user.username:
               break
           i+=1
        self.users.insert(i,user)

    def find(self, username):
        for user in self.users:
            if user.username==username:
                return user

    def update(self, user):
        target=self.find(user.username)
        target.name,target.email=user.name,user.email

    def list_all(self):
        return self.users

user=User("hamza","hamza","chokri@gmail.com")
print(user)
print(user.email, user.username)

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

# using list data structure



database = UserDatabase()
database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)


print(database.list_all())

print(database.find('siddhant'))

database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))
print(database.find('siddhant'))

print(database.list_all())
database.insert(biraj)
print(database.list_all())

#Analyze the algorithm's complexity and identify inefficiencies

#Insert: O(N)
#Find: O(N)
#Update: O(N)
#List: O(1)

"""%%time
for i in range(100000000):
    j = i*i
    
    CPU times: user 8.42 s, sys: 8.05 ms, total: 8.42 s
Wall time: 8.43 s
It takes almost 10 seconds to execute all the iterations in the above cell.

A 10-second delay for fetching user profiles will lead to a suboptimal users
 experience and may cause many users to stop using the platform al together.
The 10-second processing time for each profile request will also significantly
 limit the number of users that can access the platform at a time or increase 
 the cloud infrastructure costs for the company by millions of dollars.
As a senior backend engineer, you must come up with a more efficient data structure!
 Choosing the right data structure for the requirements at hand is an important skill.
  It's apparent that a sorted list of users might not be the best data structure to organize
   profile information for millions of users.
    """
