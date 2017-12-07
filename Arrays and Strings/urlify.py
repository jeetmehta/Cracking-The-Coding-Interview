# CTCI - Chapter 1: Arrays and Strings #
# Question 1.3
# PROBLEM STATEMENT: Write a method to replace all spaces in a string with '%20: 
# You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. 
# (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
# HINTS: #53, #118

# Replaces spaces in a string with %20
# O(n) time, O(1) space
def urlify(inputString):
	return inputString.replace(" ", "%20")

# Main function - runs unit tests
def main():
	inputString = "hello this is me testing whether this method actually works or not. Clearly it does."

	print urlify(inputString)

# Prevents file from running as import
if __name__ == "__main__":
	main()