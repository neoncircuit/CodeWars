# Regular Ball Super Ball

## Instructions

Create a class `Ball`. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

```
ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"
```

## Given Code
```python
class Ball(object):
    # your code goes here
```

## My Solution
```python
class Ball(object):
    # your code goes here
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
```
