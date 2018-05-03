# CTI-110 
# P3HW1 - Age Classifier 
# William Buckwell
# 3/10/18

def main():

    # Get the person's age
    age = float(input('What is the person"s age?: '))

    # Determine type by age
    if age <= 1:
        print('The person is an infant.')
    elif age < 13:
        print('The person is a child.')
    elif age < 20:
        print('The person is a teenager.')
    else:
        print('The person is a adult.')

main()
