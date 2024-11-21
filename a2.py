import random

user_data = {}
quiz_data = {
      'python': [
    {
        "question": "What is the output of the following code?\n\nx = [1, 2, 3, 4]\nprint(x[::-1])",
        "options": [ "[1, 2, 3, 4]","[4, 3, 2, 1]","Error","None"],
        "answer": "[4, 3, 2, 1]"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["Tuple","String","List","Integer"],
        "answer": "List"
    },
    {
        "question": "What is the correct way to create a function in Python?",
        "options": ["function myFunc():","def myFunc():","create myFunc():","def myFunc:"],
        "answer": "def myFunc():"
    },
    {
        "question": "What will be the output of the following code?\n\ndef add(x, y=5):\n    return x + y\nprint(add(3))",
        "options": [ "3", "5", "8", "Error"],
        "answer": "8"
    },
    {
        "question": "What is the purpose of the 'self' parameter in a class method?",
        "options": ["It refers to the instance of the class.","It refers to a global variable.","It refers to the class itself.","It is used to return a value."],
        "answer": "It refers to the instance of the class."
    },
    {
        "question": "What will be the output of the following code?\nx = [1, 2, 3]\nprint(len(x))",
        "options": ["3","2","1","Error"],
        "answer": "3"
    },
    {
        "question": "What does the 'lambda' keyword in Python define?",
        "options": ["A normal function","An anonymous function","A class","A module"],
        "answer": "An anonymous function"
    },
    {
        "question": "What will the following code print?\na = 5\nb = 10\na, b = b, a\nprint(a, b)",
        "options": ["5 10","10 5","Error","None"],
        "answer": "10 5"
    },
    {
        "question": "What is the output of the following code?\n\nprint(bool(0), bool(3.14), bool(-5))",
        "options": ["False True False","False True True","True False True","True True True"],
        "answer": "False True True"
    },
    {
        "question": "Which of the following will raise an error?",
        "options": ["x = 10/2","x = 10//2","x = 10 % 3","x = 10 ++ 2"],
        "answer": "x = 10 ++ 2"
    }
],
    'oopm': [
    {
        "question": "What are the four pillars of Object-Oriented Programming?",
        "options": ["Inheritance, Encapsulation, Abstraction, Polymorphism","Class, Object, Method, Constructor",    "Data hiding, Overloading, Overriding, Interfaces"],
        "answer": "Inheritance, Encapsulation, Abstraction, Polymorphism"
    },
    {
        "question": "What is the difference between an abstract class and an interface?",
        "options": ["An abstract class can have both concrete and abstract methods, while an interface can only have abstract methods.","Interfaces support multiple inheritance, but abstract classes do not.","Both (a) and (b)"],
        "answer": "Both (a) and (b)"
    },
    {
        "question": "What is method overriding in OOP?",
        "options": ["Defining a method in a subclass with the same signature as in the parent class.","Defining multiple methods with the same name in the same class.","Changing the return type of a method in the subclass."],
        "answer": "Defining a method in a subclass with the same signature as in the parent class."
    },
    {
        "question": "What is polymorphism in OOP?",
        "options": ["The ability to take many forms, allowing objects of different classes to be treated as objects of a common superclass.","Creating multiple constructors in a class.","The process of creating objects."],
        "answer": "The ability to take many forms, allowing objects of different classes to be treated as objects of a common superclass.*"
    },
    {
        "question": "Which of the following best describes encapsulation in OOP?",
        "options": ["Bundling the data and methods that operate on the data into a single unit (class).","Using inheritance to reuse code.","The ability of a function to handle different data types."],
        "answer": "Bundling the data and methods that operate on the data into a single unit (class)."
    },
    {
        "question": "What is the purpose of a constructor in object-oriented programming?",
        "options": ["To initialize the state of an object.","To destroy an object.","To implement polymorphism." ],
        "answer": "To initialize the state of an object."
    },
    {
        "question": "What is the difference between `==` and `===` in programming languages like JavaScript?",
        "options": ["`==` compares values, while `===` compares both values and types.","`==` compares memory addresses, while `===` compares values.","Both `==` and `===` work the same in JavaScript."],
        "answer": "`==` compares values, while `===` compares both values and types."
    },
    {
        "question": "What is recursion in programming?",
        "options": ["A process in which a function calls itself.","A loop that runs indefinitely.","A function that is called multiple times in a program."],
        "answer": "A process in which a function calls itself."
    },
    {
        "question": "What is a stack overflow error?",
        "options": ["When too many recursive calls are made, causing the stack memory to exceed its limit.","When a program has too many variables.","When a loop runs indefinitely."],
        "answer": "When too many recursive calls are made, causing the stack memory to exceed its limit."
    },
    {
        "question": "What is the purpose of exception handling in programming?",
        "options": ["To handle runtime errors and prevent the program from crashing.","To handle compilation errors.","To handle syntax errors."],
        "answer": "To handle runtime errors and prevent the program from crashing."
    }
],
    'dbms': [
    {
        "question": "What is a Database Management System (DBMS)?",
        "options": ["A collection of interrelated data","A set of programs to access and manage databases","Both A and B","None of the above"],
        "answer": "Both A and B"
    },
    {
        "question": "Which of the following is a primary key?",
        "options": ["A field that can have multiple values","A field that uniquely identifies each record","A field that allows duplicates","A field with missing values"],
        "answer": "A field that uniquely identifies each record"
    },
    {
        "question": "Which SQL command is used to remove a table from the database?",
        "options": ["DELETE","DROP","REMOVE","CLEAR"],
        "answer": "DROP"
    },
    {
        "question": "What does ACID stand for in the context of a transaction in DBMS?",
        "options": ["Atomicity, Consistency, Isolation, Durability","Accuracy, Consistency, Information, Durability","Availability, Concurrency, Isolation, Durability","Atomicity, Communication, Isolation, Data"],
        "answer": "Atomicity, Consistency, Isolation, Durability"
    },
    {
        "question": "What is a foreign key?",
        "options": ["A key used to uniquely identify a table","A key that is a primary key in another table","A key used for encryption","A key that contains NULL values"],
        "answer": "A key that is a primary key in another table"
    },
    {
        "question": "Which of the following is NOT a type of database model?",
        "options": ["Hierarchical","Network","Relational","Sequential"],
        "answer": "Sequential"
    },
    {
        "question": "Which normal form eliminates partial dependency?",
        "options": ["First Normal Form (1NF)","Second Normal Form (2NF)","Third Normal Form (3NF)","Boyce-Codd Normal Form (BCNF)"],
        "answer": "Second Normal Form (2NF)"
    },
    {
        "question": "In SQL, which command is used to retrieve data from a database?",
        "options": ["INSERT","UPDATE","SELECT","DELETE"],
        "answer": "SELECT"
    },
    {
        "question": "What is a JOIN in SQL?",
        "options": ["A command to combine records from two or more tables","A command to delete records","A command to update records","A command to insert new records"],
        "answer": "A command to combine records from two or more tables"
    },
    {
        "question": "Which of the following ensures that no duplicate rows are returned in SQL?",
        "options": ["DISTINCT","UNIQUE","PRIMARY","GROUP BY"],
        "answer": "DISTINCT"
    }
  ]
}

