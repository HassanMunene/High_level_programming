# Control flow
the if statement
there can be zero or more elif parts and the else part is optional
the keyword elif is a shoert for else if.

## the for statement
the python's for statements ierates over the items of any sequence(list, string, in the order in which they appear.
eg
```
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
... 
cat 3
window 6
defenestrate 12
>>> 

```
a code that modifies a collection while iterating over that same collection is tricky to get it right so it is usually advisable and more straight forward to loop over a copy of the same collection o create a new collection

## the range() function
if you really need to iterate over a sequence of numbers, the builtin range() function comes in handy. it generates arithmetic progressions:
```
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
>>> 
```
Remember in range() the given endpoint is never part of the generated sequence .
range(10) generates 10 values
to iterate ove the indeces of a sequence you can combine range() and len() as shown below
```
>>> a = ['mary', 'had', 'a', 'littel', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
... 
0 mary
1 had
2 a
3 littel
4 lamb
>>> 
```
## break and continue statements, and the else clause on loops

the break statement breaks out of the innermost for or while loop

loop statement may have an else clause, it is executed when the loop terminates through the exhaustion of the iterable with for or when th econdition becomes false with while but not when the loop terminates by break.

the pass statement does nothing it is only required when a statement is required syntatically but the program requires no action

## Pointers in c
dereferencing is the process of accessing the value stored at a particular memory location pointed to by a pointer varible.

```
int x = 10;
int *p = &x;

int y = *p;
```
the value y is assigned the value of x

when dealing with double pointers, you need to deference twice to access the value it points to.

```
int x = 10;
int *p = &x;
int **pp = &p;

int y = **pp;
```
python range() function is handy when you need to perform an action a specidfied number of times.

PEP python enhancement proposal

looping is a key computer science concept. if you want to become a good programmer mastering loop is among the first steps you need to take
sometimes you want to execute a block of code however many times you want.

range() generally allows you to generate an series of numbers within a given range.

range(stop) takes one argument - will start at 0 and includes every whole number upto it but not including it.
range(start, stop) takes two arguments
range(start, stop, step) takes three arguments

if you wrap range inside reverse()function then you can print the integers in reverse order
```
>>> for i in reversed(range(5)):
...     print(i)
... 
4
3
2
1
0
>>> 
```
## Python strings
strings are immutable this means they cannot be modified. however we changea strign by generating a copy of it.
```
>>> s = "mybacon"
>>> s[2] = 'f'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> 
```
here is how to copy a string
```
SyntaxError: unterminated string literal (detected at line 1)
>>> s = 'mybacon'
>>> s = s[:2] + 'f' + s[3:]
>>> s
'myfacon'
>>> s = 'mybacon'
>>> s = s.replace('b', 'f')
>>> s
'myfacon'
>>> 
```
the upper() method returns the string in uppercase
the lower() method does the opposite
the strip() method removes whitespace 



