from module import *
import random 

def main():
    print('Let the Race begin')
    print('\n * * The first car to 50 wins * *')

    mycar = Model_1()

    print('Your car is Model 1 and the color is {}'.format(mycar.getColor()))

    mycar.soundHorn()

    computerCar = Model_2()
    print('\nThe computer\'s car is Model 2 and the color is {}'.format(computerCar.getColor()))
    computerCar.soundHorn()

    while mycar.getDistance() < 50 and computerCar.getDistance() < 50:
        distance = random.randint(1,5)
        line = mycar.showLine(distance)
        print('(%s) %s> (%d)' %(mycar.getColor(),line,mycar.getDistance()))
        distance = random.randint(1,5)
        line = computerCar.showLine(distance)
        print('(%s ) %s> (%d)' %(computerCar.getColor(),line,computerCar.getDistance()))
    
        if mycar.getDistance() < 50 and computerCar.getDistance() < 50:
            choice = input('Drive some more? (y/n): ')
            if choice == 'n':
                break
    
    if mycar.getDistance() >=50:
        print('You Win!')
    elif computerCar.getDistance() >=50:
        print('Computer wins!')


if __name__ == '__main__':
    main()
