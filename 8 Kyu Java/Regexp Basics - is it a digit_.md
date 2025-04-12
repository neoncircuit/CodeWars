# Regexp Basics - is it a digit?

## Instructions

Implement `String#digit?` (in Java `StringUtils.isDigit(String)`), which should return `true` if given object is a single digit (0-9), `false` otherwise.

## Given Code
```
public class StringUtils {
  
  public static boolean isDigit(String s) {
    // your code goes here
  }
}
```

## My Solution
```
public class StringUtils {
  
  public static boolean isDigit(String s) {
    // your code goes here
    return s != null 
      && s.length() == 1
      && Character.getNumericValue(s.charAt(0)) >= 0 
      && Character.getNumericValue(s.charAt(0)) < 10;
  }
}
```