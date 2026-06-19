const cannonsReady = (gunners) => {
  //your solution here
  for (const status of Object.values(gunners)) {
    if (status === "nay") {
      return "Shiver me timbers!";
    }
  }
  return "Fire!";
}