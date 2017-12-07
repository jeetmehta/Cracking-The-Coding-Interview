# CTCI - Chapter 2: Linked Lists #
# Question 2.1
# PROBLEM STATEMENT: Write code to remove duplicates from an unsorted linked list. 
# How would you solve this problem if a temporary buffer is not allowed?
# HINTS: #9, #40

# Basic node class
class Node:

	def __init__(self):
		self.data = 0
		self.next = None

# Linked list class description
class LinkedList:

	# Constructor
	def __init__(self):
		self.size = 0
		self.head = None

	# Add node to list
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

	# Prints list values
	def printList(self):
		if (self.head != None):
			temp = self.head
			while (temp != None):
				print temp.data,
				temp = temp.next
			print

	# Removes all duplicates using a hash set (keeps only one unique instance)
	def removeDuplicates(self):
		if (self.head != None):
			
			# Declare hash set		
			hashSet = set([])
			
			# Initialize iterators (current + previous)
			temp = self.head
			previous = temp

			# Iterate through list looking for and removing duplicates
			while (temp != None):
				if temp.data in hashSet:
					previous.next = temp.next # should be deleting the node?
					self.size -= 1
				else:
					hashSet.add(temp.data)
					# Increment previous pointer only if no duplicates are found
					previous = temp
				
				# Increment temp
				temp = temp.next

# Main function - runs unit tests
def main():

	testInput = [0, 0, 0]
	linkedList = LinkedList()

	for num in testInput:
		linkedList.addNode(num)
	
	linkedList.printList()
	linkedList.removeDuplicates()
	linkedList.printList()

# Prevents file from running as import
if __name__ == "__main__":
	main()