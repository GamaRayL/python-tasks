from random import shuffle
from utils import load_questions, get_stats


def main():
    filename = "questions.json"
    questions = load_questions(filename)
    shuffle(questions)

    for question in questions:
        user_input = input(f"{question.build_question()}\n")
        question.user_answer = user_input

        if question.is_correct():
            question.user_points += question.diff_question * 10
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())

    get_stats(questions)


main()
