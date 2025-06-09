function heron(a, b, c) {
  let s = (a+b+c)/2;
  let formula = s*(s-a)*(s-b)*(s-c);
  return Math.sqrt(formula);
}