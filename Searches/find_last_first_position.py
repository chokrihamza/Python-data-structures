#find the first and the last position in a table
# 1 - we ned to sort the table
# create the generic binary search
# create a condition for both first and the last position

# define our generic binary_search for any condition
def Generic_binary_search(low,high,condition):
    while low<high:
        mid=(low+high)//2
        result=condition(mid)
        if result=="found":
            return mid
        if result=="left":
            high=mid-1
        if result=="right":
            low=mid+1
    return -1

# we define a fucntion containing the close condition
# and than return the Generic_binary_search(low,high,condition) with the defined condition

def first_position(table,target):
    def condition(mid):
       if table[mid]==target:
          if  mid>0 and table[mid-1]==target:
            return "left"
          else:
            return "found"

       elif table[mid]<target:
           return "right"
       else:
           return "left"
    return Generic_binary_search(0,len(table)-1,condition)

def last_position(table,target):
    def condition(mid):
       if table[mid]==target:
          if  mid < len(table)-1 and table[mid+1]==target:
            return "right"
          return "found"

       elif table[mid]<target:
           return "right"
       else:
           return "left"
    return Generic_binary_search(0,len(table),condition)

# conbine both of them:
def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

# test the problem
A=[1,2,3,3,3,5,6,6,6,6,6,6,6,6,6,6,6]
print(first_and_last_position(A, 6))