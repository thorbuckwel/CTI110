# P2HW1
# Distance Traveled
# William Buckwell
# 3/10/18

def main():
    recLength1 = float(input('Length of the first rectangle: '))
    recWidth1 = float(input('Width of the first rectangle: '))
    recLength2 = float(input('Length of the second rectangle: '))
    recWidth2 = float(input('Width of the second rectangle: '))

    recArea1 = float(recLength1 * recWidth1)
    recArea2 = float(recLength2 * recWidth2)

    if recArea1 > recArea2:
        print('The first rectangle has the larger area.')
    elif recArea1 < recArea2:
        print('The second rectangle has the larger area.')
    else:
        print('They have the same size area.')

main()
