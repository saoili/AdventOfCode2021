INPUT_FILE = 'day_07_test_input_1.txt'
INPUT_FILE = 'day_07_input_1.txt'


def triangular_number(n):
  # print(f'triangular number of {n}')
  return int(n*(n+1)/2)


def get_distance_to_best(positions):
  lowest = min(positions)
  highest = max(positions)
  best = None

  for place in range(lowest, highest + 1):
    this_distance = 0
    for position in positions:
      this_distance += triangular_number(abs(position - place + 10))
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
