# CTCI - Chapter 4: Trees and Graphs #
# Question 4.1
# PROBLEM STATEMENT: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
# HINTS: #127

class Node:
	def __init__(self, value = -1):
		self.data = value
		self.children = []

class DirectedGraph:
	def __init__(self, numNodes):
		self.nodes = []
		for i in range(0, numNodes):
			self.nodes.append(Node(i))
		self.numNodes = numNodes

	def addEdge(self, fromNode, toNode):
		self.nodes[fromNode].children.append(Node(toNode))

	def printGraph(self):
		for node in self.nodes:
			print node.data, ": ",
			for childNode in node.children:
				print childNode.data, " ",
			print

	def isConnected(self, node1, node2):

		# If the start node has no children -> return false (not connected to anything)
		start = self.nodes[node1]
		if (len(start.children) == 0):
			return False
		
		# BFS - Initialize queue and hash set
		queue = []
		visited = set([])

		# Load up queue with startNode's children
		queue += start.children
		visited.add(start.data)

		# Perform BFS until node has been found (or all options are exhausted)
		while (queue != []):
			currentChild = self.nodes[queue[0].data]
			queue.pop(0)
				
			# If we found what we're looking for -> return true
			if (currentChild.data == node2):
				return True
			# Make sure we havent' already seen this node
			elif (currentChild.data not in visited):
				visited.add(currentChild.data)
				queue += currentChild.children
				
		return False

# Main function - runs unit tests
def main():
	graph = DirectedGraph(7)
	edges = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 2), (4, 6), (6, 5), (5, 4)]

	for edge in edges:
		graph.addEdge(edge[0], edge[1])

	graph.printGraph()

	if (graph.isConnected(0, 4)):
		print "Nodes are connected"
	else:
		print "No connection between nodes"

# Prevents file from running as import
if __name__ == "__main__":
	main()