# count the number of rotation
# in a sorted list

def count_rotations_linear(table):
    min=table[0]
    i=0
    rotate=0
    while i<=len(table)-1:
        if table[i]<min:
            min=table[i]
            rotate=i
        i+=1
    return min


print(count_rotations_linear([6,7,2,3,4,5]))

# another solution
def count_rotations_linear1(table):
    position=1
    while position <len(table):
        if position > 0 and table[position]<table[position-1]:
            return position
        position+=1
    return 0


print(count_rotations_linear1([6,7,8,9,10,11,2,3,4,5]))

# optimized solution using binary search
# [5,4,0,1,2,3]  table(mid)<table(mid+1)&  table(mid)<table(mid-1) then return index

# [6,7,8,9,10,11,2,3,4,5] table(mid)> table(end) then start=mid+1

# example 2 [4,0,1,2,3] table(mid)<table(start) then high=mid-1

def count_rotation(table):
    low=0
    high=len(table)-1

    while low<=high:
        mid = low +(high -low )//2
        # get the previous  and the next index for the mid
        #prev=mid-1
        prev=(mid-1+len(table))%len(table)
        print("prev"+str(prev))
        #next=mid+1
        next = (mid +1) % len(table)
        print("next"+str(next))
        if table[mid]<table[prev] and table[next]>=table[mid]:
            return mid
        elif table[mid]<table[low]:
            high=mid-1
        elif table[mid]>table[high]:
            low=mid+1
        else:
            return 0


print(count_rotation([3,2,1]))


# Time : O(log n)
# Space: O(log n)
# we can reduce the space to O(1)
# just use add n { len(table)} as a parameter











