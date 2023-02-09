from types import FunctionType

def lesson2_test1(users_function: FunctionType):
    output = users_function()
    return ("The number should be of type `int`",
        type(output) == int,
    )
