from random import choices


class Question:
    

    def __init__(self, id, question_type, question_text, is_active=True, appearance_count=0, correct_count=0, total_questions = 0):
        self.id = id 
        self.question_type = question_type
        self.question_text = question_text
        self.is_active = is_active
        self.appearance_count = appearance_count # How many times it has been displayed during testing + practice
        self.correct_count = correct_count  # Total number of correct answers for this question
        self.total_correct_percentage = 0  # Overall percentage of correct answers
        self.total_questions = 0 # Total number of questions
        

    def get_question_text(self):
        return self.question_text

    def get_is_active(self):
        return self.is_active
    
    def get_total_questions(self):
        return self.total_questions
    
    def get_weight(self):
        incorrect_attempts = self.appearance_count - self.correct_count
        return incorrect_attempts + 1 / (self.correct_count + 1)


    def update_statistics(self, load_question_list, is_correct):
        for idx, question in enumerate(load_question_list):
            if question.id == self.id:
                total_questions = len(load_question_list)
                question.total_correct_percentage = (question.correct_count / total_questions) * 100 if total_questions > 0 else 0
                # If the answer is correct, update statistics
                question.appearance_count +=1
                if is_correct:
                    question.correct_count += 1
                    question.total_correct_percentage = round((question.correct_count / total_questions) * 100) if total_questions > 0 else 0

                # Return the updated list of questions
                return load_question_list

        # If the question is not found, return the original list
        return load_question_list
    
    
    @classmethod
    def find_active_questions(cls, load_question_list):
        active_questions_list = [question for question in load_question_list if question.is_active]
        # Iterate through all questions and select the active ones 
        # adding them to the list
        return active_questions_list


    def check_answer(self, question, user_answer):
        if self.question_type == 'free_form_question_type':
            return user_answer.lower() == question.expected_answer.lower()
            
        elif self.question_type == 'multiple_choice_question_type':
            return user_answer.lower() == question.correct_option.lower()
        else:
            return True
        
    @classmethod
    def random_chose_question(cls, active_questions_list):
        if not active_questions_list:
            return None
        weights = [q.get_weight() for q in active_questions_list]
        randon_chosen_question = choices(active_questions_list, weights=weights, k=1).pop()
        return randon_chosen_question
        # randon_chose_question  = выбираем вопрос из active_questions_list выбранный по условию задачи. 
        # the questions are chosen in such a way that the questions that are answered correctly become less likely to appear, 
        # while questions that are answered incorrectly become more likely to appear. 
        # weighted random choices. 
        # The results of the statistics on correct answers should be stored
    
    def as_dict(self):
            return {
                'id': self.id,
                'question_type': self.question_type,
                'question_text': self.question_text,
                'is_active': self.is_active,
                'appearance_count': self.appearance_count,
                'correct_count': self.correct_count,
                'total_correct_percentage': self.total_correct_percentage,
            }
