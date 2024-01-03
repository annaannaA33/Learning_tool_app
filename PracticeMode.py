from random import choices
from MultipleChoiceQuestion import MultipleChoiceQuestion

class PracticeMode:
    def __init__(self, question_manager):
        self.question_manager = question_manager

    def start_practice(self):
        while True:
            question = self.select_question()
            if not question:
                print("No active questions available for practice.")
                break

            user_answer = input(f"Practice Mode - {question.get_question_text()}: ")
            if user_answer.lower() == 'stop':
                break

            is_correct = self.check_answer(question, user_answer)
            question.practice_count += 1
            question.update_statistics(is_correct)

    def select_question(self):
        active_questions = [q for q in self.question_manager.questions if q.is_active]
        return choices(active_questions, k=1).pop() if active_questions else None

    def check_answer(self, question, user_answer):
        if isinstance(question, MultipleChoiceQuestion):
            try:
                user_answer_index = int(user_answer) - 1
                return user_answer_index == question.get_correct_option()
            except ValueError:
                return False
        else:
            return user_answer.lower() == question.get_answer().lower()
