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

