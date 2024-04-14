# easy logs

Given a logarithm base <i>X</i> and two values <i>A</i> and <i>B</i>, return a sum of logarithms with the base <i>X</i>:

<p><b>log<sub>X</sub>A + log<sub>X</sub>B</b></p>

Where <i>log<sub>X</sub>A</i> and <i>log<sub>X</sub>B</i> are logarithms of <i>A</i> and <i>B</i> with base <i>X</i>, respectively.


# Given Code

```{python}
def logs(x, a, b):
    pass
```

# My Solution

```{python}
import math

def logs(x, a, b):
    return math.log(a, x) + math.log(b, x)
```
