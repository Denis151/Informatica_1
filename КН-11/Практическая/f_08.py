Python 3.7.1rc1 (v3.7.1rc1:2064bcf6ce, Sep 26 2018, 14:21:39) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> math.fmod(37,5)
2.0
>>> 
math.random(5.0, 20.0)
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    math.random(5.0, 20.0)
AttributeError: module 'math' has no attribute 'random'
>>> import random
>>> random.random(5.0, 20.0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    random.random(5.0, 20.0)
TypeError: random() takes no arguments (2 given)
>>> random.random(5.0,20.0)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    random.random(5.0,20.0)
TypeError: random() takes no arguments (2 given)
>>> random.randint(5,20)
18
>>> 
