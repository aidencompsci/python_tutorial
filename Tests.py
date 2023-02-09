#
# File for managing all the test code
#

from types import FunctionType
import tests.lesson2 as l2

tests = {
    "lesson2_test1": l2.lesson2_test1
}

def test(testname: str):
    def wrapper(func: FunctionType):
        if not testname in tests: raise Exception(f"Test '{testname}' does not exist. Try another name.")

        result:bool = False
        failmessage = f"Error: The test '{testname}' is failing."

        try: failmessage, result = tests[testname](func)
        except: pass

        if result:  print(f"The test '{testname}' is passing!")
        else: print(failmessage)
    return wrapper
