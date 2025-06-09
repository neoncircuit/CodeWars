function calculate(str) {
  //your code here...
  let result = str.replaceAll("plus", "+").replaceAll("minus", "-");
  if (result.endsWith("+") || result.endsWith("-")) {
    result = result.slice(0, -1);
  }
  return eval(result).toString();
}