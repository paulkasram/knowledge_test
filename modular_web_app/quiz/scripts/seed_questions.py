from quiz.models import Topic, Question

def run():
    # Create the topic if it doesn't already exist
    python_topic, created = Topic.objects.get_or_create(
        name="Python for Beginners",
        description="An introduction to the Python programming language."
    )

    if not created:
        print("Topic 'Python for Beginners' already exists. Skipping creation.")
    else:
        print("Topic 'Python for Beginners' created successfully.")

    # Questions to seed
    questions = [
        {"question_text": "What is Python?", "option1": "A snake", "option2": "A programming language",
         "option3": "A type of food", "option4": "A car", "correct_answer": "A programming language"},
        {"question_text": "What is the correct extension for a Python file?", "option1": ".py", "option2": ".python",
         "option3": ".txt", "option4": ".exe", "correct_answer": ".py"},
        {"question_text": "Which keyword is used to define a function in Python?", "option1": "func", "option2": "define",
         "option3": "def", "option4": "lambda", "correct_answer": "def"},
        {"question_text": "What does len() do in Python?", "option1": "Finds the maximum value", "option2": "Finds the length of an object",
         "option3": "Converts an object to a string", "option4": "Sorts a list", "correct_answer": "Finds the length of an object"},
        {"question_text": "Which of the following is NOT a data type in Python?", "option1": "String", "option2": "Tuple",
         "option3": "List", "option4": "Tree", "correct_answer": "Tree"},
        {"question_text": "What will print(2 ** 3) output?", "option1": "5", "option2": "6",
         "option3": "8", "option4": "9", "correct_answer": "8"},
        {"question_text": "Which symbol is used for comments in Python?", "option1": "#", "option2": "//",
         "option3": "/*", "option4": "--", "correct_answer": "#"},
        {"question_text": "What is the output of print(type(5))?", "option1": "<class 'float'>", "option2": "<class 'int'>",
         "option3": "<class 'string'>", "option4": "<class 'number'>", "correct_answer": "<class 'int'>"},
        {"question_text": "What is a correct way to create a list in Python?", "option1": "{1, 2, 3}", "option2": "[1, 2, 3]",
         "option3": "(1, 2, 3)", "option4": "<1, 2, 3>", "correct_answer": "[1, 2, 3]"},
        {"question_text": "What does for i in range(3): do?", "option1": "Runs the loop 3 times", "option2": "Runs the loop 2 times",
         "option3": "Creates a list of 3 elements", "option4": "Gives a syntax error", "correct_answer": "Runs the loop 3 times"},
        {"question_text": "Which statement is used to stop a loop in Python?", "option1": "exit", "option2": "stop",
         "option3": "break", "option4": "end", "correct_answer": "break"},
        {"question_text": "What is the correct way to create a variable in Python?", "option1": "var x = 5", "option2": "x <- 5",
         "option3": "x = 5", "option4": "int x = 5", "correct_answer": "x = 5"},
        {"question_text": "What will print(10 % 3) output?", "option1": "1", "option2": "3",
         "option3": "7", "option4": "0", "correct_answer": "1"},
        {"question_text": "What is the output of print('Python' * 2)?", "option1": "Python2", "option2": "PythonPython",
         "option3": "Python*2", "option4": "Error", "correct_answer": "PythonPython"},
        {"question_text": "Which of these is used to handle exceptions in Python?", "option1": "try and catch", "option2": "try and except",
         "option3": "catch and finally", "option4": "try and handle", "correct_answer": "try and except"},
        {"question_text": "How do you import a module in Python?", "option1": "import(module_name)", "option2": "import module_name",
         "option3": "load module_name", "option4": "include module_name", "correct_answer": "import module_name"},
        {"question_text": "Which of the following is used to define a block of code in Python?", "option1": "{}", "option2": "()",
         "option3": "Indentation", "option4": ";", "correct_answer": "Indentation"},
        {"question_text": "What is the output of bool(0)?", "option1": "True", "option2": "False",
         "option3": "Error", "option4": "None", "correct_answer": "False"},
        {"question_text": "How do you start a virtual environment in Python?", "option1": "python -m venv myenv", "option2": "python venv myenv",
         "option3": "python env create", "option4": "python startenv myenv", "correct_answer": "python -m venv myenv"},
        {"question_text": "What is the correct syntax for defining a class in Python?", "option1": "class MyClass {", "option2": "class MyClass:",
         "option3": "def class MyClass:", "option4": "create class MyClass:", "correct_answer": "class MyClass:"},
    ]

    # Create questions
    for question in questions:
        Question.objects.create(topic=python_topic, **question)

    print("Seeding complete: 20 questions added.")
