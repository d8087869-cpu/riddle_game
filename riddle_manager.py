from riddle import *
from riddle_repository import RiddleRepository


class RiddleManager:
    def __init__(self, repository: RiddleRepository) -> None:
        self.__repository = repository
        self.__riddles = self.__repository.load_riddles()

    def get_all_riddles(self) -> list[Riddle]:
        return self.__riddles.copy()

    def get_riddle_by_id(self, riddle_id: int) -> Riddle | None:
        for riddle in self.__riddles:
            if riddle.get_id() == riddle_id:
                return riddle

        return None

    def add_riddle(self, riddle: Riddle) -> None:
        self.__riddles.append(riddle)
        self.__repository.save_riddles(self.__riddles)


    def update_riddle(self, riddle_id: int, new_data: dict) -> bool:
        riddle = self.get_riddle_by_id(riddle_id)

        if riddle is None:
            return False
        
        new_data["id"] = riddle_id

        updated_riddle = self.create_riddle_from_data(new_data)

        for index, riddle in enumerate(self.__riddles):
            if riddle.get_id() == riddle_id:
                self.__riddles[index] = updated_riddle
                break

        self.__repository.save_riddles(self.__riddles)

        return True
        


    def create_riddle_from_data(self, data: dict) -> Riddle:
        if data["type"] == "multiple_4":
            return FourAnswerRiddle(
                data["id"],
                data["question"],
                data["correct_answer"],
                data["possible_answers"],
                data["difficulty"],
                data["category"]
            )

        elif data["type"] == "multiple_2":
            return TwoAnswerRiddle(
                data["id"],
                data["question"],
                data["correct_answer"],
                data["possible_answers"],
                data["difficulty"],
                data["category"]
            )

        elif data["type"] == "open":
            return OpenRiddle(
                data["id"],
                data["question"],
                data["correct_answer"],
                data["difficulty"],
                data["category"]
            )

        raise ValueError("Unknown riddle type")

    def delete_riddle(self, riddle_id: int) -> bool:
        riddle = self.get_riddle_by_id(riddle_id)

        if riddle is None:
            return False

        self.__riddles.remove(riddle)
        self.__repository.save_riddles(self.__riddles)

        return True

