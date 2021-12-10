INPUT_FILE = 'day_07_test_input_1.txt'
INPUT_FILE = 'day_07_input_1.txt'


def get_distance_to_best(positions):
  lowest = min(positions)
  highest = max(positions)
  best = None

  for place in range(lowest, highest + 1):
    this_distance = 0
    for position in positions:
      if position != place:
        higher = max(position, place)
        lower = min(position, place)
        j = 0
        if place == 2:
          # print(f'lower was {lower}, higher was {higher}')
          added = 0
        for i in range(lower, higher):
          j += 1
          if place == 2:
            # print(f'i is {i}, j is {j}')
            added += j
          this_distance += j
      #   if place == 2:
      #     print(f'in total we added {added}\n')
      # else:
      #   if place == 2:
      #     print('this one was already at 5')
    if best is None or this_distance < best:
      best = this_distance

  return best


def get_positions(line):
  line = line.strip()
  return [int(p) for p in line.split(',')]


def main():
  with open(INPUT_FILE, 'r') as file:
    for line in file:
      positions = get_positions(line)

  print(get_distance_to_best(positions))


if __name__ == '__main__':
  main()
