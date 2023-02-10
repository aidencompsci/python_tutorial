from types import FunctionType

def lesson3_test1(users_function: FunctionType):
    output = users_function()
    return ("The correct full name format is \"Ross, Bob\"",
        output == "Ross, Bob",
    )

def lesson3_test2(users_function: FunctionType):
    output = users_function()
    return ("The correct full name format is \"BobBobBob\"",
        output == "BobBobBob",
    )
