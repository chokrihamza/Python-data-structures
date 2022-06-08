# we going to create an algorithme
# to sort data in sorted and rotated list

# example [4,5,1,2,3]
# the idea is to find the pivot element in the list
# here the target is (1) the index of the element 5
# after that run binary search in both left and right parts

# first we develop a solution in linear complexity

def linear_search(list,target):

    i=0
    while i <len(list):
        if list[i]==target:
            return i

        i+=1
    return -1


print(linear_search([4,5,1,2,3],2))

# complexity time O(n)
# lest implement a binary search for the rotated table
# find the pivot
def pivoted_binary_search(list,n,key):
    pivot=findPivot(list,0,n-1)
    # if pivot not exist then the is no rotation
    if pivot==-1:
        return binary_search(list,0,n-1,key)
    # if we found a pivot
    if list[pivot]==key:
        return pivot

    if list[0]<=key:
        return binary_search(list,0,pivot-1,key)
    return binary_search(list,0,pivot+1,key)

def findPivot(list,low,high):
    # base condition
    if high<low:
        return -1
    if high==low:
        return low
    mid=(low+high)//2

    if mid<high and list[mid]<list[mid+1]:
        return mid-1
    if list[low]>=list[mid]:
        return findPivot(list,low,mid-1)
    return findPivot(list,mid+1,high)

def binary_search():

    [6,7,8,9,10,1,2]
