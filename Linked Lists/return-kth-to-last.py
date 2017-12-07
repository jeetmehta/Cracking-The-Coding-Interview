# CTCI - Chapter 2: Linked Lists #
# Question 2.2
# PROBLEM STATEMENT: Implement an algorithm to find the kth to last element of a singly linked list (assuming you don't know the size of the list).
# HINTS: #8, #25, #41, #67, #126

class Node:

	def __init__(self):
		self.data = 0
		self.next = None

class LinkedList:

	def __init__(self):
		self.size = 0
		self.head = None

	def addNode(self, data):
		if (self.head == None):
			self.head = Node()
			self.head.data = data
		else:
			temp = self.head
			while (temp.next != None):
				temp = temp.next

			temp.next = Node()
			temp.next.data = data
		self.size += 1

	def printList(self):
		if (self.head != None):
			temp = self.head
			while (temp != None):
				print temp.data,
				temp = temp.next
			print

	# Returns the kth to last element, having known the size of the list
	# O(n) time, O(1) space
	def getKthToLast(self, k):

		# Edge Case 1: K is too large (can't be greater than size)
		if (k > self.size):
			print "ERROR: K is larger than the size of the linked list"
			return None

		# Edge Case 2: K is too small/negative
		elif (k < 0):
			print "ERROR: K must be greater than or equal to zero"
			return None

		count = 0
		temp = self.head
		while (count != self.size - k and temp.next != None):
			temp = temp.next
			count += 1

		return temp

# Main function - runs unit tests
def main():

	linkedList = LinkedList()

	testInput = [2, 3, 5, 1, 3, 1, 9, 24, 3, 6, 1, 3]
	for num in testInput:
		linkedList.addNode(num)

	linkedList.printList()
	print linkedList.getKthToLast(0).data


# Prevents file from running as import
if __name__ == "__main__":
	main()