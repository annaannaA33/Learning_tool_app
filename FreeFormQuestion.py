from Question import Question



class FreeFormQuestion(Question):
    def __init__(self, id, question_type, question_text, expected_answer, is_active=True, appearance_count=0, correct_count=0, total_correct_percentage=0):
        super().__init__(id, question_type, question_text, is_active, appearance_count, correct_count, total_correct_percentage)
        self.expected_answer = expected_answer


    def as_dict(self):
        
        return  {'id': self.id, #присваиваем порядковый номер в общем списке в файле, начиная с первого, 
                 'question_type': self.question_type, 
                 'question_text': self.question_text,
                 'expected_answer': self.expected_answer,
                 'is_active': self.get_is_active(),
                'appearance_count': self.appearance_count,
                'correct_count': self.correct_count,
                'total_correct_percentage': self.total_correct_percentage,
                 }
     
    
        
    
