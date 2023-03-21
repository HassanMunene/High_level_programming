#  Working of import in python

imports in python is similar to #include header files in c/c++. Python module can get access to code from another module by importing the files/function isong the import.

When a module is imported the interpreter first searches it in sys.modules, which is the cache for all the modules which have been previously imported. if it is not there then it searches in all built-in modules with that name. if it is found then the interpreter runs all the code and is made available to the file.

If it is still not found then the the interpreter searches for a file with the same name in the list of the directories given by the variable sys.path.

**sys.path** is a variable containing a list of paths that contain python libraries, packages and a directory containing the input scripts

## Syntax of import statement
users can import both packages and modules. 

Users can also import specific objects from a package or a module.

```
import gfg
```
gfg can be a package or a module

```
from gfg import geek
```
Here the user imports the resource from another package or module. so geek can either be a module, sub-package, objects such as class or function
## Guide on imports
1. They should always be written at the top of the file, just after any module comment or docstrings
1. imports should always be separated by a blank space

```
# Example
import math

import os

# Third party imports
from flask import Flask

from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy

# local application imports
from local_module import local_class
```

## Absolute imports in Python
Absolute imports involve a fullpath. i.e from the projects root folder to the desired module

let's assume we have the following directory structure:

![dir-structure](https://github.com/HassanMunene/Django/blob/main/images/absolute-import-updated.jpg)

Here is a directory named project
under which there are to subdirectories: pkg1 and pkg2

pkg1 has 2 modules in it: module1 and module2

pkg2 has 3 modules: module3, module4 and __init__.py and 1 subpkg names subpkg1 which contians module5:

let's assume module1 contains a function called fun1
module3 contains a function called fun2

module5 contains a function called fun3

This is how we can import those functions using absolute path

```
from pkg1 import module2
from pkg2 import module3 import fun2
from pkg2.subpkg1.module5 import fun3
```
Absolute path will remain valid even if the current location of the import statement changes

## Relative imports

Relative imports specifies an object or module imported from it's current location
they depend on the current location as well as the location of the modules or the object to be imported

It uses dot(.) to specifiy the location. 
A single dot specifies that the module is in the current directory

Two dots specifies that the module is in it's parent directory of the current location

Three dots(...) specifies that it is in the grandparent directory of the current location
