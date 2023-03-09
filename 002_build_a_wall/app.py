from functions import wall_contruction, correct_parameters


while True:
    user_input = input("Build ")

    flag, number_of_rows, number_of_bricks = correct_parameters(user_input)
    if flag != True:
        continue

    wall = wall_contruction(number_of_rows, number_of_bricks)
    print(wall)
