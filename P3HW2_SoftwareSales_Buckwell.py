# CTI-110 
# P3HW1 - Software Sales 
# William Buckwell
# 3/10/18

def main():

    # Get amount from the user
    amount = float(input('Enter the amount you would like?: '))

    # Get the base cost before discounts
    baseCost = amount * 99

    if amount < 10:
        print('Total Cost $' + str(baseCost))
    elif 10 <= amount < 20:
        discountedPrice = baseCost*.9
        print('Before discount the cost is $' + str(baseCost))
        print('Your discount is 10%')
        print('You total cost is $' + str(round(discountedPrice,2)))
    elif 20 <= amount < 50:
        discountedPrice = baseCost*.8
        print('Before discount the cost is $' + str(baseCost))
        print('Your discount is 20%')
        print('You total cost is $' + str(round(discountedPrice,2)))
    elif 50 <= amount < 100:
        discountedPrice = baseCost*.7
        print('Before discount the cost is $' + str(baseCost))
        print('Your discount is 30%')
        print('You total cost is $' + str(round(discountedPrice,2)))
    else:
        discountedPrice = baseCost*.6
        print('Before discount the cost is $' + str(baseCost))
        print('Your discount is 40%')
        print('You total cost is $' + str(round(discountedPrice,2)))



main()
