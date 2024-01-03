import datetime


class Question:

    

    def __init__(self, id, question_type, question_text, is_active=True, practice_count=0, test_count=0, correct_count=0, total_questions = 0):
        self.id = id # геренируется просто по порядку
        self.question_type = question_type
        self.question_text = question_text
        self.is_active = is_active
        self.practice_count = practice_count   #сколько раз он отображался во время практики
        self.test_count = test_count    #сколько раз он отображался во время тестирования
        self.correct_count = correct_count   #процент правильных ответов на данный вопрос общий
        self.total_correct_percentage = 0  # 
        self.total_questions = 0 # обшее количество вопросов
        

    def get_question_text(self):
        return self.question_text

    def get_is_active(self):
        return self.is_active
    
    def get_total_questions(self):
        return self.total_questions

    def update_statistics(self, is_correct):
        # Method to update statistics based on whether the question was answered correctly
        self.total_questions += 1
        if is_correct:
            self.correct_count += 1
        self.total_correct_percentage = (self.correct_count / self.total_questions) * 100 if self.total_questions > 0 else 0    

def as_dict(self):
        return {
            'id': self.id,
            'question_type': self.question_type,
            'question_text': self.question_text,
            'is_active': self.is_active,
            'practice_count': self.practice_count,
            'test_count': self.test_count,
            'correct_count': self.correct_count,
            'total_correct_percentage': self.total_correct_percentage,
            'total_questions': self.total_questions
        }
