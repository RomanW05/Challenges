from validator import User_input_validator
from pydantic import ValidationError


def wall_contruction(number_of_rows, number_of_bricks):
    FULL_BRICK = '■■'
    HALF_BRICK = '■'
    MORTAR = '|'
    wall = ''
    for index in range(number_of_rows):
        if index % 2 == 0:
            construction = (FULL_BRICK + MORTAR) * (number_of_bricks - 1) + FULL_BRICK
        else:
            construction = (HALF_BRICK + MORTAR) + (FULL_BRICK + MORTAR) * (number_of_bricks - 1) + HALF_BRICK
        wall += f'{construction}\n'
    
    return wall


def operations_on_user_input(user_input):
    number_of_rows, number_of_bricks = user_input.split()
    number_of_rows = int(number_of_rows)
    number_of_bricks = int(number_of_bricks)

    return True, number_of_rows, number_of_bricks


def correct_parameters(user_input):
    try:
        User_input_validator(
            user_input=user_input,
        )
    except ValidationError as e:
        return False, 0, 0
    
    return operations_on_user_input(user_input)
    
    