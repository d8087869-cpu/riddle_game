import time
from results import *
from riddle import *
from player import Player
from datetime import date

class RiddleGame:
    def __init__(
        self,
        player: Player,
        riddles: list[Riddle]) -> None:

        self.__player = player
        self.__riddles = riddles
        self.__results = []

    def ask_riddle(self, riddle: Riddle) -> QuestionResult:
        start_time = time.time()

        riddle.display()
        answer = input("Your answer: ")

        while not riddle.check_answer(answer):
            print("Incorrect. Try again.")
            answer = input("Your answer: ")

        end_time = time.time()
        time_taken = end_time - start_time

        return QuestionResult(
            riddle.get_id(),
            riddle.get_type(),
            riddle.get_category(),
            time_taken)

    def start(self) -> GameResult:
        start_time = time.time()

        for riddle in self.__riddles:
            result = self.ask_riddle(riddle)
            self.__results.append(result)

        end_time = time.time()
        total_time = end_time - start_time

        return GameResult(
        self.__player.get_username(),
        str(date.today()),
        total_time,
        self.__results)

    def print_summary(self, result: GameResult) -> None:
        print("\n----- GAME SUMMARY -----")
        print(f"Player: {self.__player.get_username()}")
        print(f"Total riddles: {result.get_total_riddles()}")

        total_time = result.to_csv_row()[2]
        print(f"Total time: {total_time:.3f} seconds")

        print("Average time by type:")
        for riddle_type, average in result.average_time_by_type().items():
            print(f"{riddle_type}: {average:.3f} seconds")


        print("Average time by category:")
        for category, average in result.average_time_by_category().items():
            print(f"{category}: {average:.3f} seconds")