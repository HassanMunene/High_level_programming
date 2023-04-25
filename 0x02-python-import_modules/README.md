# Modules 
as your proagram get longer you may want to split it into several files for easier maintenance. you may also want to use handy function that you have written in several programs without copyinh its defination into each program

definationas in a module can be imported into other modules or into the main module

module is a file containing python definations and statements

## compiled python files
To speed up the loading of modules, python cashes the compiled version of each module in the __pycache__ directory under the name module.version.pyc
where the version encodes the format of the compile file.

eg the compiled version of spam.py will be
```
__pychache__/spam.cpython-33.pyc
```
this naming convention allows compiled modules from different releases and differrent versions of python to coexist

the compiled modules are platform-independent so the same library can be shared among systems with different architectures.

