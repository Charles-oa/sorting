import utility
MenuSort = {1:'1.Ascending', 2:'2.Descending'}

numbers = []
maxNumbers = int(input('How many numbers to do you want to sort?: '))
print('Enter your ', maxNumbers, 'numbers. Hit enter to save')
numsEntered = 0

while numsEntered < maxNumbers:
    ReadNum = int(input('Enter your ' + str(numsEntered +1) + ' number: '))
    numbers.append (ReadNum)
    numsEntered = numsEntered +1
print('These are the numbers you entered: ',numbers)


countOfNums = len(numbers)
#print(countOfNums)
swaps = 1 # set to 1 to make the while statement run at least once
utility.PrintMenu('Sorting Modes', MenuSort)
sortChoice = int(input('Choose your sorting mode:'))

while swaps > 0:
    swaps = 0
    for numberIndex in range (countOfNums):
        if numberIndex == countOfNums - 1:
            break

        numA = numbers[numberIndex]
        numB = numbers[numberIndex + 1]
        if (sortChoice == 1 and numA > numB) or (sortChoice == 2 and numA < numB):
            numbers[numberIndex],numbers[numberIndex + 1] = numbers[numberIndex + 1], numbers[numberIndex]
            swaps += 1
                
if sortChoice == 1:
    print ('Sorted Numbers in ascending order are:', numbers)
else:
    print ('Sorted numbers in descending order are:', numbers)
    

    
