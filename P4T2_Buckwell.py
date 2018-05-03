# Bug collecter program
# William Buckwell
# 3/25/18

def main():

    # declare the accumalater for the total and a count variable
    totalBugs = 0
    day = 1

    # Tell user what the program is doing
    print('Program will keep a running total of bugs collect over 7 days!')

    # Loop through for 7 days
    while day <= 7:
        bugsCollected = int(input('How many bugs collect on day ' + str(day) + '?:'))
        totalBugs += bugsCollected

        print('Total Bugs collect is -', totalBugs)
        day +=1

main()
