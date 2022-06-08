# this is a brute force approach
# declare the function
def binary_serch(array,target):
    # create the varbile postion with the value of 0
    postion=0
    # set up the while loop
    # log the data
    print("array: ",array)
    print("target: ",target)
    while postion<len(array):
        if array[postion]==target:
            # if we reach the target we show the postion and exit
            return postion
        # increment postion +1
        postion+=1
        if postion==len(array):
            return -1

# test our function
print(binary_serch([1,2,3,45,20,5,10,47],20))
print(binary_serch([1,2,3,45,20,5,10,47],200))

# complexity
# Time  O(n)
# Space O(1)