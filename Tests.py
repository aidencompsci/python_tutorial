#
# File for managing all the test code
#

from types import FunctionType
import tests.lesson2 as l2
import tests.lesson3 as l3
import tests.lesson4 as l4

tests = {
    "lesson2_test1": l2.lesson2_test1,

    "lesson3_test1": l3.lesson3_test1,
    "lesson3_test2": l3.lesson3_test2,

    "lesson4_test1": l4.lesson4_test1,
    "lesson4_test2": l4.lesson4_test2,
    "lesson4_test3": l4.lesson4_test3,
    "lesson4_test4": l4.lesson4_test4,
    "lesson4_test5": l4.lesson4_test5,
    "lesson4_test6": l4.lesson4_test6,
    "lesson4_test7": l4.lesson4_test7,
}

def test(testname: str):
    def wrapper(func: FunctionType):
        if not testname in tests: raise Exception(f"Test '{testname}' does not exist. Try another name.")

        result:bool = False
        usermessage = f"Error: The test '{testname}' is failing."

        try: usermessage, result = tests[testname](func)
        except: pass

         
        if result:
            if not usermessage == f"Error: The test '{testname}' is failing.": print(usermessage)
            print(f"The test '{testname}' is passing!")
        else: print(usermessage)
    return wrapper
