def Game():
    import time
    import random
    username = input("Hello, My name is PB-Bot, What is your name?  ")
    userscore = 0
    AIscore = 0
    Want2Play = "Y"

    Gamelist = ["ROCK", "PAPER", "SCISSORS"]

    print ("Great!, Nice to meet you " + username )

    time.sleep(2)

    while (Want2Play =='Y'):
        Thechoice = random.choice(Gamelist)
        YesORNo = input ("Are you ready to play? Please input Y for yes and N for No (Please avoid Spaces) :  ")
        if YesORNo.upper() != 'Y' and YesORNo.upper() !=  'N':
                print ("I am sorry, I am not sure if i understand")
        elif YesORNo.upper()== "N":
            print ("Maybe Next Time")
            Want2Play = 0
            break
        else:
            print ("Lets get the game Starteeeed")
            time.sleep(2)
            userinput= input("Please choose Rock, Paper or Scissors : ")

            if userinput.upper() not in  Gamelist:
                print ("I am sorry, what you chose is not in the list please try again")
                
            elif userinput.upper() == Thechoice:
                print("It is a Tie, Try again")
            elif userinput.upper() == "ROCK":
                if Thechoice == "PAPER":
                    print ("HAHA I have won this round, I have picked Paper")
                    AIscore = AIscore +1
                    print (" My score is {}".format(AIscore))
                    print (" Your score is {}".format(userscore))
                if Thechoice == "SCISSORS":
                    print ("NOOOO I have lost this Round")
                    userscore = userscore +1
                    print (" My score is {}".format(AIscore))
                    print (" Your score is {}".format(userscore))
            elif userinput.upper() == "PAPER":
                if Thechoice == "SCISSORS":
                    print ("HAHA I have won this round, I have picked Scissors")
                    AIscore = AIscore +1
                    print (" My score is {}".format(AIscore))
                    print (" Your score is {}".format(userscore))
                if Thechoice == "ROCK":
                    print ("NOOOO I have lost this Round")
                    userscore = userscore +1
                    print (" My score is {}".format(AIscore))
                    print (" Your score is {}".format(userscore))
            elif userinput.upper() == "SCISSORS":
                if Thechoice == "ROCK":
                    print ("HAHA I have won this round, I have picked ROCK")
                    AIscore = AIscore +1
                    print (" My score is {}".format(AIscore))
                    print (" Your score is {}".format(userscore))
                if Thechoice == "PAPER":
                    print ("NOOOO I have lost this Round")
                    userscore = userscore +1
                    print (" My score is {}".format(AIscore))
                    print (" Your score is {}".format(userscore))
            
            
