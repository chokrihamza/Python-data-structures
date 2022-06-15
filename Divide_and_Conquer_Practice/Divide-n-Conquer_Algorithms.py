"""
Assignment 3 - Divide-n-Conquer Algorithms in Python
This assignment is a part of the course "Data Structures and Algorithms in Python".

In this assignment, you will implement an efficient algorithm for polynomial multiplication.

As you go through this notebook, you will find the symbol ??? in certain places.
To complete this assignment, you must replace all the ??? with appropriate values,
expressions or statements to ensure that the notebook runs properly end-to-end.

Guidelines

1-Make sure to run all the code cells, otherwise you may get errors like NameError for undefined variables.
2-Do not change variable names, delete cells or disturb other existing code. It may cause problems during evaluation.
3-In some cases, you may need to add some code cells or new statements before or after the line of code containing the ???.
4-Since you'll be using a temporary online service for code execution, save your work by running jovian.commit at regular intervals.
5-Questions marked (Optional) will not be considered for evaluation, and can be skipped. They are for your learning.
6-If you are stuck, you can ask for help on the [community forum]
(TODO - add link). Post errors or ask for hints, but please don't ask for OR share the full working answer code on the forum.
7-There are some tests included with this notebook to help you test your implementation.
However, after submission your code will be tested with some hidden test cases.
Make sure to test your code exhaustively to cover all edge cases.
Given two polynomials represented by two lists, write a function that efficiently multiplies given two polynomials.
For example, the lists [2, 0, 5, 7] and [3, 4, 2] represent the polynomials
2+5x^2+7x^3
and
3+4x+2x^2.
Their product is:
6+8x+19x^2+41x^3+38x^4+14x^5
It can be represented by the list [6, 8, 19, 41, 38, 14]
---------------------------------------------------------------------------------
The Method
Here's the systematic strategy we'll apply for solving problems:

1-State the problem clearly. Identify the input & output formats.
2-Come up with some example inputs & outputs. Try to cover all edge cases.
3-Come up with a correct solution for the problem. State it in plain English.
4-Implement the solution and test it using example inputs. Fix bugs, if any.
5-Analyze the algorithm's complexity and identify inefficiencies, if any.
6-Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
7-This approach is explained in detail in Lesson 1 of the course. Let's apply this approach step-by-step
-------------------------------------------------------------------------------------------------------------
Solution
1. State the problem clearly. Identify the input & output formats.
While this problem is stated clearly enough, it's always useful to try and express in your own words,
in a way that makes it most clear for you.

Problem
"""
# Brute force solution
def multiply_poly(poly1,poly2):
    m=len(poly1)
    n=len(poly2)
    result=[0]*(m+n-1)
    for i in range(m):
        for j in range(n):
            result[i+j] += poly1[i]*poly2[j]
    return result

"""
test the result 

"""
#print(multiply_poly([2, 0, 5, 7], [3, 4, 2]) == [6, 8, 19, 41, 38, 14])
#print(multiply_poly([5, 0, 10, 6], [1, 2, 4]) ==[5, 10, 30, 26, 52, 24])

""" 
in the next part we make an implementation using 
devide and conquer technique 
We can apply the divide and conquer technique 
to solve this problem more efficiently. Given two polynomials A and B, 
we can express each of them as a sum of two polynomials as follows:
"""
def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])


def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly

def remove_zeros(items):
    for ele in reversed(items):
        if not ele:
            if len(items) > 1:
                del items[-1]
        else:
            break

def subtract(poly1, poly2):
    poly = [-i for i in poly2]
    return add(poly1,poly)


def multiply_optimized(poly1, poly2):
    if len(poly1) == multiply_optimized or len(poly2) == 0:
        return []

    if len(poly1) == 1:
        if poly1[0] == 0:
            return [0]
        else:
            return [poly1[0] * i for i in poly2]
    elif len(poly2) == 1:
        if poly2[0] == 0:
            return [0]
        else:
            return [poly2[0] * i for i in poly1]

    n = max(len(poly1), len(poly2))

    if n % 2 != 0:
        n = n - 1

    #     print(n)

    A, B = split(poly1, poly2)

    Y = multiply_optimized(add(A[0], A[1]), add(B[0], B[1]))
    U = multiply_optimized(A[0], B[0])
    Z = multiply_optimized(A[1], B[1])

    #     print('Before:')
    #     print(Y, U, Z)

    Y = increase_exponent(subtract(Y, add(U, Z)), n // 2)
    Z = increase_exponent(Z, n)

    #     print('After:')
    #     print(Y, U, Z)

    result = add(Y, add(U, Z))

    remove_zeros(result)

    return result













