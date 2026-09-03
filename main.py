from riddle import *
from player import *
from results import *
from game import *
from riddle_repository import *
from riddle_manager import *


repository = RiddleRepository("riddles.json")

manager = RiddleManager(repository)

def show_main_menu() -> str:
    print("\n1. Play game")
    print("2. Manage riddles")
    print("3. View leaderboard")
    print("4. Exit")

    return input("Choose an option: ")

def show_management_menu() -> str:
    print("\n--- RIDDLE MANAGEMENT ---")
    print("1. Add riddle")
    print("2. Show all riddles")
    print("3. Update riddle")
    print("4. Delete riddle")
    print("5. Return")

    return input("Choose an option: ")

def add_riddle(manager: RiddleManager) -> None:
    print("\n--- ADD RIDDLE ---")
    try:
        riddle_id = int(input("Enter riddle ID: "))
    except ValueError:
        print("Riddle ID must be a number.")
        return
    if manager.get_riddle_by_id(riddle_id) is not None:
        print("A riddle with this ID already exists.")
        return
    question = input("Enter question: ")
    correct_answer = input("Enter correct answer: ")
    difficulty = input("Enter difficulty (easy/medium/hard): ")
    category = input("Enter category: ")

    print("\nChoose riddle type:")
    print("1. Open riddle")
    print("2. Two-answer riddle")
    print("3. Four-answer riddle")

    riddle_type = input("Choose a type: ")
    try:
        if riddle_type == "1":
            riddle = OpenRiddle(
                riddle_id,
                question,
                correct_answer,
                difficulty,
                category)

        elif riddle_type == "2":
            answer1 = input("Enter first answer: ")
            answer2 = input("Enter second answer: ")

            riddle = TwoAnswerRiddle(
                riddle_id,
                question,
                correct_answer,
                [answer1, answer2],
                difficulty,
                category)

        elif riddle_type == "3":
            answer1 = input("Enter first answer: ")
            answer2 = input("Enter second answer: ")
            answer3 = input("Enter third answer: ")
            answer4 = input("Enter fourth answer: ")

            riddle = FourAnswerRiddle(
                riddle_id,
                question,
                correct_answer,
                [answer1, answer2, answer3, answer4],
                difficulty,
                category)

        else:
            print("Invalid riddle type.")
            return
    except ValueError as error:
        print(error)
        return
    manager.add_riddle(riddle)
    print("Riddle added successfully.")


def update_riddle(manager: RiddleManager) -> None:
    print("\n--- UPDATE RIDDLE ---")

    try:
        riddle_id = int(input("Enter riddle ID: "))
    except ValueError:
        print("Riddle ID must be a number.")
        return

    riddle = manager.get_riddle_by_id(riddle_id)

    if riddle is None:
        print("Riddle not found.")
        return

    print("\nCurrent riddle:")
    riddle.display()

    question = input("Enter new question: ")
    correct_answer = input("Enter new correct answer: ")
    difficulty = input("Enter new difficulty (easy/medium/hard): ")
    category = input("Enter new category: ")

    possible_answers = []

    if riddle.get_type() == "multiple_2":
        answer1 = input("Enter first answer: ")
        answer2 = input("Enter second answer: ")
        possible_answers = [answer1, answer2]

    elif riddle.get_type() == "multiple_4":
        answer1 = input("Enter first answer: ")
        answer2 = input("Enter second answer: ")
        answer3 = input("Enter third answer: ")
        answer4 = input("Enter fourth answer: ")
        possible_answers = [answer1, answer2, answer3, answer4]


    new_data = {
        "question": question,
        "correct_answer": correct_answer,
        "difficulty": difficulty,
        "category": category,
        "type": riddle.get_type(),
        "possible_answers": possible_answers
    }

    try:
        success = manager.update_riddle(riddle_id, new_data)

        if success:
            print("Riddle updated successfully.")
        else:
            print("Failed to update riddle.")

    except ValueError as error:
        print(error)


def delete_riddle(manager: RiddleManager) -> None:
    print("\n--- DELETE RIDDLE ---")

    try:
        riddle_id = int(input("Enter riddle ID: "))
    except ValueError:
        print("Riddle ID must be a number.")
        return

    riddle = manager.get_riddle_by_id(riddle_id)

    if riddle is None:
        print("Riddle not found.")
        return

    print("\nRiddle to delete:")
    riddle.display()

    confirmation = input("Are you sure you want to delete this riddle? (yes/no): ")

    if confirmation.lower() != "yes":
        print("Deletion cancelled.")
        return

    success = manager.delete_riddle(riddle_id)

    if success:
        print("Riddle deleted successfully.")
    else:
        print("Failed to delete riddle.")


def main() -> None:
    while True:
        choice = show_main_menu()

        if choice == "1":
            print("Play game")

        elif choice == "2":
            while True:
                management_choice = show_management_menu()

                if management_choice == "1":
                    add_riddle(manager)

                elif management_choice == "2":
                    riddles = manager.get_all_riddles()

                    if not riddles:
                        print("No riddles found.")

                    else:
                        for riddle in riddles:
                            print(
                                f"{riddle.get_id()} | "
                                f"{riddle.get_type()} | "
                                f"{riddle.get_question()}"
                            )

                elif management_choice == "3":
                    update_riddle(manager)

                elif management_choice == "4":
                    delete_riddle(manager)

                elif management_choice == "5":
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            print("View leaderboard")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()