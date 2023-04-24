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




