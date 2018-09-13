from random import *

def randomNumber(amount):
    listOfNumbers = []
    for i in range(amount):
        number = randint(1,100)
        listOfNumbers.append(number)
    print(listOfNumbers)
    
        
def main():
    question = int(input('How many numbers are you needing? '))
    randomNumber(question)
    
main()