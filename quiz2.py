
# create tupples list for the questions and answers
questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
c_answer = []
# Initialize the user's score.
score = 0
question_num = 0

# Present each questions
for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

#update the user's score.
    guess = input("Enter (A, B, C, D): ").upper()
    c_answer.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("      YOUR RESULTS    ")
print("----------------------")

# Display the correct answers.
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

# Display the correct answers.
print("correct_answers: ", end="")
for guess in c_answer:
    print(guess, end=" ")
print()

# Display the final score.
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
