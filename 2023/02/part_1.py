import re
from collections import defaultdict

games = open("input.txt").read().strip().split("\n")
possible_games = 0

# Credits for https://github.com/fuglede/adventofcode/blob/master/2023/day02/solutions.py
for game in games:
  gamelist = re.sub('[;,:]','',game).split()
  bag = defaultdict(int)
  for num, color in zip(gamelist[2::2], gamelist[3::2]):
    bag[color] = max(bag[color], int(num))
  if bag["red"] <= 12 and bag["green"] <= 13 and bag["blue"] <= 14:
    possible_games += int(gamelist[1])

print(possible_games)