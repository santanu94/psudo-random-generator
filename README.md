# psudo-random-generator
A psudo random generator code based on Middle Square Method algorithm.
The main code goes in the customPRG.py file.
It has a function random() which accepts a numerical value(limit) as parameter, and generates a random number from 0 to ( limit - 1 ), both inclusive.
# How to use
1) Simply import the class:
```python
import customPRG
```
2) Create object for the class:
```python
cmsm = customPRG.customMSM()
```
3) Get random number:
```python
rnd = cmsm.random(30)
```
This returns a random number between 0 to 29.
