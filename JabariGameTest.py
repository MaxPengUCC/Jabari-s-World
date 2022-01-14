import art
word=art.text2art("Welcome To Jabari's World")
print (word) 
inp = input("Do you want to play? (y/n): ")
if "y" in inp.lower():
    print()
    print ("Ok great! Help Jabari get to the diving board by helping him gain confidence! You will be asked some Math and English questions, if you pass a level you will help Jabari gain confidence and increase the chances to help him jump off the diving board. Good Luck!")
    print()
    input("Type anything to start level one! If you want to restart, just restart the terminal!: ")
    print()
    validInput = False
    while validInput == False:
        command = input("Type a direction to move. Valid directions are NORTH(n), SOUTH(s), EAST(e), WEST(w). If you think you're ready you can also go to the Diving Board(db):  ")
        if "n" in command.lower():
            print()
            print ("You have moved north") 
            print()
            intOne = input("You see a small girl. Do you want to approach her? (y/n): ")
            print()
            if "y" in intOne.lower():
                questionOne = input("Hello, My name is Ling Ling! I think your not smart, prove me wrong... What's 9 + 11?: ")
                confidence = 0
                count = 0
                correct = False
                while correct == False and count <= 4:
                    if ("20" == questionOne.lower()) or ("twenty" in questionOne.lower()):
                        print()
                        print ("O M G you are so smart. Are you sure you're not a Mathematician?\n")
                        confidence += 1
                        print ("Jabari has gained +1 confidence")
                        print ("Your current confidence level is: ", confidence)
                        print()
                        correct = True
                    else:
                        if count < 4: 
                            print()
                            questionOne = input("Maybe I am right HAHA, I'll give you a few more tries... What's 9 + 11?: ")
                        else:
                            print()
                            print ("Ran out of tries lol. Try better next time ¯\_(ツ)_/¯")
                            print()
                            over=art.text2art("GAME OVER")
                            print (over)
                            validInput = True
                    count += 1
            else:
                print("You have gone back to your original position")
                print()
                validInput == False
        elif "e" in command.lower():
            print()
            print ("You have moved east")
            print()
            eastIntOne = input("You see your dad waving his arms to you, do you want to approach him?(y/n): ")
            print()
            if "y" in eastIntOne.lower():
                questionTwo = input("Hi Jabari its your Daddy! Have you been doing your English Homework? Let me test you! Name all the words in this sentence that should have capitals: john goes with his dog called spot to pizza nova: ")
                correct = False
                while correct == False and count <= 4:
                    if ("john" in questionTwo.lower()) and ("spot" in questionTwo.lower()) and ("pizza" in questionTwo.lower()) and ("nova" in questionTwo.lower()):
                        print()
                        print ("Good job son! Im pround of you!\n")
                        confidence += 1
                        print ("Jabari has gained +1 confidence")
                        print ("Your current confidence level is: ", confidence)
                        print()
                        correct = True
                    else:
                        if count < 4: 
                            print()
                            questionOne = input("Its ok son, I'll give you a few more tries.")
                        else:
                            print()
                            print ("I expected better from you... Do your homework next time Jabari!")
                            print()
                            over=art.text2art("GAME OVER")
                            print (over)
                        count += 1
            else:
                print("You move back. Your dad's face forms a sad expression as you walk away. You have gone back to your original position")
                print()
                validInput == False
        elif "w" in command.lower():
            print ("You have moved west")
            print()
            westIntOne = input("You find an iPad, on the bench. Do you want to open it?(y/n): ")
            print()
            if "y" in westIntOne.lower():
                questionThree = input("The iPad opens. A question appears on it. 'What is 16 - 4?': ")
                correct = False
                count = 0
                while correct == False and count <= 4:
                    if ("12" == questionThree.lower()) or ("twelve" in questionThree.lower()):
                        print()
                        print ("The iPad shifts into a new screen. 'Great Job Smarty Pants, you passed!'\n")
                        confidence += 1
                        print ("Jabari has gained +1 confidence")
                        print ("Your current confidence level is: ", confidence)
                        print()
                        correct = True
                    else:
                        if count < 4: 
                            print()
                            questionThree = input("Wrong! Try again:  ")
                        else:
                            print()
                            print ("Try again next time!")
                            print()
                            over=art.text2art("GAME OVER")
                            print (over)
                        count += 1
            else:
                print("You leave the iPad there. You have gone back to your original position.")
                print()
                validInput == False
        elif "s" in command.lower():
            print ("You have moved south")    
            print()
            southIntOne = input("You find a piece of paper on the floor. It seems to be a scavenger hunt, do you want to read the instructions?(y/n): ")
            print()
            if "y" in southIntOne.lower():
                questionFour = input("Find the verb in this sentence to figure out where to go next: I walk my dog everyday!: ")
                correct = False
                count = 0
                while correct == False and count <= 4:
                    if ("walk" == questionFour.lower()):
                        print()
                        southIntTwo = input("You walk forward and find an old woman. Do you want to approach her?(y/n): ")
                        print()
                        if "y" in southIntTwo.lower():
                            questionFive = input("Hi there sweetie! I see you have figured out the note I put. Now let me ask you this, I have 11 dollars, but then I give you 2 dollars. How much money do I have now?: ")
                            correct = False
                            count = 0
                            while correct == False and count <= 4:
                                if ("9" == questionFive) or ("nine" in questionFive.lower()):
                                    print()
                                    print ("Nice job sweetie, I knew you were smart the second I saw you! Here, take 2 dollars.\n")
                                    dollars = 2
                                    confidence =+ 1
                                    print ("Jabari has gained +1 confidence")
                                    print ("Your current confidence level is: ", confidence)
                                    print()
                                    print ("In you inventory you have:", dollars, "dollars")
                                    print()
                                    correct = True
                                else:
                                    if count < 4: 
                                        print()
                                        questionFive = input("That isn't quite right, I'll give you a few more tries honey: ")
                                    else:
                                        print()
                                        print ("I thought you were smart sweetie, better luck next time!")
                                        print()
                                        over=art.text2art("GAME OVER")
                                        print (over)
                                    count += 1
                    else: 
                        if count < 4: 
                            print()
                            questionFour = input("That doesn't seem to be right, try again!:  ")
                        else:
                            print()
                            print ("You gave up after too many tries.")
                            print()
                            over=art.text2art("GAME OVER")
                            print (over)
                            validInput = True
                        count += 1
            else:
                print("You leave the paper there.")
                print()
                validInput == False
        elif "db" in command.lower():
            divingInput = input("Are you sure you want to head to the diving board? If you fail the jump, all your progress will be lost!(y/n): ")
            if "y" in divingInput.lower():
                if confidence == 4:
                    print("Remembering all the words of confidence Jabari recieved, he takes a big leap of faith and jumps off the board.")
                    victory=art.text2art("YOU WIN!")
                    print (victory) 
            else:
                print("You back off the diving board. Maybe another time...")
                print()
                validInput == False
        else:
            print ("I do no recongnize that command. Try again!")
            print ()
else:
    print ()
    print ("Ok, rerun the code to play!")