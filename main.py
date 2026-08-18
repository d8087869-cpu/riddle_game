from riddle import *
from player import *
from results import *

riddle = TwoAnswerRiddle(
    2,
    "Is Python a programming language?",
    "Yes",
    ["Yes", "No"],
    "easy",
    "english")


result = QuestionResult(
    1,
    "multiple_4",
    "math",
    5.4)




result1 = QuestionResult(1, "multiple_4", "math", 5.0)
result2 = QuestionResult(2, "multiple_4", "english", 7.0)
result3 = QuestionResult(3, "open", "geography", 10.0)
result4 = QuestionResult(4, "open", "history", 14.0)

game_result = GameResult(
    "David",
    "2026-08-18",
    36.0,
    [result1, result2, result3, result4])


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
#player.rename("   ")

print("Question result created successfully")


#print(game_result.get_total_riddles())
#print(game_result.average_time_by_type())

print("Total riddles:", game_result.get_total_riddles())
print("By type:", game_result.average_time_by_type())
print("By category:", game_result.average_time_by_category())
