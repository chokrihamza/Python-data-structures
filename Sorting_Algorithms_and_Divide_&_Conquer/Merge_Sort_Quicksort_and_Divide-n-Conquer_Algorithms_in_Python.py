# Problem
"""
we'll focus on solving the following problem:

QUESTION 1: You're working on a new feature on Jovian called
"Top Notebooks of the Week". Write a function to sort a list
of notebooks in decreasing order of likes. Keep in mind that
up to millions of notebooks can be created every week, so your
function needs to be as efficient as possible.
-----------------------------------------------------------------------------------------------------
The problem of sorting a list of objects comes up over and over in computer science
and software development, and it's important to understand common approaches for sorting,
and the trade-offs they offer. Before we solve the above problem, we'll solve a simplified
version of the problem:
-----------------------------------------------------------------------------------------------------
QUESTION 2: Write a program to sort a list of numbers.

"Sorting" usually refers to "sorting in ascending order", unless specified otherwise.

-----------------------------------------------------------------------------------------------------
The Method
Here's a systematic strategy we'll apply for solving problems:

1-State the problem clearly. Identify the input & output formats.
2-Come up with some example inputs & outputs. Try to cover all edge cases.
3-Come up with a correct solution for the problem. State it in plain English.
4-Implement the solution and test it using example inputs. Fix bugs, if any.
5-Analyze the algorithm's complexity and identify inefficiencies, if any.
6-Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

"""
# 1. State the problem clearly. Identify the input & output formats.
# Problem
# We need to write a function to sort a list of numbers in increasing order.

import random

in_list=list(range(1000))
random.shuffle(in_list)
#print(in_list)
""" 
3. Come up with a correct solution. State it in plain English.
It's easy to come up with a correct solution. Here's one:

Iterate over the list of numbers, starting from the left
Compare each number with the number that follows it
If the number is greater than the one that follows it, swap the two elements
Repeat steps 1 to 3 till the list is sorted.
We need to repeat steps 1 to 3 at most n-1 times to ensure that the array is sorted. 
Can you explain why? Hint: After one iteration, the largest number in the list.

This method is called bubble sort, as it causes smaller elements to bubble to the top
and larger to sink to the bottom. Here's a visual representation of the process:
"""

def bubble_sort(nums):


    for _ in range(len(nums)-1):
        for i in range(len(nums)-1-_):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]

    return nums



#print(bubble_sort([5,3,8,10,4,7,90,-20]))

""" 
--Analyze the algorithm's complexity and identify inefficiencies--
(𝑛−1)(n-1)  i.e.  𝑛2−2𝑛+1 
O(n^2)
bubble sort requires  𝑂(1)  additional space.
"""
""" 
Insertion Sort
Before we look at explore more efficient sorting techniques,
here's another simple sorting technique called insertion sort,
where we keep the initial portion of the array sorted and insert
the remaining elements one by one at the right position.

As we saw from the last test, a list of 10,000 numbers takes about 12 seconds 
to be sorted using bubble sort. A list of ten times the size will 100 times longer
i.e. about 20 minutes to be sorted, which is quite inefficient. A list of a million elements
would take close to 2 days to be sorted.

The inefficiency in bubble sort comes from the fact that we're shifting elements
by at most one position at a time.


"""

def insertion_sort(nums):
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]

            j-=1
        nums[j+1]=key
    return nums



#print(insertion_sort([5,3,8,10,4,7,90,-20]))

""" 
6. Apply the right technique to overcome the inefficiency. Repeat Steps 3 to 6.
To performing sorting more efficiently, we'll apply a strategy called Divide and Conquer,
 which has the following general steps:

1-Divide the inputs into two roughly equal parts.
2-Recursively solve the problem individually for each of the two parts.
3-Combine the results to solve the problem for the original inputs.
4-Include terminating conditions for small or indivisible inputs.

"""

# Merge Sort
# 1- divide
# 2- conquer
# 3- combine



def merge_sort(nums):
    # base condition if nums has 0 or 1 element
    if len(nums)<=1:
        return nums
    # Get the mid point
    mid=len(nums)//2
    # split the lists
    left = nums[:mid]
    right = nums[mid:]
    # sort the lists
    left_sorted,right_sorted=merge_sort(left),merge_sort(right)
    # call the helper function
    # combine the results of the two halves
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums

# the hint know is to create the merge helper function
# the idea is to compare the element in order and assigne them in a new table

