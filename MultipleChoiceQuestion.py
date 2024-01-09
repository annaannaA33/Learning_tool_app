from Question import Question
from random import shuffle


class MultipleChoiceQuestion(Question):
    def __init__(self, id, question_type, question_text, options, correct_option, is_active=True, appearance_count=0, correct_count=0, total_correct_percentage=0):
        super().__init__(id, question_type, question_text, is_active, appearance_count, correct_count, total_correct_percentage)
        self.correct_option = correct_option
        self.options = options
#question_type, question_text, options, correct_option)
        
    def get_correct_option(self):
        return self.correct_option

 
    def as_dict(self):
        return  {'id': self.id,
                'question_type': self.question_type, 
                'question_text': self.question_text,
                'options': self.options,
                'correct_option': self.correct_option,
                'is_active': self.get_is_active(),
                'appearance_count': self.appearance_count,
                'correct_count': self.correct_count,
                'total_correct_percentage': self.total_correct_percentage,
                 }
    
    def get_question_text(self):
        shuffled_options = [self.correct_option] + self.options
        shuffle(shuffled_options)
        return f"{super().get_question_text()}\nAnswer Options: {', '.join(shuffled_options)}"
