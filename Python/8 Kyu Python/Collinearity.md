# Collinearity

Theoretical Material
You are given two vectors starting from the origin (x=0, y=0) with coordinates (x1,y1) and (x2,y2). Your task is to find out if these vectors are collinear. Collinear vectors are vectors that lie on the same straight line. They can be directed in the same or opposite directions. One vector can be obtained from another by multiplying it by a certain number. In terms of coordinates, vectors (x1, y1) and (x2, y2) are collinear if (x1, y1) = (k*x2, k*y2) , where k is any number acting as a coefficient.
![Alt text](https://d138zd1ktt9iqe.cloudfront.net/media/seo_landing_files/collinear-vectors-1627481628.png)

For more information, check out this article on collinearity.

# Given Code

```{python}
def collinearity(x1, y1, x2, y2):
    pass
```

# My Solution

```{python}
def collinearity(x1, y1, x2, y2):
    determinant = x1 * y2 - y1 * x2
    return determinant == 0
```
