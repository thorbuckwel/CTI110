# Program takes 5 grade show letter grade then average grades
# 4/11/18
# CTI-110 P5HW1 - Test Average and Grade
# William Buckwell


def main():
    # instead of 5 test score we will use an accumlator varaible
    totalScore = 0

    # used to display the test number
    count = 1

    # loop through to get score from user and display the letter grade for each score
    for test in range(5):
        score = float(input('Enter score for test ' + str(count) + ': ' ))
        totalScore += score
        count += 1
        print('That test was an', determine_grade(score))

    # get the average for all test and display the average and letter grade
    final = cal_average(totalScore)
    print('The average of all the test is', final, 'which is an', determine_grade(final))

# determine the average from the passed totalScore
def cal_average(total):
    average = total / 5
    return average

# determine the letter grade from the passed score.
def determine_grade(score):

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

main()
