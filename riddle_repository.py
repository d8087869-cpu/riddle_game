import json
from riddle import*


class RiddleRepository:
    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path

    def load_riddles(self)-> list[Riddle]:
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            riddles = []
        except (FileNotFoundError, json.JSONDecodeError):
            return[]
        if not data:
            return []
        riddles = []
        for item in data:
            if item["type"] == "multiple_4":
                riddle = FourAnswerRiddle(
                    item['id'],
                    item['question'],
                    item['correct_answer'],
                    item['possible_answers'],
                    item['difficulty'],
                    item['category'])
            elif item['type'] == 'multiple_2':
                 riddle =TwoAnswerRiddle(
                    item['id'],
                    item['question'],
                    item['correct_answer'],
                    item['possible_answers'],
                    item['difficulty'],
                    item['category'])
            elif item["type"] == "open":
                riddle = OpenRiddle(
                    item["id"],
                    item["question"],
                    item["correct_answer"],
                    item["difficulty"],
                    item["category"])

            else:
                raise ValueError("Unknown riddle type")

            riddles.append(riddle)

        return riddles


    def save_riddles(self, riddles:list[Riddle])->None:
        data = []

        for riddle in riddles:
            data.append(riddle.to_dict())

        with open(self.__file_path, 'w') as file:
            json.dump(data, file, indent=4)

