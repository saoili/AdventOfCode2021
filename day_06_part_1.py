# INPUT_FILE = 'day_06_test_input_1.txt'
INPUT_FILE = 'day_06_input_1.txt'


def tick(fish):
  new_fish = []
  for fishy in fish:
    if fishy == 0:
      new_fish += [6, 8]
    else:
      new_fish.append(fishy - 1)

  return new_fish



def main():
  with open(INPUT_FILE, 'r') as file:
    for line in file:
      fish = [int(f) for f in line.strip().split(',')]

  print(fish)

  for i in range(80):
    fish = tick(fish)
    print(len(fish))


if __name__ == '__main__':
  main()