def clearscreen():
    print("\033[H\033[J")

def register():
    clearscreen()
    print("\n--- Register yourself here ---")
    while True:
        username = input("Enter a username: ")
        if username in user_data:
            print("Username already exists. Try again.")
        elif not username.isalnum() or len(username) < 5:
            print("Invalid username. It must be at least 5 characters long and contain only letters and numbers.")
        else:
            break

    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Password too short. It must be at least 8 characters long.")
        elif not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase letter.")
        elif not any(char.isdigit() for char in password):
            print("Password must contain at least one number.")
        elif not any(char in "!@#$%^&*()-_+=<>?/|\\{}[]:;\"',." for char in password):
            print("Password must contain at least one special character.")
        else:
            break
    
    user_data[username] = password
    print("Registration successful!")

def login():
    clearscreen()
    print("\n--- Login here ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if user_data.get(username) == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password. Try again.")
        return None

def take_quiz(username, subject):
    print(f"\n--- {subject} Quiz ---")
    questions = random.sample(quiz_data[subject], 5)
    score = 0
    for idx, q in enumerate(questions, 1):
        print(f"\nQ{idx}: {q['question']}")
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        while True:
            try:
                answer = int(input("Enter your answer (1-4): "))
                if 1 <= answer <= 4:
                    break
                else:
                    print("Invalid input. Choose between 1 and 4.")
            except ValueError:
                print("Please enter a number.")
        if q["options"][answer - 1] == q["answer"]:
            score += 1
    print(f"\nYou scored {score} out of 5!")
    save_details(username, subject, score)

def save_details(username, subject, score):
    with open("detail.txt", "a") as f:
        f.write(f"Username: {username}, Password: {user_data[username]}, Subject: {subject}, Score: {score}\n")

def main():
    while True:
        print("\n--- Quiz Application ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                clearscreen()
                while True:
                    print("\nChoose a subject for the quiz:")
                    for i, sub in enumerate(quiz_data.keys(), 1):
                        print(f"{i}. {sub}")
                    print(f"{len(quiz_data) + 1}. Logout")
                    sub_choice = input("Choose a subject: ")
                    clearscreen()
                    if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(quiz_data):
                        take_quiz(username, list(quiz_data.keys())[int(sub_choice) - 1])
                    elif sub_choice == str(len(quiz_data) + 1):
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice. Try again.")
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid input. Try again.")
        clearscreen()

if __name__ == "__main__":
    main()
