import random
print("Welcome to Ultimate Ninja Battle Combat!!!")
name = input("Please enter your name: ", )
print("Welcome,", name)
print("Your current balance is $100")
finalBalance = []  # a list of player's balances


def getSelection(selection):  # This function will do the error handling for the game menu
    while selection.upper() not in ['I', 'P', 'Q']:
        print("""Error! Please choose again!
(I)nstructions
(P)lay game
(Q)uit game""")
        selection = input()
        getSelectionI(selection)
        getSelectionP(selection)
        getSelectionQ(selection)


def getSelectionI(selection): # This function will show the instructions of the game when the selection of player
                              # is I
    while selection.upper() == "I":
        print("""Welcome to Ultimate Ninja Battle Combat!!!
You will be fighting against the computer, and the winner gets bragging rights.
For each turn you will be asked to use one of the 6 attacks below:
(1) Punch of Fury
(2) Kick of Punishment
(3) Sword of Justice
(4) Shuriken of Vengeance
(5) Nunchucks of Anger
(6) Knife of Freedom
Choose wisely.""")
        if len(finalBalance)==0:
            print("Your current balance is $100")
        else:
            print("Your current balance if ${}".format(finalBalance[-1]))
        print("""Please choose from the following menu:")
(I)nstructions
(P)lay game
(Q)uit game""")
        selection = input()
        getSelection(selection)
        getSelectionP(selection)
        getSelectionQ(selection)


def getSelectionP(selection):  # This function will do the playing process and calculate balance for player when
                                # the selection of player is P
    if len(finalBalance) == 0:
        currentBalance = 100
    else:
        currentBalance = finalBalance[-1]
    newBalance=currentBalance  # The new balance will be the current balance in the next times played
    while selection.upper() == "P":
        if currentBalance == 0:
            print("Good bye {}. Your final balance is $0".format(name))
            print("""Your balance history is:
Starting Balance: $100""")
            for i in range(len(finalBalance)):
                print("After round {}: ${}".format(i + 1, finalBalance[i]))
            break
        else:
            print("Your current balance is ${}".format(newBalance))
            print("Please enter the amount to bet. All bets must be multiples of 5.")
            money = int(input())
            while money % 5 != 0 or money <= 0 or money > currentBalance:
                print("You choose to bet ${}".format(money))
                print("That is not a valid amount. You bet must be a multiple of 5, and be within your means")
                print("Your current balance is ${}".format(newBalance))
                print("Please enter the amount to bet. All bets must be multiples of 5.")
                money = int(input())
            else:
                print("You choose to bet ${}".format(money))
                print(name, ", you must choose one of the following attacks:")
                print("""(1) Punch of Fury
(2) Kick of Punishment
(3) Sword of Justice
(4) Shuriken of Vengeance
(5) Nunchucks of Anger
(6) Knife of Freedom""")
                number = input()
                while number not in ["1","2","3","4","5","6"] :
                    print("""Error! Please choose again!
(1) Punch of Fury
(2) Kick of Punishment
(3) Sword of Justice
(4) Shuriken of Vengeance
(5) Nunchucks of Anger
(6) Knife of Freedom""")
                    number = input()
                getPlayerChoose(number)
                randomNumber = random.randint(1,6)
                getComputerChoose(randomNumber)
                getResult1(number,randomNumber)
                getResult2(number,randomNumber)
                getResult3(number,randomNumber)
                getResult4(number,randomNumber)
                getResult5(number,randomNumber)
                getResult6(number,randomNumber)
                num_list1=[2,3,6]  #Those lists are the random numbers for winning or losing coditions, then attach it
                num_list2=[4,5]    #to each number to calculate the new balance
                num_list3=[3,4,6]
                num_list4=[1,5]
                num_list5=[1,2,6]
                num_list6=[3,4]
                num_list7=[1,2,5]
                if number=="1" and randomNumber in num_list1:
                    newBalance = currentBalance - money
                elif number == "1" and randomNumber in num_list2:
                    newBalance = currentBalance + money
                elif number == "2" and randomNumber in num_list3:
                    newBalance = currentBalance - money
                elif number == "2" and randomNumber in num_list4:
                    newBalance = currentBalance + money
                elif number =="3" and randomNumber in num_list5:
                    newBalance = currentBalance + money
                elif number=="3" and randomNumber in num_list2:
                    newBalance = currentBalance - money
                elif number=="4" and randomNumber in num_list4:
                    newBalance = currentBalance - money
                elif number=="4" and randomNumber in num_list1:
                    newBalance = currentBalance + money
                elif number=="5" and randomNumber in num_list5:
                    newBalance = currentBalance - money
                elif number=="5" and randomNumber in num_list6:
                    newBalance = currentBalance + money
                elif number=="6" and randomNumber in num_list7:
                    newBalance = currentBalance + money
                elif number == "6" and randomNumber in num_list6:
                    newBalance = currentBalance - money
                elif number==randomNumber:
                    newBalance=currentBalance
                print("Your current balance is ${}".format(newBalance))

                currentBalance=newBalance        # The new balance will be the current balance in the next times played
                finalBalance.append(newBalance)  # Store the new balance in the final balance list

                print("""Please choose from the following menu:
(I)nstructions
(P)lay game
(Q)uit game
            """)
                selection = input()
                getSelection(selection)
                getSelectionI(selection)
                getSelectionQ(selection)


