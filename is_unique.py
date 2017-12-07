# CTCI - Chapter 1: Arrays and Strings #
# Question 1.1
# PROBLEM STATEMENT: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# HINTS: #44, #117, #132

# Checks if a string has all unique characters using a set (don't need a count, just needs to check if it exists): O(n) where n = size of string
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

# Checks if a string has all unique characters iteratively, cross-checking every character against every other character: O(n^2) where n = size of string
def allUniqueCharactersNoDS(inputString):

	# Edge Case 1: Empty String
	if inputString == "":
		return True

	# Go through every character, and check against every other character in string
	for i, char in enumerate(inputString):
		for j, otherChar in enumerate(inputString):
			if (char == otherChar and i != j):
				return False

	# All characters are unique
	return True


# Main function - runs unit tests
def main():

	inputString = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+~`{;'<>?}|-./"
	print "----- Using Hash -------"
	if (allUniqueCharactersUsingHash(inputString)):
		print " String has all unique characters"
	else:
		print "String has repeated characters"

	print "------ No DS --------"
	if (allUniqueCharactersNoDS(inputString)):
		print " String has all unique characters"
	else:
		print "String has repeated characters"


# Prevents file from running as import
if __name__ == "__main__":
	main()