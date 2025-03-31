# Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence

## Instructions

## Description

Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

## Examples

```
"Hi!" --> "H!!"
"!Hi! Hi!" --> "!H!! H!!"
"aeiou" --> "!!!!!"
"ABCDE" --> "!BCD!"
```

## Given Code
```java
public class Solution {
    public static String replace(final String s) {
        return ""; //coding and coding....
    }
}
```

## My Solution
```java
public class Solution {
    public static String replace(final String s) {
        return s.replaceAll("[aeiouAEIOU]", "!"); //coding and coding....
    }
}
```
