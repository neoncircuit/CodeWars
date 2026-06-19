function none(arr, fun){
  // ...
  return arr.length === 0 || arr.every(item => !fun(item));
}