def getSelectionQ(selection):  # This function will show player's final balance and player's balance history when
                               # the selection of player is Q
    if selection.upper() == "Q":
        if len(finalBalance)==0:
            print("Good bye {}. Your final balance is $100 ".format(name))
            print("""Your balance history is:
Starting Balance: $100""")
        else:
            print("Good bye {}. Your final balance is ${} ".format(name,finalBalance[-1]))
            print("""Your balance history is:
Starting Balance: $100""")
            for i in range(len(finalBalance)):
                print("After round {}: ${}".format(i+1, finalBalance[i]))


def getPlayerChoose(number):  # This function will attach the moves to each number from 1 to 6 which is
                              # player's choice
    if number == "1":
        print("{}, you chose: Punch of Fury".format(name))
    elif number == "2":
        print("{}, you chose: Kick of Punishment".format(name))
    elif number == "3":
        print("{}, you chose: Sword of Justice".format(name))
    elif number == "4":
        print("{}, you chose: Shuriken of Vengeance".format(name))
    elif number == "5":
        print("{}, you chose: Nunchucks of Anger".format(name))
    elif number == "6":
        print("{}, you chose: Knife of Freedom".format(name))


def getComputerChoose(randomNumber):  # This function will attach the moves to each random number from 1 to 6 which
                                      # is generated by computer
    if randomNumber == 1:
        print("The computer chose: Punch of Fury")
    elif randomNumber == 2:
        print("The computer chose: Kick of Punishment")
    elif randomNumber == 3:
        print("The computer chose: Sword of Justice")
    elif randomNumber == 4:
        print("The computer chose: Shuriken of Vengeance")
    elif randomNumber == 5:
        print("The computer chose: Nunchucks of Anger")
    elif randomNumber == 6:
        print("The computer chose: Knife of Freedom")


def getResult1(number,randomNumber):  # This function will show the result between player and computer when the
                                   # player’s choice is 1
    if number == "1" and randomNumber == 1:
        print("Tie No Winner")
    elif number == "1" and randomNumber == 2:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "1" and randomNumber == 3:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "1" and randomNumber == 4:
        print("Congratulations, you won {}".format(name))
    elif number == "1" and randomNumber == 5:
        print("Congratulations, you won {}".format(name))
    elif number == "1" and randomNumber == 6:
        print("Unfortunately, {}, you lost".format(name))


def getResult2(number,randomNumber):  # This function will show the result between player and computer when the
                                   # player’s choice is 2
    if number == "2" and randomNumber == 1:
        print("Congratulations, you won {}".format(name))
    elif number == "2" and randomNumber == 2:
        print("Tie No Winner")
    elif number == "2" and randomNumber == 3:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "2" and randomNumber == 4:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "2" and randomNumber == 5:
        print("Congratulations, you won {}".format(name))
    elif number == "2" and randomNumber == 6:
        print("Unfortunately, {}, you lost".format(name))


def getResult3(number,randomNumber):  # This function will show the result between player and computer when the
                                   # player’s choice is 3
    if number == "3" and randomNumber == 1:
        print("Congratulations, you won {}".format(name))
    elif number == "3" and randomNumber == 2:
        print("Congratulations, you won {}".format(name))
    elif number == "3" and randomNumber == 3:
        print("Tie No Winner")
    elif number == "3" and randomNumber == 4:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "3" and randomNumber == 5:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "3" and randomNumber == 6:
        print("Congratulations, you won {}".format(name))


def getResult4(number,randomNumber):  # This function will show the result between player and computer when the
                                   # player’s choice is 4
    if number == "4" and randomNumber == 1:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "4" and randomNumber == 2:
        print("Congratulations, you won {}".format(name))
    elif number == "4" and randomNumber == 3:
        print("Congratulations, you won {}".format(name))
    elif number == "4" and randomNumber == 4:
        print("Tie No Winner")
    elif number == "4" and randomNumber == 5:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "4" and randomNumber == 6:
        print("Congratulations, you won", name)


def getResult5(number,randomNumber):  # This function will show the result between player and computer when the
                                   # player’s choice is 5
    if number == "5" and randomNumber == 1:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "5" and randomNumber == 2:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "5" and randomNumber == 3:
        print("Congratulations, you won {}".format(name))
    elif number == "5" and randomNumber == 4:
        print("Congratulations, you won {}".format(name))
    elif number == "5" and randomNumber == 5:
        print("Tie No Winner")
    elif number == "5" and randomNumber == 6:
        print("Unfortunately, {}, you lost".format(name))


def getResult6(number,randomNumber):  # This function will show the result between player and computer when the
                                   # player’s choice is 6
    if number == "6" and randomNumber == 1:
        print("Congratulations, you won {}".format(name))
    elif number == "6" and randomNumber == 2:
        print("Congratulations, you won {}".format(name))
    elif number == "6" and randomNumber == 3:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "6" and randomNumber == 4:
        print("Unfortunately, {}, you lost".format(name))
    elif number == "6" and randomNumber == 5:
        print("Congratulations, you won {}".format(name))
    elif number == "6" and randomNumber == 6:
        print("Tie No Winner")


def main():  # This function will show the game menu and will be the backbone of the game
    print("""Please choose from the following menu:
(I)nstructions
(P)lay game
(Q)uit game""")
    selection = input()
    getSelection(selection)
    getSelectionI(selection)
    getSelectionP(selection)
    getSelectionQ(selection)
main()