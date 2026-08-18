from riddle import *
from player import Player

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

player = Player('David')
print(player.get_username())
player.rename("David2")
print(player.get_username())
player.rename("   ")