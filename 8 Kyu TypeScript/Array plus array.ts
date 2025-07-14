export const arrayPlusArray = (arr1 : number[], arr2 : number[]) : number => {
  // something went wrong ?
  return [...arr1, ...arr2].reduce((sum, current) => sum + current, 0);
}