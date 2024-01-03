from Player import Player, welcome_player
from FileManager import FileManager
from QuestionManager import QuestionManager
from PracticeMode import PracticeMode


   
def main():
    player = Player()
    file_manager = FileManager()
    question_manager = QuestionManager()
    questions_list = question_manager.questions

    #user_data = file_manager.load_user_data()

    #if 'name' in user_data:
   #     player.name = user_data['name']
    welcome_player(player)
    main_manu(question_manager, file_manager)


def practice_mode():
    pass
    #practice = PracticeMode()
    #practice.start_practice()

def test_mode_menu(self):
    num_questions = int(input("Enter the number of questions for the test: "))
    self.test_mode(num_questions)


def main_manu(question_manager, file_manager):
    
    print("Welcome! Rules and instructions: The program will keep running until you choose to stop."
        "Program Usage:\n"
        "1. Adding Questions: Select '1' to add quiz or free-form text questions. Questions are saved for future sessions.\n"
        "2. View Statistics: Select '2' to see statistics for all questions, including ID, activity status, text, and performance percentages.\n"
        "3. Disable/Enable Questions: Select '3' to disable or enable specific questions by entering their ID.\n"
        "4. Practice Mode: Select '4' to practice questions. The program adapts, showing questions answered incorrectly more often.\n"
        "5. Test Mode: Select '5' to take a test. Choose the number of questions, and receive a score with percentages.\n"
        "Note: At least 5 questions must be added before entering practice or test modes.\n\n"
        "To stop the program and save data, type 'stop' anytime. All data is automatically saved. ")

    while True:
        player_choice = input("Enter your choice: ")
        if player_choice.lower() == 'stop':
            print("Exiting the program. Goodbye!")
            break
        elif player_choice == '1':
            new_question_list = []
            new_question_list = question_manager.add_question_menu()
            if len(new_question_list) > 0:
                file_manager.save_questions_to_csv(new_question_list)
                print(f"вы успешно добавили {len(new_question_list)} вопросов")
            else:
                print("You haven't saved any questions")
        #TODO              
        elif player_choice == '2':
            question_manager.view_statistics()
        elif player_choice == '3':   # Disable/Enable Questions
            #print the questions from json file manager
            file_manager.question_activity_control()
        elif player_choice == '4':
            practice_mode()
        elif player_choice == '5':
            #test_mode_menu()
            pass

        else:
            print("Invalid choice. Please choose a valid option.") 


if __name__ == "__main__":
    main()
    
            
    

      
        


