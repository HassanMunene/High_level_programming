# 0x0A-python-inheritance
The following is the syntax for a derived class
```
class DerivedClassName(BaseClassName):
	statements
	.
	.
	.
	statements
```

```
class DerivedClassName(modname.BaseClassName)
```
When the class object is constructed the base class is remembered

If a requested attribute is not found in the class, the search proceeds to the base class and this rule applies recursively

python has two builtin functions that work with inheritance

1. Use *isinstance()* to check an instance type
1. Use *issubclass()* to check class inheritance.
```
issubclass(bool, int) is true since bool is a subclass of int,

however issubclass(float, int) is False since float is not a subclass of int
```
## Multiple Inheritance

```
class DerivedClassName(Base1, Base2, Base3):
	....
```

