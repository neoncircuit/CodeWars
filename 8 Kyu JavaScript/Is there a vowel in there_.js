function isVow(a){
  const vowels = {
    97: 'a',
    101: 'e',
    105: 'i',
    111: 'o',
    117: 'u'
  };
  const result = [];
  for (let i = 0; i < a.length; i++) {
    const num = a[i];
    if (vowels.hasOwnProperty(num)) {
      result.push(vowels[num]);
    } else {
      result.push(num);
    }
  }
  return result;
}