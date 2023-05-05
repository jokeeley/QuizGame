print("Welcome to Jo's Trivia!")

playing = input("Do you want to play? " )

if playing.lower() != "yes": 
    quit()

print ("Okay! Let's Play!" )
score = 0

answer =input("Who was the main antagonist of Animorphs? ")
if answer.lower() == "Visser Three" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer =input("What was the goat's name in The Witch? ")
if answer.lower() == "Black Phillip" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer =input("Who is Monster Zero in the Godzilla franchise? ")
if answer.lower() == "King Ghidorah" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer =input("What is the name above Winnie the Pooh's house? ")
if answer.lower() == "Sanders" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")

print("You got " + str((score/4) * 100) + "%. Excelsior!")