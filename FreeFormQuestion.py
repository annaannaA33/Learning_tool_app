from Question import Question



class FreeFormQuestion(Question):
    def __init__(self, id, question_type, question_text, expected_answer, is_active=True):
        super().__init__(id, question_type, question_text, is_active)
        self.expected_answer = expected_answer


    def as_dict(self):
        
        return  {'id': self.id, #присваиваем порядковый номер в общем списке в файле, начиная с первого, 
                 'question_type': self.question_type, 
                 'question_text': self.question_text,
                 'expected_answer': self.expected_answer,
                 'is_active': self.get_is_active()
                 }
     
    
        
    

    
        
    
