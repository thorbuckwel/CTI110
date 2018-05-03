# A running total program
# William Buckwell
# 3/25/18

def main():

	# start the running total to zero
    runningTotal = 0

    print('Program totals numbers until a negative number is entered')
	
	# Ask a user for a number and add it to total until they enter a negative number
    while True:
        number = int(input('Enter a number? '))

        if number < 0:
            break;
        else:
            runningTotal += number
	
	# Print the Totsl of all numbers entered
    print('Your total is:', runningTotal)
    

main()
