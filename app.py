from Player import Player, welcome_player
from FileManager import FileManager
from QuestionManager import QuestionManager
from Question import Question
from random import choices
import os


def main():
  
    player = Player()
    file_manager = FileManager()
    question_manager = QuestionManager()   

    questions_list = question_manager.questions
    #user_data = file_manager.load_user_data()

    welcome_player(player)
    main_manu(question_manager, file_manager)
    

def __init__(self, load_question_list):
    self.load_question_list = load_question_list
    #if 'name' in user_data:
#     player.name = user_data['name']
    
def clear_terminal():
    # does not work
    print('\x1bc', end='')

def start_practice(active_questions_list):
    while True:
        print("You are in practice mode")
        one_question = Question.random_chose_question(active_questions_list)
        #print(one_question.get_question_text())
        if not one_question:
            print("No active questions available for practice.")
            break
        if len(active_questions_list) > 5:
            print("To start practicing, there should be at least 5 active questions. Please check the questions list.")
            break

        user_answer = input(f"{one_question.get_question_text()}:\n ")

        if user_answer.lower() == 'main_manu':
            # Save statistics and return to the main menu
            break
        elif one_question.check_answer(one_question, user_answer) == True:
            print("Answer is correct")
        else: 
            print("Answer is incorrect. Correct answer:", one_question.get_correct_answer())

        one_question.update_statistics()
        

        # In the end, return the list of questions with updated statistics after returning to the main menu. 
        #This list will be passed to the main file for updating and loading into the main CSV file

def check(questions_asked, active_questions_list):
        while True:
            one_question = Question.random_chose_question(active_questions_list)
            if one_question not in questions_asked:
                return one_question

def start_test(load_question_list, active_questions_list):
    correct = 0
    questions_asked = set()
    num_questions = 0
    print("You are in testing mode")
    
    while True:
        try:
            num_questions = int(input("Enter the number of questions for the test: "))
            if num_questions <= len(active_questions_list):
                break
        except ValueError:
            print("not anouth questions.")

        for _ in range(num_questions):
            while True:
                one_question = check(questions_asked, active_questions_list)
                questions_asked.add(one_question)
                user_answer = input(f"{one_question.get_question_text()}:\n ")

        if user_answer.lower() == 'main_menu':
            print("Testing mode aborted. Returning to the main menu.")
            break

        if one_question.check_answer(one_question, user_answer):
            correct += 1
            one_question.update_statistics(load_question_list, True)
        else: 
            one_question.update_statistics(load_question_list, False)

    # Display test results
    accuracy_percentage = (correct / num_questions) * 100 if num_questions > 0 else 0
    result_string = f"{accuracy_percentage:.2f}%"
    print(f"Test completed. Correct answers: {correct}/{num_questions} ({result_string})")
    return result_string



def print_ruls():
    print("Welcome! Rules and instructions: The program will keep running until you choose to stop."
        "Program Usage:\n"
        "1. Adding Questions: Select '1' to add quiz or free-form text questions. Questions are saved for future sessions.\n"
        "2. View Statistics: Select '2' to see statistics for all questions, including ID, activity status, text, and performance percentages.\n"
        "3. Disable/Enable Questions: Select '3' to disable or enable specific questions by entering their ID.\n"
        "4. Practice Mode: Select '4' to practice questions. The program adapts, showing questions answered incorrectly more often.\n"
        "5. Test Mode: Select '5' to take a test. Choose the number of questions, and receive a score with percentages.\n"
        "Note: At least 5 questions must be added before entering practice or test modes.\n\n"
        "To stop the program and save data, type 'stop' anytime. All data is automatically saved. ")
    
def print_menu():
    menu_options = [
        "1. Adding questions",
        "2. Statistics viewing",
        "3. Disable/enable questions",
        "4. Practice mode",
        "5. Test mode"
    ]

    max_length = max(len(option) for option in menu_options)

    print(f"+{'-' * (max_length + 2)}+")
    for option in menu_options:
        padding = (max_length - len(option)) // 2
        print(f"|{' ' * padding}{option}{' ' * (max_length - len(option) - padding)}|")
    print(f"+{'-' * (max_length + 2)}+")



def main_manu(question_manager, file_manager):
    print_ruls()
    
    while True:
        
        print_menu()
        player_choice = input("Enter your choice: ")
        if player_choice.lower() == 'stop':
            print("Exiting the program. Goodbye!")
            break

        # Add question, save question
        elif player_choice == '1':
            new_question_list = []
            new_question_list = question_manager.add_question_menu()
            if len(new_question_list) > 0:
                file_manager.save_questions_to_csv(new_question_list)
                print("The list of questions has been successfully updated")
            else:
                print("You haven't saved any questions")

        # Print the questions from file manager with statistics                
        elif player_choice == '2':
            load_question_list = []
            load_question_list = file_manager.load_questions_from_csv()
            file_manager.print_questions_table(load_question_list)
            
        # Disable/Enable Questions
        elif player_choice == '3':   
            #print the questions from file manager
            file_manager.question_activity_control()

        # Practice
        elif player_choice == '4':   
            load_question_list = []
            load_question_list = file_manager.load_questions_from_csv()
            active_questions_list = Question.find_active_questions(load_question_list)
            start_practice(active_questions_list)
            updated_load_question_list = load_question_list # with updated statistics
            # Get the updated list with statistics and update file with questions
            file_manager.save_questions_to_csv(updated_load_question_list)

        elif player_choice == '5':
            load_question_list = []
            load_question_list = file_manager.load_questions_from_csv()
            print(load_question_list)
            active_questions_list = Question.find_active_questions(load_question_list)
            print(active_questions_list)
            result_string = start_test(load_question_list, active_questions_list)

            updated_load_question_list = load_question_list 
            # Save results using FileManager
            file_manager.save_test_results(result_string)

            pass

        else:
            print("Invalid choice. Please choose a valid option.") 


if __name__ == "__main__":
    main()
    
            