def merge(nums1,nums2):
    # list to store the reslut
    merged=[]
    # indices for iteration
    i,j=0,0
    # Loop over the two list
    while i<len(nums1) and j<len(nums2):
        # include the smaller element in the list and move
        if nums1[i]<=nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j += 1

    # get the remaining parts
    nums1_tail=nums1[i:]
    nums2_tail=nums2[j:]
    # Return the final merged array
    return merged+nums1_tail+nums2_tail

# test
#print(merge([1, 4, 7, 9, 11], [-1, 0, 2, 3, 8, 12]))

#print(merge_sort([5,3,8,10,4,7,90,-20]))

# 9. Analyze the algorithm's complexity and identify inefficiencies

""" 
Analyzing the complexity of recursive algorithms can be tricky.
It helps to track and follow the chain of recursive calls.
We'll add some print statements to our merge_sort and merge_functions to display 
the tree of recursive function calls.
"""

# Analyze the algorithm's complexity and identify inefficiencies
""" 
Analyzing the complexity of recursive algorithms can be tricky. 
It helps to track and follow the chain of recursive calls.
We'll add some print statements to our merge_sort and merge_functions
to display the tree of recursive function calls.

1 - n elements
2 - 2*n/2
3- 4*2/4
4-8*n/8
.
.
.
.
n- n ( 1 1 1 1 1 1 ........1 1 1 1 1) n times

total number of comparison using merge is n in each level
if h is the heigh of the tree
we have in total n*h comparison

2^𝑘∗𝑛/2^𝑘=𝑛 .
Thus, if the height of the tree is  ℎ , 
the total number of comparisons is  𝑛∗ℎ .
Since there are  𝑛  sublists of size 1 at the lowest level, 
it follows that  2^(ℎ−1)=𝑛  i.e.  ℎ=log𝑛+1 .
*Thus the time complexity of the merge sort algorithms is  𝑂(𝑛log𝑛) .
*The space complexity of merge sort is  𝑂(𝑛) .
"""

"""
def merge(nums1, nums2, depth=0):
    print('  ' * depth, 'merge:', nums1, nums2)
    i, j, merged = 0, 0, []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    return merged + nums1[i:] + nums2[j:]


def merge_sort(nums, depth=0):
    print('  ' * depth, 'merge_sort:', nums)
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid], depth + 1),
                 merge_sort(nums[mid:], depth + 1),
                 depth + 1)



"""

#10. Apply the right technique to overcome the inefficiency. Repeat Steps 3 to 6.
#--------------------------------------------------------------------------------
# the problem with merge sort is the space complexity we need an efficient solution
# for this problem
#----------------------------------------------------------------------------------
# Quick Sort
""" 
10. Apply the right technique to overcome the inefficiency. Repeat Steps 3 to 6.
The fact that merge sort requires allocating additional space as large as the input 
itself makes it somewhat slow in practice because memory allocation is far more 
expensive than comparisons or swapping.

Quicksort
To overcome the space inefficiencies of merge sort,
we'll study another divide-and-conquer based sorting
algorithm called quicksort, which works as follows:

If the list is empty or has just one element, return it. It's already sorted.
Pick a random element from the list. This element is called a pivot.
Reorder the list so that all elements with values less than or equal 
to the pivot come before the pivot, while all elements with values greater 
than the pivot come after it. This operation is called partitioning.
The pivot element divides the array into two parts which can be sorted
independently by making a recursive call to quicksort.

Quicksort
To overcome the space inefficiencies of merge sort, we'll study another divide-and-conquer based sorting algorithm called quicksort, which works as follows:

1-If the list is empty or has just one element, return it. It's already sorted.
2-Pick a random element from the list. This element is called a pivot.
3-Reorder the list so that all elements with values less than or equal to the pivot come before the pivot, while all elements with values greater than the pivot come after it. This operation is called partitioning.
4-The pivot element divides the array into two parts which can be sorted independently by making a recursive call to quicksort.
"""


def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot - 1)
        quicksort(nums, pivot + 1, end)

    return nums


def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1

    # Initialize right and left pointers
    l, r = start, end - 1

    # Iterate while they're apart
    while r > l:
        # print('  ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1

        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1

        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end

l1 = [1, 5, 6, 2, 0, 11, 3]
pivot = partition(l1)
print(l1, pivot,quicksort(l1))

"""
Time complexity : O(nlogn) average / worst case O(n^2)
Space :O(1)

"""


class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)

nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]

#print(notebooks)

def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'


def default_compare(x, y):
    if x < y:
        return 'less'
    elif x == y:
        return 'equal'
    else:
        return 'greater'

def merge_sort(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(merge_sort(objs[:mid], compare),
                 merge_sort(objs[mid:], compare),
                 compare)

def merge(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

sorted_notebooks = merge_sort(notebooks, compare_likes)

print(sorted_notebooks)