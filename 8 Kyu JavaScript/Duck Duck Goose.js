function duckDuckGoose(players, goose) {
  // ...
  let position = (goose-1) % players.length
  return players[position].name
}