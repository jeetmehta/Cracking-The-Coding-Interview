# CTCI - Chapter 2: Linked Lists #
# Question 2.3
# PROBLEM STATEMENT: Implement an algorithm to delete a node in the middle 
# (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
# EXAMPLE - Input: the node c from the linked list a - >b- >c - >d - >e- >f. Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
# HINTS: #72

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.size = 0
		self.head = None

	def addNode(self, data):
		if (self.head == None):
			self.head = Node(data)
		else:
			temp = self.head
			while (temp.next != None):
				temp = temp.next
			temp.next = Node(data)
		self.size += 1

	def getNode(self, data):
		if (self.head == None):
			return None
		elif (self.head.data == data):
			return self.head
		else:
			temp = self.head
			while (temp != None and temp.data != data):
				temp = temp.next
			return temp
	# Delete middle node only with access to the node of interest
	# Copy value of next node over, and set the node's next pointer to next->next (basically copying and then deleting the one after it)
	# O(1) time, O(1) space
	def removeNodeInMiddle(self, node):
		temp = node.next
		node.data = temp.data
		node.next = temp.next
		self.size -= 1

	def printList(self):
		if (self.head != None):
			temp = self.head
			while (temp != None):
				print temp.data ,
				temp = temp.next
			print

# Main function - runs unit tests
def main():
	linked = LinkedList()
	numbers = [3, 5, 7, 6, 2]
	for num in numbers:
		linked.addNode(num)
	linked.printList()
	node = linked.getNode(7)
	linked.removeNodeInMiddle(node)
	linked.printList()


# Prevents file from running as import
if __name__ == "__main__":
	main()