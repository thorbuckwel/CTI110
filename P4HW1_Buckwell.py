# Distance traveled program
# William Buckwell
# 3/25/18

def main():

	# Get the users Spped and Time
    speed = int(input('How fast where you traveling?: '))
    time = int(input('How many hours at that speed?: '))
    
	# Declare counting variable
	hour = 1

    print('HOUR', '\t', 'Distance')
    
	# Calculate and display distance every hour.
	while hour <= time:
        distance = speed * hour
        print(hour, '\t', distance, 'miles')
        hour += 1


main()
