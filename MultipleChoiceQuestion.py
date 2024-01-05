from Question import Question


class MultipleChoiceQuestion(Question):
    def __init__(self, id, question_type, question_text, options, correct_option, is_active=True):
        super().__init__(id, question_type, question_text, options, is_active)
        self.correct_option = correct_option
        self.options = options
#question_type, question_text, options, correct_option)
        
    def get_correct_option(self):
        return self.correct_option

    def update_statistics(self, load_question_list, is_correct):
        super().update_statistics(load_question_list, is_correct)
        # Доп действия для MultipleChoiceQuestion

 
 
    def as_dict(self):
        return  {'id': id,#присваиваем порядковый номер в общем списке в файле, начиная с первого, 
                'question_type': self.question_type, 
                'question_text': self.question_text,
                'options': self.options,
                'correct_option': self.correct_option,
                'is_active': self.get_is_active()
                    }
    
