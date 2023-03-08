from functions import contruction, validation

while True:
    numbers = input("Build ")

    flag, number_of_rows, number_of_bricks = validation(numbers)
    if flag != True:
        continue

    wall = contruction(number_of_rows, number_of_bricks)
    print(wall)
