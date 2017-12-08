# CTCI - Chapter 3: Stacks and Queues #
# Question 3.2
# PROBLEM STATEMENT: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.
# HINTS: #27, #59, #78

# MY ANSWER
# Declare another stack to keep track of mins. Every time you push onto the main stack, you check if pushValue < top(minStack).
# If it is, push it to both mainStack and minStack. Every time you pop, you check if popValue == top(minStack)
# If it is, you pop from both mainStack and minStack
# Edge cases: If minStack is empty (in the begining), you push the first/any value (first value == min)