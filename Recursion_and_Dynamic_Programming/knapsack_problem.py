# solving the knapsack problem
def max_profit_recursive(weights,profits,capacity,idx=0):
    if idx==len(weights):
        return 0
    elif weights[idx]>capacity:
        return max_profit_recursive(weights,profits,capacity,idx+1)
    else:
        option1=max_profit_recursive(weights,profits,capacity,idx+1)
        option2=profits[idx]+max_profit_recursive(weights,profits,capacity-weights[idx],idx+1)
        return max(option1,option2)

#print(max_profit_recursive([23,31,29,44,53,38,63,85,89,82],[92,57,49,68,60,43,67,84,87,72],165))
# complexity O(2^N)

""" 
solution using memoization
"""


def knapsack_memo(capacity, weights, profits):
    memo = {}
    def recurse(idx, remaining):
        key = (idx, remaining)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recurse(idx + 1, remaining)
        else:
            memo[key] = max(recurse(idx + 1, remaining),profits[idx] + recurse(idx + 1, remaining - weights[idx]))
        return memo[key]

    return recurse(0, capacity)

print(knapsack_memo(165,[23,31,29,44,53,38,63,85,89,82],[92,57,49,68,60,43,67,84,87,72]))

""" 
Solution using dynamique programming 

Dynamic Programming
1-Create a table of size (n+1) * (capacity+1) consisting of all 0s, where is n is the number of elements.
table[i][c] represents the maximum profit that can be obtained using the first i elements if the maximum
capacity is c. Here's a visual representation of a filled table (source - geeksforgeeks):
(The 0th row will contain all zeros and is not shown above.)

2-We'll fill the table row by row and column by column. table[i][c] can be filled using some values in the row above it.

3-If weights[i] > c i.e. if the current element can is larger than capacity, then table[i+1][c] is simply 
equal to table[i][c] (since there's no way we can pick this element).

4-If weights[i] <= c then we have two choices: to either pick the current element or not to get the value of table[i+1][c].
We can compare the maximum profit for both these options and pick the better one as the value of table[i][c].
A. If we don't pick the element with weight weights[i], then once again the maximum profit is table[i][c]
B. If we pick the element with weight weights[i], then the maximum profit is profits[i] + table[i][c-weights[i]],
since we have used up some capacity.

Verify that the complexity of the dynamic programming solution is 
O(N∗W).
"""

def max_profit_dp(weights,profits,capacity):
    n=len(weights)
    table=[[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for idx in range(n):
        for c in range(capacity+1):
            if weights[idx]>c:
                results[idx + 1][c] = results[idx][c]
            else:
                results[idx + 1][c] = max(results[idx][c], profits[idx] + results[idx][c - weights[idx]])

        return results[-1][-1]

print(max_profit_dp([23,31,29,44,53,38,63,85,89,82],[92,57,49,68,60,43,67,84,87,72],165))

