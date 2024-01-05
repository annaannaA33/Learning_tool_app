from Question import Question
import json
import datetime
from MultipleChoiceQuestion import MultipleChoiceQuestion
from FreeFormQuestion import FreeFormQuestion
from typing import Union
import os
import csv
from tabulate import tabulate
from datetime import datetime, date, time

class FileManager:
    def __init__(self):
        self.QUESTIONS_FILE = 'questions.csv'

    

    def save_questions_to_csv(self, new_question_list):
        existing_questions = []

        # Check if the questions file exists
        if os.path.exists(self.QUESTIONS_FILE) and os.stat(self.QUESTIONS_FILE).st_size != 0:
            # f the file exists and is not empty, load the questions
            existing_questions = self.load_questions_from_csv()

        # Merge old and new questions
        all_questions = existing_questions + new_question_list

        # Assign unique IDs
        for i, question in enumerate(all_questions, start=1):
            question.id = i

        # Save the updated list of questions to the file
        self.save_prepeared_questions_to_file(all_questions)
        

    def save_prepeared_questions_to_file(self, all_questions):
        with open(self.QUESTIONS_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'question_type', 'question_text', 'expected_answer', 'options', 'correct_option', 'is_active'])
            for question in all_questions:
                writer.writerow([question.id, question.question_type, question.get_question_text(),
                                 getattr(question, 'expected_answer', None), getattr(question, 'options', None),
                                 getattr(question, 'correct_option', None), question.get_is_active()])


    def load_questions_from_csv(self):
        # Load questions from the file
        question_list = []
        with open(self.QUESTIONS_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Create a question object and add it to the list
                if row['question_type'] == 'free_form_question_type':
                    question = FreeFormQuestion(
                        id=int(row['id']),
                        question_type=row['question_type'],
                        question_text=row['question_text'],
                        expected_answer=row['expected_answer'],
                        is_active=row['is_active'].lower() == 'true'
                    )
                elif row['question_type'] == 'multiple_choice_question_type':
                    question = MultipleChoiceQuestion(
                        id=int(row['id']),
                        question_type=row['question_type'],
                        question_text=row['question_text'],
                        options=row['options'],
                        correct_option=row['correct_option'],
                        is_active=row['is_active'].lower() == 'true'
                    )
                else:
                    # Handle other question types
                    question = None

                if question:
                    question_list.append(question)

        return question_list

    def print_questions_table(self, questions):
        # Prepare data for tabulation

        # Table header
        print("{:<5} {:<20} {:<10} {:<40} {:<10} {:<10} {:<15} {:<15} {:<15}".format(
            "ID", "Type", "Active", "Question", "Practice", "Test", "Correct %", "Total Shown", "Total Correct"))

        # Iterate through questions
        for question in questions:
            # Calculate the total number of times shown
            total_shown = question.practice_count + question.test_count

            # Calculate the percentage of correct answers
            correct_percentage = (question.correct_count / total_shown) * 100 if total_shown > 0 else 0

            # Display data in the table
            print("{:<5} {:<20} {:<10} {:<40} {:<10} {:<10} {:<15.2f} {:<15} {:<15}".format(
                question.id,
                question.question_type,
                "Yes" if question.is_active else "No",
                question.question_text,
                question.practice_count,
                question.test_count,
                correct_percentage,
                total_shown,
                question.correct_count))
        total_questions = len(questions)
        print(f"Total Questions: {total_questions}")

  
     # Question management mode: Enable/Disable/Delete questions
    def question_activity_control(self):
        question_list_print = []
        question_list_print = self.load_questions_from_csv()
        print("You are in the question activity management mode.")
        self.print_questions_table(question_list_print)

        while True:
            id_switch = input("Write the ID of the question you want to enable, disable, or delete (or 'main_menu' to return to the main menu): ")

            if id_switch.lower() == "main_menu":
                # Check for changes and save if there are any
                self.save_prepeared_questions_to_file(question_list_print)
                print("Changes have been successfully saved.")
                break

            try:
                id_switch = int(id_switch)
                selected_question = next((q for q in question_list_print if q.id == id_switch), None)

                if selected_question:
                    switch_command = input("Choose 'enable', 'disable', or 'delete': ")

                    if switch_command.lower() == "enable":
                        selected_question.is_active = True
                    elif switch_command.lower() == "disable":
                        selected_question.is_active = False
                    elif switch_command.lower() == "delete":
                        question_list_print.remove(selected_question)
                        print(f"Question with ID {id_switch} has been deleted.")
                        
                    else:
                        print("Invalid command. Please enter 'enable', 'disable', or 'delete'.")
                else:
                    print("Question not found. Enter a valid ID or 'main_menu' to return to the main menu.")
            except ValueError:
                print("Invalid input. Please enter a valid ID or 'main_menu' to return to the main menu.")
    
    def save_test_results(self, result_string):
        with open("results.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - {result_string}\n")

