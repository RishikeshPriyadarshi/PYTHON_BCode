
   #1-D tuple for questions
questions = ("How many elements in the periodic table ?: ",
           "Which animal lays the largest egg ?: ",
           "What is the the most abundant gas  in the earth's atmosphere ?: ",
           "How many bones r there in the human body ?: ",
           "which planet in the solar system is the hottest ?: ")

  #2-D tuple for options
options = (("A.116", "B.117", "C.198", "D.118"),
           ("A.Whale", "B.Crocodile", "C.Elephant", "D.Ostrich"),
           ("A.Nitrogen", "B.Oxygen", "C.Carbon", "D.Sulphur"),
           ("A.206", "B.208", "C.209", "D.216"),
           ("A.Mercury", "B.Venus", "C.Earth", "D.Mars"))


answers = ("D","D","A","B","B")
guesses = []
score  =0
question_num = 0  #it is the index

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)  

    if guess == answers[question_num]:
        #then we will be increasing the score
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT:")
        print(f"{answers[question_num]} is the correct answer")     

    #incrementing the ques_num(i.e index ) for diffrent options for diffrent questons
    question_num +=1


       #beautifying  the Game
print("-------------------")
print("     RESULTS       ")
print("-------------------")


print("answers:", end="")
for answer in answers:
    print(answer, end=" ")

print("gusses:", end="")
for guess in guesses:
    print(guess, end=" ")

print()

score = int(score/len(questions) * 100)
print(f"Your score is {score}%")

