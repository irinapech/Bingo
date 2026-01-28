#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define FILENAMESIZE 10
#define NUMBEROFBALLS 20

struct bingoBall
{
    char letter;
    int number;
};

struct bingoBall generateBingoBall()
{
    struct bingoBall newBall;
    static char bingoLetters[] = {'B', 'I', 'N', 'G', 'O'};
    
    newBall.letter = bingoLetters[rand() % 5];
    newBall.number = rand() % 75 + 1;

    return newBall;
}

void printBingoBall(struct bingoBall ball)
{
    printf("%c %d\n", ball.letter, ball.number);
}

bool validateBingoBall(struct bingoBall ball)
{
    int rangeBetweenLetters = 15, offset = 1, bingoLength = 5, index;

    static char bingoLetters[] = {'B', 'I', 'N', 'G', 'O'};

    for (int i = 0; i < bingoLength; i++)
    {
        if (ball.letter == bingoLetters[i])
        {
            index = i;
        }
    }

    if (ball.number >= index * rangeBetweenLetters + offset 
        && ball.number <= (index + offset) * rangeBetweenLetters)
    {
        return true;
    }

    return false;
}

bool checkForDuplicates(struct bingoBall ball, char bingoLetters[], int bingoNumbers[], int numberOfBingoCalls)
{
    for (int i = 0; i < numberOfBingoCalls; i++)
    {
        if (ball.letter == bingoLetters[i] && ball.number == bingoNumbers[i])
        {
            return true;
        }
    }
    return false;
}

int main(int argc, char *argv[])
{
    if (argc == 1)
    {
        printf("____blank____\n");
    }
    else
    {
        FILE *infp = fopen(argv[1], "w+");
        srand(time(NULL));

    int bingoNumbers[NUMBEROFBALLS];
    char bingoLetters[NUMBEROFBALLS];

    int numberOfBingoCalls = 0;
    while (numberOfBingoCalls < NUMBEROFBALLS)
    {
        struct bingoBall newBall = generateBingoBall();
        printBingoBall(newBall);
        
        if (validateBingoBall(newBall) 
            && !checkForDuplicates(newBall, bingoLetters, bingoNumbers, numberOfBingoCalls))
        {
            bingoLetters[numberOfBingoCalls] = newBall.letter;
            bingoNumbers[numberOfBingoCalls] = newBall.number;
            fprintf(infp, "%c %d\n", newBall.letter, newBall.number);
            numberOfBingoCalls++;
        }
    }
    }
}