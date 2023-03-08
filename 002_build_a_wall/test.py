import pytest
from functions import contruction
from wall import wall_5_5, wall_10_7

from functions import validation

def test_wall():
    wall = contruction(5, 5)
    assert wall == wall_5_5, 'Wall 5 5 not constructed properly'
    wall = contruction(10, 7)
    assert wall == wall_10_7, 'Wall 5 5 not constructed properly'



def test_split_values():
    flag, number_of_rows, number_of_bricks = validation('5')
    assert flag == False, 'Unvalid flag response, only one number added'
    assert number_of_rows == 0, 'Unvalid number of rows response'
    assert number_of_bricks == 0, 'Unvalid number of bricks response'


def test_integers():
    flag, number_of_rows, number_of_bricks = validation('5 4')
    assert flag == True, 'Unvalid flag response'
    assert number_of_rows == 5, 'Unvalid number of rows response'
    assert number_of_bricks == 4, 'Unvalid number of bricks response'

    flag, number_of_rows, number_of_bricks = validation('a 4')
    assert flag == False, 'Unvalid flag response'
    assert number_of_rows == 1, 'Unvalid code number of rows response'
    assert number_of_bricks == 0, 'Unvalid code number of bricks response'

    flag, number_of_rows, number_of_bricks = validation('"eight" [3]')
    assert flag == False, 'Unvalid flag response'
    assert number_of_rows == 1, 'Unvalid code number of rows response'
    assert number_of_bricks == 0, 'Unvalid code number of bricks response'

    flag, number_of_rows, number_of_bricks = validation('12 -4')
    assert flag == False, 'Unvalid flag response'
    assert number_of_rows == 1, 'Unvalid code number of rows response'
    assert number_of_bricks == 1, 'Unvalid code number of bricks response'


def test_building_limits():
    flag, number_of_rows, number_of_bricks = validation('123 1024')
    assert flag == False, 'Unvalid flag response'
    assert number_of_rows == 2, 'Unvalid code number of rows response'
    assert number_of_bricks == 0, 'Unvalid code number of bricks response'