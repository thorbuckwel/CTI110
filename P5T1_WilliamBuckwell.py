# This program take kilometers and then displays it in miles format
# 4/11/18
# CTI-110 P5T1
# William Buckwell

# 
CONVERSION_FACTOR = 0.6214

# This main function get kilometers from the user and then passes it to
# the show_miles function.
def main():
    # Get the distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)


# This function converts kilometers into miles and then dispays the results
def show_miles(km):
    # Calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')
    
main()
