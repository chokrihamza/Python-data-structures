# we applay the Binarysearch only if the array is sorted
def binarySearch(array,target):
    # show data
     print("array: ",array)
     print("target: ",target)
     low=0
     high=len(array)-1
     while low<=high:
         mid=(low+high)//2
         if array[mid]==target:
             return mid
         if array[mid]>target:
             high=mid-1
         if array[mid]<target:
             low=mid+1
     return -1

# test
print(binarySearch([1,2,3,4,5,6,7,8,9],9))
print(binarySearch([1,2,3,4,5,6,7,8,9],10))
#print(binarySearch(range(0,1000000000),1000000))
# complexity
# initial length N
# iteration 1 --> N/2 i.e
# iteration 2 --> N/4 i.e N/(2)^2
# iteration 3 --> N/8 i.e N/(2)^3
# iteration 4 --> N/16 i.e N/(2)^4
# iteration 5 --> N/32 i.e N/(2)^5
# ...
# ...
# ...
# ...
# ...
# ...
# iteration k -->  i.e N/(2)^k

# since the final length of an array is 1
# so we have N/(2)^k=1 -> log(N/(2)^k)=0 -> log(N)-klog(2)=0
# -> k=log2(N)
# O(log2(N) :Time
# O(1) :Space


