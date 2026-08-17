from riddle import *

riddle = MultipleChoiceRiddle(
    1,
    "What is 5 + 7?",
    "12",
    ["10", "11", "12", "13"],
    "easy",
    "math"
)

riddle.display()

print(riddle.check_answer("3"))
print(riddle.check_answer("12"))
print(riddle.check_answer("10"))