# A program to conver feet to inches
# 4/11/18
# CTI-110 P5T2 - Feet to inches
# William Buckwell

# Constant for the number of inches per foot
INCHES_PER_FOOT = 12

# Main function
def main():
    # Get the number of feet from the user
    feet = int(input('Enter the number of feet: '))

    # Convert that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Call the main function
main()
