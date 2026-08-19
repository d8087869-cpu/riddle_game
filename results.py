class QuestionResult:
    def __init__(
        self,
        riddle_id: int,
        riddle_type: str,
        category: str,
        time_taken: float) -> None:

        if time_taken <0:
            raise ValueError('Time cannot be negative')
        
        self.__riddle_id = riddle_id
        self.__riddle_type = riddle_type
        self.__category = category
        self.__time_taken = time_taken

    def get_riddle_type(self) -> str:
        return self.__riddle_type

    def get_time_taken(self) -> float:
        return self.__time_taken

    def get_category(self) -> str:
        return self.__category

    def get_riddle_id(self) -> int:
        return self.__riddle_id

class GameResult:
    def __init__(
        self,
        username: str,
        date: str,
        total_time: float,
        question_results: list[QuestionResult]) -> None:

        self.__username = username
        self.__date = date
        self.__total_time = total_time
        self.__question_results = question_results

    def get_total_riddles(self)-> int:
        return len(self.__question_results)

    def average_time_by_type(self) -> dict[str, float]:
        times_by_type = {}

        for result in self.__question_results:
            riddle_type = result.get_riddle_type()
            time_taken = result.get_time_taken()

            if riddle_type not in times_by_type:
                times_by_type[riddle_type] = []

            times_by_type[riddle_type].append(time_taken)

        averages = {}

        for riddle_type, times in times_by_type.items():
            averages[riddle_type] = sum(times) / len(times)

        return averages
    

    def average_time_by_category(self) -> dict[str, float]:
        times_by_category = {}

        for result in self.__question_results:
            category = result.get_category()
            time_taken = result.get_time_taken()

            if category not in times_by_category:
                times_by_category[category] = []

            times_by_category[category].append(time_taken)

        averages = {}

        for category, times in times_by_category.items():
            averages[category] = sum(times) / len(times)

        return averages

    def to_csv_row(self) -> list:
        total_riddles = self.get_total_riddles()

        if total_riddles == 0:
            average_time = 0
        else:
            average_time = self.__total_time / total_riddles

        return [
            self.__username,
            self.__date,
            self.__total_time,
            total_riddles,
            average_time]