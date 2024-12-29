# Barking mad

## Instructions

Teach snoopy and scooby doo how to bark using object methods. Currently only snoopy can bark and not scooby doo.

```
snoopy.bark() #return "Woof"
scoobydoo.bark() #undefined
```

Use method prototypes to enable all Dogs to bark.

## Given Code
```python
class Dog ():
  def __init__(self, breed):
    self.breed = breed
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")
```

## My Solution
```python
class Dog ():
    def __init__(self, breed):
        self.breed = breed
    
    def bark(self):
        return "Woof"
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")

snoopy.bark = lambda: "Woof"
```
