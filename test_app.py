from app import start_test
import pytest
from app import check, Question
from FileManager import FileManager
from Question import Question


def test_save_questions_to_csv():
    # Creating a sample question for testing
    question1 = Question(id=1, question_type='free_form_question_type', question_text='What is your name?',
                         correct_answer='John Doe', is_active=True, appearance_count=10, correct_count=5,
                         total_correct_percentage=50)

    # Creating an instance of the FileManager
    file_manager = FileManager()

    # Save the question to CSV
    file_manager.save_questions_to_csv([question1])

    # Load the questions from CSV to check if the saved data is correct
    loaded_questions = file_manager.load_questions_from_csv()

    # Assert that the loaded question matches the original question
    assert len(loaded_questions) == 1
    assert loaded_questions[0].id == 1
    assert loaded_questions[0].question_type == 'free_form_question_type'
    assert loaded_questions[0].question_text == 'What is your name?'
    assert loaded_questions[0].correct_answer == 'John Doe'
    assert loaded_questions[0].is_active is True
    assert loaded_questions[0].appearance_count == 10
    assert loaded_questions[0].correct_count == 5
    assert loaded_questions[0].total_correct_percentage == 50

def test_load_questions_from_csv():
    # Assuming 'questions.csv' contains valid data
    file_manager = FileManager()
    loaded_questions = file_manager.load_questions_from_csv()

    # Assert that the loaded questions list is not empty
    assert len(loaded_questions) > 0

    # Assert that each loaded question is an instance of the Question class
    for question in loaded_questions:
        assert isinstance(question, Question)

def test_question_activity_control():
    # Assuming 'questions.csv' contains valid data
    file_manager = FileManager()

    # Capture user input for testing
    with pytest.raises(SystemExit):
        # Mocking user input to exit the loop after first iteration
        with pytest.raises(SystemExit):
            file_manager.question_activity_control = lambda: "main_menu"
            file_manager.question_activity_control()

        # Mocking user input to enable a question
        file_manager.question_activity_control = lambda: "1\nenable"
        file_manager.question_activity_control()

        # Mocking user input to disable a question
        file_manager.question_activity_control = lambda: "2\ndisable"
        file_manager.question_activity_control()

        # Mocking user input to delete a question
        file_manager.question_activity_control = lambda: "3\ndelete"
        file_manager.question_activity_control()

if __name__ == "__main__":
    pytest.main()
