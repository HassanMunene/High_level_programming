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

