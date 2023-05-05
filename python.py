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

answer =input("What is the name of Percy Jackson's sword? ")
if answer.lower() == "Riptide" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer =input("What was Catherine the Great's birth name? ")
if answer.lower() == "Sophie" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer =input("Which birds symbolize the Norse god Odin? ")
if answer.lower() == "Ravens" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer =input("What is the name of the caterpillar squishmallow? ")
if answer.lower() == "Rutabaga" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer =input("What is the name of the full moon in March? ")
if answer.lower() == "The worm moon" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer =input("Who wrote Swan Lake? ")
if answer.lower() == "Tchaikovsky" :
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")

print("You got " + str((score/10) * 100) + "%. Excelsior!")