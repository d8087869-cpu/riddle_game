from riddle import Riddle

riddle = Riddle(
    1,
    "What is 5 + 7?",
    "12",
    "easy",
    "math")
print(riddle.check_answer('12'))
print(riddle.check_answer("10"))
print(riddle.to_dict())