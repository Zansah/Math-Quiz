import random
import time

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])
    question = f"What is {num1} {operator} {num2}? "
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, answer

def run_quiz():
    print("You have ten questions to answer consisting of multiplication, subtraction and division\n")
    time.sleep(3)
    print("You may now begin")
    score = 0

    for i in range(1, 11):
        question, correct_answer = generate_question()
        print(f"Question {i}: {question}")
        start_time = time.time()
        user_answer = input("Your answer: ")
        end_time = time.time()

        time_taken = int(end_time - start_time)

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print(f"Correct! Time taken: {time_taken} seconds\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}. Time taken: {time_taken} seconds\n")

    print("Quiz completed!\n")
    time.sleep(2)
    print(f"Your final score is: {score}/10")

run_quiz()
