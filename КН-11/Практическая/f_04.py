Python 3.7.1rc1 (v3.7.1rc1:2064bcf6ce, Sep 26 2018, 14:21:39) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 'abc'
>>> a *5
'abcabcabcabcabc'

>>> 
a = 'розробити програму'
>>> b = 'програму'
>>> a1 = 'розробити схему'
>>> b1 = 'схему'
>>>  in b
SyntaxError: unexpected indent
>>> a in b
False
>>> a1 in b1
False
>>> 

>>> import math
>>> math.max(7,22,37,16,8)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    math.max(7,22,37,16,8)
AttributeError: module 'math' has no attribute 'max'
>>> max(7,22,37,16,8)
37
>>> 
