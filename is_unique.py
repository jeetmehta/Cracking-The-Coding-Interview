# CTCI - Chapter 1: Arrays and Strings #
# Question 1.1
# PROBLEM STATEMENT: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# HINTS: #44, #117, #132

# Check if a string has all unique characters using a set (don't need a count, just needs to check if it exists)
def allUniqueCharactersUsingHash(inputString):
	
	# Edge Case 1: Empty String
	if inputString == "":
		return True
	
	# Initialize hash set
	hashSet = set([])	

	# Add unique string characters to set
	for char in inputString:
		if (char in hashSet):
			return False
		else:
			hashSet.add(char)

	# All characters are unique
	return True

# Main function - runs unit tests
def main():

	inputString = ""
	if (allUniqueCharactersUsingHash(inputString)):
		print "Using Hash: String has all unique characters"
	else:
		print "Using Hash: String has repeated characters"

# Prevents file from running as import
if __name__ == "__main__":
	main()