# CTCI - Chapter 3: Stacks and Queues #
# Question 3.1
# PROBLEM STATEMENT: Describe how you could use a single array to implement three stacks.
# HINTS: #2, #12, #38, #58

# MY ANSWER
# You basically split up the array into three segments, with a "top" pointer/index for each third
# IE: arary: [][][][][][][][][][][][][][]
# Pointers:  top1     top2     top3

# If the array is mutable, it's easy since you can insert/delete at those specific positions.
# If the array isn't mutable, you assign/declare each stack to have a fixed capacity/max size (size of the third)
# Then, you can just move the respective top pointer up/down depending on a push/pop. You never actually have to remove values