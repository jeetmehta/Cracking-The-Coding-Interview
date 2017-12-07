# CTCI - Chapter 1: Arrays and Strings #
# Question 1.2
# PROBLEM STATEMENT: Given two strings, write a method to decide if one is a permutation of the other.
# HINTS: #1, #84, #122, #131

# Checks if two strings are permutations of each other using hash maps
def checkPermutations(firstString, secondString):

	firstHashMap = {}
	secondHashMap = {}

	for char in firstString:
		if char not in firstHashMap:
			firstHashMap[char] = 1
		else:
			firstHashMap[char] += 1

	for char in secondString:
		if char not in secondHashMap:
			secondHashMap[char] = 1
		else:
			secondHashMap[char] += 1

	if firstHashMap == secondHashMap:
		return True
	else:
		return False


# Main function - runs unit tests
def main():
	firstString = "xyzabcd"
	secondString = "bdaczx2"

	if (checkPermutations(firstString, secondString)):
		print "Strings are permutations of each other"
	else:
		print "Strings are not permutations"

# Prevents file from running as import
if __name__ == "__main__":
	main()