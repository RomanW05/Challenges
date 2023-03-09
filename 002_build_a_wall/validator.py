# from interfaces import IValidator
from pydantic import BaseModel, ValidationError, validator

class User_input_validator(BaseModel):
    user_input: str

    @validator("user_input")
    def input_must_contain_space(cls, v):
        print(v, 'spaces', type(v))
        if ' ' not in v:
            raise ValueError('User input must contain a space')
        return v.title()

    @validator("user_input")
    def integers_check(cls, v):
        print(v.title())
        print(v, 'integers', type(v))
        number1, number2 = v.split(' ')
        try:
            number1 = int(number1)
            number2 = int(number2)
        except:
            raise ValueError('Both parameters must be integers')
        
        return [number1, number2]
        

    @validator("user_input")
    def boundry_values(cls, v):
        for index, number in enumerate(v):
            if number < 1:
                raise ValueError(f'Parameter with index {index} must be greater then 1')

        
    




















# class Validator(IValidator):
#     def __init__(self, user_input:str) -> None:
#         self.user_input = user_input
#         self.parameters = {}
    
#     def conditions(self) -> bool:
#         # The user_input must consist of 2 integers only
#         try:
#             self.user_input

#         except:
#             return False

#     def integers(self) -> bool:


    
#     def boundries(self):
#         pass