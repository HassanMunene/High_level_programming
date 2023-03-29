Testing is crucial in the software development phase. It helps ensure easy debugging, agile code, and enhanced reusability. 
Performing tests that cover all use cases helps prevent a codebase from breaking — minimizing exposure to vulnerabilities. 
Python has two main testing frameworks that developers can use, doctest and unittest.

## DOCTEST
Doctest is an inbuilt test framework that comes bundled with python by default. The doctest module searches for code fragments that resemble interactive python sessions and runs those sessions to confirm they operate as shown.

developers commonly use doctests to test documentation.the doctest module looks for sequences of prompts in a docstring, re-executes the extracted command, and compares the output with the commands input given in the docstrings test example

## unittest

Unittest test case runners allow more options when running tests, like reporting test statistics such as tests that passed and failed.

Unittest uses methods created in classes to manage tests. It has support for automation, setup, and shutdown code when testing. Unittest has several rich, in-built features that are unavailable in doctest, including generators and group fixture managers like setUp and tearDown.
