INPUT_FILE = 'day_10_test_input_1.txt'
INPUT_FILE = 'day_10_input_1.txt'


BRACKET_PAIRS = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}

POINTS_VALUES = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}


def process(line):
  # print(f"\n\nprocessing {line}")
  line = line.strip()
  open_brackets = []
  for char in line:
    if char in '([{<':
      open_brackets.append(char)
    else:
      if not BRACKET_PAIRS[open_brackets.pop()] == char:
        return POINTS_VALUES[char]

  # print(f'{line} is incomplete')
  return 0


def main():
  total = 0

  with open(INPUT_FILE, 'r') as file:
    for line in file:
      total += process(line)

  print(f"total is {total}")


if __name__ == '__main__':
  main()
