# pseudo-random-generator
A psudo random generator code based on Middle Square Method algorithm.
The main code goes in the customPRG.py file.
It has a function random() which accepts a numerical value(limit) as parameter, and generates a random number from 0 to ( limit - 1 ), both inclusive.

The code produces a seed file which helps in reducing chances of repetaton at the start for the same seed value.
# How to use
1) Download the customPRG.py file in the same folder as rest of the file using this one, or else help yourself with the path.
2) import the class:
```python
import customPRG
```
3) create object for the class:
```python
cmsm = customPRG.customMSM()
```
4) get random number:
```python
rnd = cmsm.random(30)
```
This returns a random number between 0 to 29.
