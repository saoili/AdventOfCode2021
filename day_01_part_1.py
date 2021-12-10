# INPUT_FILE = 'day_01_test_input_1.txt'
INPUT_FILE = 'day_01_input_1.txt'


def main():
  increases = 0

  with open(INPUT_FILE, 'r') as file:
    last_depth = None

    for line in file:
      depth = int(line.strip())
      if last_depth and depth > last_depth:
        increases += 1

      last_depth = depth

  print(f"there were {increases} increases")


if __name__ == '__main__':
  main()
