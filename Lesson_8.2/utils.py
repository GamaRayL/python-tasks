import json
from question import Question


def load_questions(filename):
    with open(filename, encoding="utf-8") as file:
        date = json.load(file)

    questions = []
    for item in date:
        questions.append(Question(item["q"], item["d"], item["a"]))

    return questions


def get_stats(questions):
    total_score = 0
    total_answers = 0
    total_questions = 0
    for item in questions:
        total_score += item.user_points
        total_questions += 1

        if item.user_points > 0:
            total_answers += 1

    return f"Вот и всё!" \
           f"Отвечено {total_answers} вопроса из {total_questions}" \
           f"Набрано баллов: {total_score}"
