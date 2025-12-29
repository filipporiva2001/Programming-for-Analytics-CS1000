# -*- coding: utf-8 -*-
# Group 4 – Assignment 7
#
# Group Members:
#   - Lucas: Manager
#   - Bryce: Quality Assurance
#   - Filippo: Spokesperson
#   - Hugo: Process Analyst
#
# Topic:
# Fibonacci Sequence
#
# This assignment demonstrates two different approaches to generating
# a Fibonacci sequence:
#   1) Iterative method
#   2) Recursive method
#
# NOTE:
# - The iterative solution does NOT use list.append()
# - The recursive solution builds the list through recursive calls
# =============================================================================


# =============================================================================
# Question 1
#
# Iterative method to generate the Fibonacci sequence without using append().
#
# The function fibn(n) returns a list containing the first n Fibonacci numbers.
#
# Example:
#   fibn(5) → [0, 1, 1, 2, 3]
# =============================================================================
def fibn(n):
    ans = []          # Initialize the list to store Fibonacci numbers
    a = 0             # First Fibonacci number
    b = 1             # Second Fibonacci number

    for i in range(n):
        ans = ans + [a]   # Concatenate the current value of 'a' as a single-element list
        a, b = b, a + b  # Update to the next Fibonacci numbers

    return ans


# Test the iterative method
print("Iterative Fibonacci (first 19 numbers):")
print(fibn(19))
print()


# =============================================================================
# Question 2
#
# Recursive method to generate the Fibonacci sequence.
#
# The function fibr(n) returns a list containing the first n Fibonacci numbers.
# Default parameters are used to keep track of the current values and results.
#
# Base case:
#   n == 0 → return the accumulated list
# =============================================================================
def fibr(n, a=0, b=1, ans=None):
    if ans is None:
        ans = []          # Initialize the list on first call

    if n == 0:
        return ans        # Base case: no more numbers to add

    ans = ans + [a]       # Add current Fibonacci number
    return fibr(n - 1, b, a + b, ans)  # Recursive call with updated values


# Test the recursive method
print("Recursive Fibonacci (first 19 numbers):")
print(fibr(19))


# =============================================================================
# Source Note:
# ChatGPT was used to help with the recursion method implementation.
# =============================================================================
