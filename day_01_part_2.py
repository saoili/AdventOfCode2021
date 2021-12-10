# INPUT_FILE = 'day_01_test_input_1.txt'
INPUT_FILE = 'day_01_input_1.txt'


def main():
  increases = 0

  with open(INPUT_FILE, 'r') as file:
    depths = [int(line.strip()) for line in file]

    windows = [sum(depths[i:i+3]) for i in range(len(depths)-2)]

    last_window = None

    for window in windows:
      if last_window and window > last_window:
        increases += 1

      last_window = window

  print(f"there were {increases} increases")


if __name__ == '__main__':
  main()
