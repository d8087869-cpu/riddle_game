from riddle import *


riddle = TwoAnswerRiddle(
    2,
    "Is Python a programming language?",
    "Yes",
    ["Yes", "No"],
    "easy",
    "english"
)

riddle.display()

print(riddle.get_type())
print(riddle.check_answer("1"))
print(riddle.check_answer("Yes"))
print(riddle.check_answer("No"))
riddle.get_type()