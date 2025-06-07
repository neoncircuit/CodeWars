function neutralise(s1, s2) {
  // Here be dragons!
  let result = [];
    
  for (let i = 0; i < Math.min(s1.length, s2.length); i++) {
      if (s1[i] === s2[i]) {
          result.push(s1[i]);
      } else {
          result.push("0");
      }
  }

  return result.join("");
}