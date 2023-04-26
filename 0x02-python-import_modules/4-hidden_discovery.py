#!/usr/bin/python3
"""
this program prints all the names defined by the compiled
module that is going to be imported here
it should print one name per line
it should print only names that do not start with __
"""
if __name__ == "__main__":
    import hidden_4
    import types
    import importlib.util

    module = types.ModuleType("hidden_4")
    code = hidden_4.__code__
    exec(code, module.__dict__)

    for name in sorted(dir(module)):
        if not name.startswith("__"):
            print(name)
