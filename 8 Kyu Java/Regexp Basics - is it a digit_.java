public class StringUtils {
  
  public static boolean isDigit(String s) {
    // your code goes here
    return s != null 
      && s.length() == 1
      && Character.getNumericValue(s.charAt(0)) >= 0 
      && Character.getNumericValue(s.charAt(0)) < 10;
  }
}