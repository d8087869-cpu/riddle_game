class Riddle:
    def __init__(self, riddle_id:int,
                 question:str,
                 correct_answer:str,
                 difficulty:str,
                 category:str) -> None:

        if riddle_id <= 0 :
            raise ValueError ('Riddle ID must be positive')
        if not question.strip():
            raise ValueError ('Question cannot be empty')
        if not correct_answer.strip():
            raise ValueError ('Correct answer cant be empty')
        if difficulty.lower() not in ['easy', 'medium', 'hard']:
            raise ValueError ('Invalid difficulty')
        if not category.strip():
            raise ValueError('Category cannot be empty')

        self.__id = riddle_id
        self.__question = question
        self.__correct_answer = correct_answer
        self.__difficulty = difficulty
        self.__category = category

    def check_answer(self, answer:str) -> bool:
        return answer.lower() == self.__correct_answer.lower()

    def get_type(self)-> str:
        raise NotImplementedError
    
    def display(self)-> None:
        raise NotImplementedError

    def to_dict(self)-> dict:
        return {'id': self.__id,
                'question': self.__question,
                'correct_answer': self.__correct_answer,
                'difficulty': self.__difficulty,
                'category': self.__category}

    def get_question(self) -> str:
        return self.__question

    def get_id(self) -> int:
        return self.__id

    def get_category(self) -> str:
        return self.__category

class MultipleChoiceRiddle(Riddle):
    def __init__(self, riddle_id:int, question:str, correct_answer:str,possible_answers:list[str], difficulty:str, category:str)->None:
        super().__init__(riddle_id, question, correct_answer, difficulty, category)
        
        if not possible_answers:
            raise ValueError('possible answer cannot be empty')
        if correct_answer not in possible_answers:
            raise ValueError('correct answer must be in possible answer')

        self.__possible_answers = possible_answers

    def display(self)-> None:
        print(self.get_question())

        for index, answer in enumerate(self.__possible_answers, start=1):
            print(f'{index}. {answer}')
        
    def check_answer(self, answer:str)->bool:
        if answer.isdigit():
            number = int(answer)
            if 1 <= number <= len(self.__possible_answers):
                answer = self.__possible_answers[number -1]
        return super().check_answer(answer)

    def get_possible_answers(self) -> list[str]:
        return self.__possible_answers.copy()

class FourAnswerRiddle(MultipleChoiceRiddle):
    def __init__(self,
        riddle_id: int,
        question: str,
        correct_answer: str,
        possible_answers: list[str],
        difficulty: str,
        category: str) -> None:
        super().__init__(riddle_id,question,correct_answer,possible_answers,difficulty,category)

        if len(possible_answers) != 4:
            raise ValueError('four answer riddle must have exactly 4 answer')

    def get_type(self) -> str:
        return "multiple_4"


class TwoAnswerRiddle(MultipleChoiceRiddle):
    def __init__(
        self,
        riddle_id: int,
        question: str,
        correct_answer: str,
        possible_answers: list[str],
        difficulty: str,
        category: str) -> None:

        super().__init__(riddle_id,question,correct_answer,possible_answers,difficulty,category)

        if len(possible_answers) != 2:
            raise ValueError("Two answer riddle must have exactly 2 answers")

    def get_type(self) -> str:
        return "multiple_2"

class OpenRiddle(Riddle):
    def __init__(
        self,
        riddle_id: int,
        question: str,
        correct_answer: str,
        difficulty: str,
        category: str) -> None:
        super().__init__(riddle_id,question,correct_answer,difficulty,category)

    def display(self) -> None:
        print(self.get_question())

    def get_type(self) -> str:
        return "open"