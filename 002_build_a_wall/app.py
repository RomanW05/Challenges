from functions import contruction, validation
from validator import User_input_validator
from pydantic import ValidationError

while True:
    user_input = input("Build ")
    print(f'{len(user_input)}, {type(user_input)}, |{user_input}|')
    try:
        User_input_validator(
            user_input=user_input,
        )
    except ValidationError as e:
        print(e)
        continue

    flag, number_of_rows, number_of_bricks = validation(numbers)
    if flag != True:
        continue

    wall = contruction(number_of_rows, number_of_bricks)
    print(wall)
