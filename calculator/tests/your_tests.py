#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
assert run("20 / 4").output == "5"
assert run("8 - 1").output == "7"
assert run("25").exit_status != 0
###

print("All tests passed!")