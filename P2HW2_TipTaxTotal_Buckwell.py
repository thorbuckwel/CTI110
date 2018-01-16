# CTI-110
# P2HW2 - Tip, Tax, and Total
# William Buckwell
# 1/16/18

def main():
    # Define constant varabiles
    tipAmount = .18
    salesTax = .07

    # Define changing varabiles
    totalCost = 0
    totalTax = 0
    totalTip = 0
    subTotal = 0

    # Get food cost from user
    foodCost = float(input('What was the total food cost? '))

    # Calculate tax, subTotal, totalTip, and totalCost
    totalTax = foodCost * salesTax
    subTotal = foodCost + totalTax
    totalTip = subTotal * tipAmount
    totalCost = subTotal + totalTip

    # Display all cost
    print('Your food total was', '${:0.2f}'.format(foodCost))
    print('The taxes are', '${:0.2f}'.format(totalTax))
    print('The SubTotal is', '${:0.2f}'.format(subTotal))
    print('The tip should be', '${:0.2f}'.format(totalTip))
    print('Leaving the total of', '${:0.2f}'.format(totalCost))
main()
