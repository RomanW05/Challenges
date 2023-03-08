def contruction(number_of_rows, number_of_bricks):
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


def validation(numbers):
    try:
        number_of_rows, number_of_bricks = numbers.split()
    except:
        print('null\n')
        return False, 0, 0
    
    try:
        number_of_rows = int(number_of_rows)
        number_of_bricks = int(number_of_bricks)
    except:
        print('null\n')
        return False, 1, 0
    
    if number_of_rows < 1 or number_of_bricks < 1:
        print('null\n')
        return False, 1, 1
    
    total_bricks = number_of_rows * number_of_bricks
    if total_bricks > 10000:
        print("Naah, too much...here's my resignation.\n")
        return False, 2, 0

    return True, number_of_rows, number_of_bricks