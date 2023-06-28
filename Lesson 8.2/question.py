class Question:
    def __init__(self, text_question, diff_question, correct_answer):
        self.text_question = text_question
        self.diff_question = int(diff_question)
        self.correct_answer = correct_answer

        self.has_question = False
        self.user_answer = None
        self.user_points = 0

    def __repr__(self):
        return "Класс вопроса"

    def get_points(self):
        return self.user_points

    def is_correct(self):
        return self.correct_answer == self.user_answer

    def build_question(self):
        return f"Вопрос: {self.text_question}\nСложность {self.diff_question}/5"

    def build_positive_feedback(self):
        return f"Ответ верный, получено {self.user_points}"

    def build_negative_feedback(self):
        return f"Ответ неверный, верный ответ {self.correct_answer}"
