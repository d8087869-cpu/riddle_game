from riddle import *
from player import *
from results import *
from game import *

riddle1 = FourAnswerRiddle(
    1,
    "What is 5 + 7?",
    "12",
    ["10", "11", "12", "13"],
    "easy",
    "math")

riddle2 = OpenRiddle(
    2,
    "What is the capital of France?",
    "Paris",
    "easy",
    "geography")

player = Player("David")

game = RiddleGame(player, [riddle1, riddle2])

result = game.start()

game.print_summary(result)