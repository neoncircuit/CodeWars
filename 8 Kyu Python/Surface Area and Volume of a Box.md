# Surface Area and Volume of a Box

Write a function that returns the total surface area and volume of a box as an array: [area, volume]

# Given Code

```{python}
def get_size(w,h,d):
    #your code here
```

# My Solution

```{python}
def get_size(w,h,d):
    #your code here
    area = 2 * ((w*h)+(h*d)+(d*w))
    volume = w * h * d
    return [area, volume]
```
