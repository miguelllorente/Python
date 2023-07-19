-- Simple code that features a menu screen bringing you the option to choose 4 games for a class final project

import random
while True:
    # Starting game menu.
    def main():
        print('<<<<<<<<Menu>>>>>>>>>>')
        print('[1] Display project information')
        print('[2] Lottery Number Generator')
        print('[3] Pig Latin')
        print('[4] Rock, Paper, Scissors Game')

    main()
    # User enters selection.
    game = int(input('Enter the number of your selection:'))

    # project information.
    def displayprojectinformation():
        print('Miguel Llorente')
        print('mxl1941@miami.edu')
        print('CSC 115')
        print('Economics Major')

    # lottery number generator.
    def lotterynumbergenerator():

        # Initialise an empty list that will be used to store the 6 lucky numbers.
        lotteryNumbers = []

        for i in range(0, 6):
            number = random.randint(1, 69)
            # Check if this number has already been picked.
            while number in lotteryNumbers:
                # if it has, pick a new number instead.
                number = random.randint(1, 69)

            # Append the unique number to the list.
            lotteryNumbers.append(number)

        # Sort the list in ascending order
        lotteryNumbers.sort()

    # modify final number with a range 1-26
        lotteryNumbers[-1] = random.randint(1, 26)

        # Display the list on screen:
        print(">>> Today's lottery numbers are: ")
        result = ','.join(str(item) for item in lotteryNumbers)
        print(result)

# pigLatin Game
    def pigLatin():


    # Reading user input from user
        userIP = input("\n English: ")

    # Word that holds Pig Latin form
        pigLatin = ""

    # Iterating over each word
        for word in userIP.split(" "):
    # Converting to pigLatin form and forming new sentence
            pigLatin = pigLatin + (word[1:] + word[0] + "ay").upper() + " "

    # Printing sentence in Pig latin form
        print("\n Pig Latin: " + pigLatin + " \n")



# rockPaperScissors Game.
    def rockPaperScissorsGame():
        print('Rock. Paper. Scissors.' '\n' 'Enter 1 for Rock, 2 for Paper or 3 for Scissors.', '\n')
        enter_player_answer()


    # Generate random integers.
    def generate_random_int():
        return random.randrange(1, 3)


    # Function that gets player choice with loop.
    def enter_player_answer():
        player = int(input('Enter your choice: '))
        # Input loop.
        while player != 1 and player != 2 and player != 3:
            print('Invalid entry. Please try again.')
            player = int(input('Enter 1, 2, or 3.: '))
        display_computer_answer(player)


    # Function that displays computer answer.
    def display_computer_answer(player):
        c_answer = generate_random_int()
        print('Computer picks: ', c_answer, '\n')
        determine_winner(c_answer, player)


    # Function that determines the winner.
    def determine_winner(c, p):
        if c == p:
            print('Play the Game Again.')
            enter_player_answer()
        elif c == 1 and p == 2:
            print('Paper wraps rock. Player wins!')
        elif c == 1 and p == 3:
            print('Rock smashes scissors. Computer Wins.')
        elif c == 2 and p == 1:
            print('Paper wraps rock. Computer Wins.')
        elif c == 2 and p == 3:
            print('Scissors cut paper. Player wins!')
        elif c == 3 and p == 1:
            print('Rock smashes scissors. Player wins!')
        elif c == 3 and p == 2:
            print('Scissors cut paper. Computer wins!')


# main menu options to choose each game.

    if game == 1:
        displayprojectinformation()
    elif game == 2:
        lotterynumbergenerator()
    elif game == 3:
        pigLatin()
    elif game == 4:
        rockPaperScissorsGame()
        # prompts user to either restart or end.
    check = input("Do you want to quit or start again? enter Y to restart or another key to end: ")
    if check.upper() == "Y":  # go back to the top.
        continue
    print("Bye")
    break  # exit

# main function.
if __name__=='__main__':
    main()
