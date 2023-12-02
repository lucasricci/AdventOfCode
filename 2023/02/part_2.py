import re
import math
from collections import defaultdict

games = open("input.txt").read().strip().split("\n")
possible_games = 0
total_power = 0

# Credits for https://github.com/fuglede/adventofcode/blob/master/2023/day02/solutions.py
for game in games:
  gamelist = re.sub('[;,:]','',game).split()
  bag = defaultdict(int)
  # Here we zip both lists, the first with the numbers and the second with it colors
  # Making it a tupple like [("red": 4),("blue": 6)] etc.
  for num, color in zip(gamelist[2::2], gamelist[3::2]):
    bag[color] = max(bag[color], int(num))
  if bag["red"] <= 12 and bag["green"] <= 13 and bag["blue"] <= 14:
    possible_games += int(gamelist[1])
  total_power += math.prod(bag.values())

print(total_power)