export const boolToWord = (bool: boolean): string => {
  let con = " ";
  if (bool) {
    con = "Yes";  
  } else {
    con = "No";
  }
  return con;
};