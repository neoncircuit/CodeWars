# Training JS #32: methods of Math---round() ceil() and floor()

## Instructions

From this lesson, we learn about JS static object: `Math`. It mainly helps us to carry out mathematical calculations. It has a lot of properties and methods. Some of the properties and methods we rarely used. So we only learn some common methods.

The properties of the Math object are some constants, such as PI, on behalf of the approximate value of pi. The usage is `Math.PI`. I will no longer introduce one by one, please refer to the manual:

- [Math Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)

In this lesson we learn three methods to turn a number into an integer: `round()`, `ceil()` and `floor()`.

Their definitions and detailed information:

- [Math.round()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/round)

- [Math.ceil()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/ceil)

- [Math.floor()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor)

First of all, we have to understand the first thing, all the methods of the Math object are static methods. It means that you need to use the Math method like this: `Math.round(1.23)`. Not like this: `(1.23).round()`.

Here we use some examples to understand their usage:

```
console.log(Math.round(1.45)); //output:1
console.log(Math.ceil(1.45));  //output:2
console.log(Math.floor(1.45)); //output:1
console.log(Math.round(1.55)); //output:2
console.log(Math.ceil(1.55));  //output:2
console.log(Math.floor(1.55)); //output:1
```

We can see, `ceil()` always rounding up to get a large integer; `floor()` always rounding down to get a small integer; `round()` according to the fractional part and round it to integer.

When the parameter is negative, they still works:

```
console.log(Math.round(-1.45)); //output:-1
console.log(Math.ceil(-1.45));  //output:-1
console.log(Math.floor(-1.45)); //output:-2
console.log(Math.round(-1.55)); //output:-2
console.log(Math.ceil(-1.55));  //output:-1
console.log(Math.floor(-1.55)); //output:-2
```

It should be noted that they are not working on the fractional part. If you want to keep two decimal places or otherwise, you should use [Methods of Number object--toFixed(), toExponential() and toPrecision()](http://www.codewars.com/kata/57256064856584bc47000611), or use the following techniques:

```
var n=1.23456
var a=Math.round(n*100)/100
var b=Math.ceil(n*100)/100
var c=Math.floor(n*100)/100
console.log(a,b,c);  //output: 1.23 1.24 1.23
```

In the example above, we first multiply the number by 100, and then round it. the final result is to retain two decimal places.

Ok, lesson is over. let's us do some task.

## Task

Coding in function `roundIt`. function accept 1 parameter `n`. It's a number with a decimal point. Please use different methods based on the location of the decimal point, turn the number into an integer.

If the decimal point is on the left side of the number (that is, the count of digits on the left of the decimal point is less than that on the right), Using `ceil()` method.

```
roundIt(3.45) should return 4
```

If the decimal point is on the right side of the number (that is, the count of digits on the left of the decimal point is more than that on the right), Using `floor()` method.

```
roundIt(34.5) should return 34
```

If the decimal point is on the middle of the number (that is, the count of digits on the left of the decimal point is equals that on the right), Using `round()` method.

```
roundIt(34.56) should return 35
```

## Given Code
```python
def round_it(n):
    return
```

## My Solution
```python
import math

def round_it(n):
    int_part, dec_part = str(n).split('.')
    int_len = len(int_part)  
    dec_len = len(dec_part)
    return math.floor(n) if (int_len > dec_len) else math.ceil(n) if (int_len < dec_len) else round(n)
```
