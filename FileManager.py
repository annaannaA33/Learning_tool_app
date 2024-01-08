from Question import Question
import datetime
from MultipleChoiceQuestion import MultipleChoiceQuestion
from FreeFormQuestion import FreeFormQuestion
from typing import Union
import os
import csv
from tabulate import tabulate
from colorama import Fore, Style


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
            writer.writerow(['id', 'question_type', 'question_text', 'expected_answer', 'options', 'correct_option', 'is_active', 'appearance_count', 'correct_count', 'total_correct_percentage', 'total_questions'])

            for question in all_questions:
                row_data = {
                    'id': question.id,
                    'question_type': question.question_type,
                    'question_text': question.get_question_text(),
                    'expected_answer': getattr(question, 'expected_answer', None),
                    'options': getattr(question, 'options', None),
                    'correct_option': getattr(question, 'correct_option', None),
                    'is_active': question.get_is_active(),
                    'appearance_count': question.appearance_count,
                    'correct_count': question.correct_count,
                    'total_correct_percentage': question.total_correct_percentage,
                    'total_questions': getattr(question, 'total_questions', None),
                }

                writer.writerow([row_data[field] for field in row_data])

    def load_questions_from_csv(self):
        # Загрузка вопросов из файла
        question_list = []
        with open("D:\\Python\\3pr\\Learning_tool_app\\questions.csv", mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                question_type = row['question_type']
                if question_type not in ['free_form_question_type', 'multiple_choice_question_type']:
                    print(f"Ошибка: Неизвестный тип вопроса: {question_type}")
                    continue

                # Преобразование значений к нужным типам данных
                id = int(row['id'])
                question_type = row['question_type']
                question_text = row['question_text']
                is_active = row['is_active'].lower() == 'true'
                appearance_count = int(row['appearance_count'])
                correct_count = int(row['correct_count'])
                total_correct_percentage = int(row['total_correct_percentage'])

                # Создание объекта вопроса и добавление его в список
                if row['question_type'] == 'free_form_question_type':
                    expected_answer = row['expected_answer']
                    question = FreeFormQuestion(
                        id=id,
                        question_type=question_type,
                        question_text=question_text,
                        expected_answer = expected_answer,
                        is_active=is_active,
                        appearance_count=appearance_count,
                        correct_count=correct_count,
                        total_correct_percentage=total_correct_percentage,
                    )
                    question_list.append(question)

                elif row['question_type'] == 'multiple_choice_question_type':
                    options = row['options'].split(', ') if row['options'] else []                    
                    correct_option = row['correct_option']
                    question = MultipleChoiceQuestion(
                        id=id,
                        question_type=question_type,
                        question_text=question_text,
                        options=options,
                        correct_option=correct_option,
                        is_active=is_active,
                        appearance_count=appearance_count,
                        correct_count=correct_count,
                        total_correct_percentage=total_correct_percentage,
                    )
                    question_list.append(question)

        return question_list
 
    def print_questions_table(self, questions):
        # Prepare data for tabulation
        table_data = []
        for question in questions:
            correct_percentage = (question.correct_count / question.appearance_count) * 100 if question.appearance_count > 0 else 0

            # Используем пустую строку, если атрибут отсутствует
            expected_answer = getattr(question, 'expected_answer', '')
            options = ', '.join(getattr(question, 'options', []))
            correct_option = getattr(question, 'correct_option', '')

            row = [question.id, question.question_type, "Yes" if question.is_active else "No",
                question.question_text, expected_answer, options, correct_option,
                question.appearance_count, f"{correct_percentage:.2f}", question.correct_count]

            table_data.append(row)

        # Table header
        headers = ["ID", "Type", "Active", "Question", "Expected Answer", "Options", "Correct Option",
                "Appearance Count", "Correct %", "Total Correct"]
        colored_headers = [f"{Fore.GREEN}{header}{Style.RESET_ALL}" for header in headers]
        print(tabulate(table_data, headers=colored_headers, tablefmt="pretty"))


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
            timestamp = datetime.datetime.now().isoformat()
            file.write(f"{timestamp} - {result_string}\n")           

