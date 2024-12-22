# Grasshopper - Terminal Game #1

## Instructions

## Terminal Game - Create Hero Prototype

In this first kata in the series, you need to define a Hero prototype to be used in a terminal game. The hero should have the following attributes:

| Attribute   | Value                        |
|-------------|------------------------------|
| name        | User argument or 'Hero'      |
| position    | '00'                         |
| health      | 100                          |
| damage      | 5                            |
| experience  | 0                            |


## Given Code
```python
class Hero(object):
    def __init__(self, name):
        #Add default values here
        pass
```

## My Solution
```python
class Hero(object):
    def __init__(self, name="Hero"):
        #Add default values here
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0
```
