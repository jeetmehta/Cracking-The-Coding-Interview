# CTCI - Chapter 3: Stacks and Queues #
# Question 3.3
# PROBLEM STATEMENT: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should 
# create a new stack once the previous one exceeds capacity. 
# SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
# (that is, pop ( ) should return the same values as it would if there were just a single stack).
# FOLLOW UP - Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
# HINTS: #27, #59, #78

# Basic stack class
class Stack:

	def __init__(self):
		self.size = 0
		self.stack = []

	def push(self, value):
		self.stack.append(value)
		self.size += 1

	def top(self):
		return self.stack[-1]

	def pop(self):
		self.stack.pop()
		self.size -= 1

	def size(self):
		return self.size

# Implementation for the set of stacks
class SetOfStacks:

	def __init__(self, capacity):
		self.capacity = capacity
		self.set = [Stack()]
		self.numStacks = 1

	def push(self, value):
		for stack in self.set:
			# If stack isn't full -> normal push
			if stack.size < self.capacity:
				stack.push(value)
				return
			# If stack is full, either try the next stack or if it's the last one, add a new stack to the set
			elif stack.size == self.capacity:
				if (stack == self.set[-1]):
					newStack = Stack()
					newStack.push(value)
					self.set.append(newStack)
					self.numStacks += 1
					return

	def top(self):
		if (self.numStacks > 0):
			return self.set[-1].top()
		else:
			print "ERROR: Set is empty"

	def pop(self):
		# Empty set
		if (self.numStacks == 0):
			print "ERROR: Set is empty"
		# Remove a value from the last stack in the set -> if it's empty after removing, get rid of the stack completely
		else:
			self.set[-1].pop()
			if (self.set[-1].size == 0):
				self.set.pop()
				self.numStacks -= 1

	def printStack(self):
		count = 1
		for stack in self.set:
			print "Stack #: ", count
			print stack.stack
			count += 1


# Main function - runs unit tests
def main():
	
	setOfStacks = SetOfStacks(5)
	testInput = [2, 4, 5, 12, 124, 24, 35,35, 53,531,5,531,531 ,5,3,5 ,53,53,5, 6, 4,6,46,64,26,6,26,8,7686,4,253,1,134,45,35]
	for num in testInput:
		setOfStacks.push(num)

	setOfStacks.printStack()
	print "------- POPPING VALUES NOW ------"
	for i in range(0, 35):
		setOfStacks.pop()
		setOfStacks.printStack()


# Prevents file from running as import
if __name__ == "__main__":
	main()