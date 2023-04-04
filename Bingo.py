import random

rangeBetweenLetters = 15
offset = 1
columns = 5


def printGameChoices():
    print()
    print("Enter number to choose of the following Bingo game choices: ")
    print("75 Ball Bingo:")
    print("Enter 1 for Four corners\nEnter 2 for Outer edge\nEnter 3 for Full house\nEnter 4 for Row\nEnter 5 for Column\nEnter 6 for Letter\nEnter 7 for Diagonal\n")


def winColumn(bingoCard):
    for i in range(columns):
        isAllMarked = True
        for j in range(columns):
            if bingoCard[j][i] != 'X':
                isAllMarked = False
                break
        if isAllMarked:
            return True
    return False


def winRow(bingoCard):
    markedColumn = ['X'] * columns
    for row in bingoCard:
        if row == markedColumn:
            return True
    return False


def winDiagonal(bingoCard):
    i = 0
    j = 0
    while (i < columns):
        if bingoCard[i][j] != 'X':
            return False
        i += 1
        j += 1
    # print("BINGO!")
    return True


def winFourCorners(bingoCard):
    if bingoCard[0][0] == 'X' and bingoCard[4][4] == 'X' and bingoCard[0][4] == 'X' and bingoCard[4][0]:
        # print("BINGO!")
        return True
    return False


def winOuterEdge(bingoCard):
    markedLine = ['X'] * columns
    if bingoCard[0] != markedLine:
        return False
    if bingoCard[4] != markedLine:
        return False
    for j in range(columns):
        if bingoCard[j][0] != 'X':
            return False
    for j in range(columns):
        if bingoCard[j][4] != 'X':
            return False
    return True


def winFullHouse(bingoCard):
    markedLine = ['X'] * columns
    for row in bingoCard:
        if row != markedLine:
            return False
    return True


def winLetter(bingoCard):
    # for letter L
    for i in range(columns):
        if bingoCard[i][0] != 'X':
            return False
    if bingoCard[4] != ['X'] * columns:
        return False
    return True


def generateBingoBall(generatedBalls):
    bingo = "BINGO"
    letterIndex = random.randint(0, 4)
    letter = bingo[letterIndex]
    number = random.randint(rangeBetweenLetters * letterIndex +
                            offset, rangeBetweenLetters * (letterIndex + offset))
    while number in generatedBalls:
        letterIndex = random.randint(0, 4)
        letter = bingo[letterIndex]
        number = random.randint(rangeBetweenLetters * letterIndex +
                                offset, rangeBetweenLetters * (letterIndex + offset))

    return letter, number


def printBingoCard():
    print('B   I   N   G   O')
    for i in range(columns):
        for j in range(columns):
            print("{:<3}".format(bingoCard[j][i]), end=' ')
        print()
    print()


def chooseGame():
    while True:
        try:
            printGameChoices()
            userChoice = int(input('Enter a number: '))
            if userChoice not in [1, 2, 3, 4, 5, 6, 7]:
                print('INVALID! You need to enter a number from the list')
                continue
            return userChoice
        except ValueError:
            print('INVALID! You need to enter a number')
            continue


def isDone():
    while True:
        userChoice = input(
            "Enter \"continue\" to continue and \"done\" to finish the game: ")
        if userChoice == "done":
            return True
        if userChoice == "continue":
            return False
        if userChoice not in ["continue", "done"]:
            print("INVALID! You need to enter either \"continue\" or \"done\"")
            continue


gameMode = {1: winFourCorners, 2: winOuterEdge,
            3: winFullHouse, 4: winRow, 5: winColumn, 6: winLetter, 7: winDiagonal}

userGameChoice = chooseGame()

bingoCard = []
checkIfDone = isDone()
if not checkIfDone:
    bingoCard = [[0 for i in range(columns)] for j in range(columns)]
    import random
    for i in range(columns):
        bingoCard[i] = random.sample(range(
            i * rangeBetweenLetters + offset, (i + offset) * rangeBetweenLetters), columns)

    printBingoCard()

    numberOfCalls = 0

generatedBalls = []

checkIfWin = False

while not checkIfDone:
    if checkIfDone:
        print("L + RATIO")
        break

    checkIfWin = gameMode[userGameChoice](bingoCard)
    if checkIfWin:
        print('BINGO!!!')
        break

    if numberOfCalls > 75:
        print("L + RATIO")
        break

    bingoCallLetter, bingoCallNumber = generateBingoBall(generatedBalls)
    generatedBalls.append(bingoCallNumber)
    print(generatedBalls)
    print("Bingo Call: ", bingoCallLetter, bingoCallNumber)
    numberOfCalls += 1

    # with open("bingoballs.txt", 'a') as out_file:
    #     out_file.write(bingoCallLetter, end=' ')
    #     out_file.write(str(bingoCallNumber), end='\n')

    for i in range(columns):
        for j in range(columns):
            if bingoCard[j][i] == bingoCallNumber:
                bingoCard[j][i] = 'X'
                print("You have it!\n")
                printBingoCard()

    print(f'{numberOfCalls = }')

    checkIfDone = isDone()
