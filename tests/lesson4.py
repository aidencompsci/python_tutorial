from types import FunctionType

def lesson4_test1(users_function: FunctionType):
    output = users_function()
    return ("x and y should be equal",
        output,
    )

def lesson4_test2(users_function: FunctionType):
    output = users_function()
    return ("x should be less than y",
        output,
    )


def lesson4_test3(users_function: FunctionType):
    output = users_function()
    return ("x should be less than or equal to y",
        output,
    )

def lesson4_test4(users_function: FunctionType):
    output = users_function()
    return ("x should be greater than or equal to y",
        output,
    )

def lesson4_test5(users_function: FunctionType):
    output = users_function()
    return ("x should be greater than y",
        output,
    )

def lesson4_test6(users_function: FunctionType):
    output = users_function()
    if len(output) == 2:
        their_grade, the_grade_they_want = output
        if not the_grade_they_want == "A+":
            return ("Don't aim for anything other than the highest grade! You can do it!",
                False,
            )
        elif their_grade == the_grade_they_want:
            return ("You got an A+, I knew you could do it! I'm sure you earned it, Well done!",
                True,
            )
    else:
        return ("Make sure the last line of the test says 'return your_grade, the_grade_you_want'! ",
            False,
        )
    return ("Try hacking the system and changing the teachers password while she isn't looking!",
        False,
    )

def lesson4_test7(users_function: FunctionType):
    choice_list = ["rock",     "paper", "scissors"]
    beat_list   = ["scissors", "rock",  "paper"]
    try:
        for pc,pb in zip(choice_list, beat_list):
            for uc in choice_list:
                game_config_output = f"computer={pc} and you={uc}"
                yc, cc, tied, yhw = users_function(uc, pc)
                if not pc == cc or not uc == yc:
                    return ("Remember not to change your value or the computers value by hand", False)
                game_tied, you_win = pc == uc, pb == uc
                if not tied == game_tied:
                    return (f"The game should be a tie for {game_config_output}", False)
                if yhw and not you_win:
                    return (f"The computer should beat you with {game_config_output}", False)
                if not yhw and you_win:
                    return (f"You should beat the computer with {game_config_output}", False)
                else:
                    return ("All possible states accounted for!", True)
    except:
        return ("something is wrong with the test, try setting it back to how it was originally and restarting? I'm sorry", False)
