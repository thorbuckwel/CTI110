# CTI 110
# P2T1 - Sales Prediction
# William Buckwell
# 1/16/18

def main():
    # Get total sales from user
    totalSales = int(input('What was your total sales? '))

    # Calculate annual profit
    annualProfit = totalSales * .23

    print('With your total sales of', '${:2}'.format(totalSales), ', the annual profit is ', '${:2}'.format(annualProfit))

main()
