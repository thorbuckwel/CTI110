# Factorial program
# William Buckwell
# 3/25/18

def main():

	# Get the user number then start a count variable and the factorial number to 1
    num = int(input('Please enter a non-negative integer:'))
    count = 1
    factorial = 1
	
	# Calculate the user number to the factorial number
    while count <= num:
        factorial = factorial * count
        count += 1
	
	# Print the factorial number
    print('The factorial of', num, 'is', factorial)



main()
