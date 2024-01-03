from random import shuffle
from MultipleChoiceQuestion import MultipleChoiceQuestion


class TestMode:


    

    def start_test(self, num_questions, questions_list):
        active_questions = [q for q in questions_list if q.is_active]
        if len(active_questions) < num_questions:
            print("Not enough active questions for the test.")
            return 
