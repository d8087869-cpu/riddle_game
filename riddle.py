class Riddle:
    def __init__(self, riddle_id:int,
                 question:str,
                 correct_answer:str,
                 difficulty:str,
                 category:str) -> None:

        if riddle_id <= 0 :
            raise ValueError ('Riddel ID must be positive')
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
    