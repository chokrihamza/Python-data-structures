# we will define a global approch for all the problems
# here the target is to retrun the first element even
# if the elements are duplicated in the table
def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards) - 1, condition)

# bunch of tests

print(locate_card([13, 11, 10, 7, 4, 3, 1, 0],7))
print(locate_card([13, 11, 10, 7, 4, 3, 1, 0],1))
print(locate_card([4, 2, 1, -1],4))
print(locate_card([3, -1, -9, -127],-127))
print(locate_card([6],6))
print(locate_card([9, 7, 5, 2, -9],4))
print(locate_card([],7))
print(locate_card([8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],3))
print(locate_card([8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],6))


