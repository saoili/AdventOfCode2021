from collections import defaultdict


INPUT_FILE = 'day_06_test_input_1.txt'
INPUT_FILE = 'day_06_input_1.txt'


class IDontHaveAGoodName:
  def __init__(self, fish):
    self.spawn_days = defaultdict(int)
    self.total_fish = 0
    self.days_past = 0

    for initial_state in fish:
      self.spawn_days[initial_state + 1] += 1
      self.total_fish += 1

    print(f"after init self.spawn_days is {self.spawn_days}")
    print(f"total_fish is {self.total_fish} and days_past is {self.days_past}")

  def tick(self):
    self.days_past += 1
    fish_today = self.spawn_days[self.days_past]
    print(f"adding {fish_today} fish, for a total of", end=" ")
    self.total_fish += fish_today
    self.spawn_days[self.days_past + 7] += fish_today
    self.spawn_days[self.days_past + 9] += fish_today

    # print(f"after tick self.spawn_days is {self.spawn_days}")
    # print(f"total_fish is {self.total_fish} and days_past is {self.days_past}")

    return self.total_fish


# def model_separately(initial_state, fish_count, days):
#   # with days - initial count days left we get fish_count new
#   days_left = days - initial_state
#   # then 


# def to_thing(fish, days):
#   fish_counts = {}

#   for i in range(8):
#     fish_counts[i] = fish.count(i)

#   print(fish_counts)


# def tick(fish):
#   new_fish = []
#   for fishy in fish:
#     if fishy == 0:
#       new_fish += [6, 8]
#     else:
#       new_fish.append(fishy - 1)

#   return new_fish



def main():
  with open(INPUT_FILE, 'r') as file:
    for line in file:
      fish = [int(f) for f in line.strip().split(',')]

  # to_thing(fish)
  # print(fish)
  # previous_day = 0
  # previous_growth = 0

  # # for day in range(256):
  # for day in range(80):
  #   fish = tick(fish)
  #   today = len(fish)
  #   growth = today - previous_day
  #   print(f"on day {day} growth grew by {growth - previous_growth}", end=" ")
  #   print(f"because it grew by {growth} to {today}")
  #   previous_day = today
  #   previous_growth = growth

  thing = IDontHaveAGoodName(fish)
  for day in range(256):
    print(f"on day {day + 1},", end=" ")
    print(thing.tick())


if __name__ == '__main__':
  main()
