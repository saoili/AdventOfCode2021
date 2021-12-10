INPUT_FILE = 'day_08_test_input_1.txt'
INPUT_FILE = 'day_08_test_input_2.txt'
INPUT_FILE = 'day_08_input_1.txt'


LENGTH_MAP = {2: 1, 4: 4, 3: 7, 7: 8}


def get_patterns(signal_patterns):
  patterns = {}

  for signal_pattern in signal_patterns:
    spl = len(signal_pattern)
    if spl in LENGTH_MAP:
      patterns[signal_pattern] = LENGTH_MAP[spl]

  return patterns



def parse_line(line):
  line = line.strip()
  signal_patterns, output_digits = line.split('|')

  signal_patterns = ["".join(sorted(sp)) for sp in signal_patterns.split()]
  output_digits = ["".join(sorted(od)) for od in output_digits.split()]

  return signal_patterns, output_digits


def main():
  total_count = 0

  with open(INPUT_FILE, 'r') as file:
    for line in file:
      print(f"\n\nline is {line}")
      signal_patterns, output_digits = parse_line(line)
      # print(signal_patterns, '\n', output_digits)
      patterns = get_patterns(signal_patterns)
      print(patterns)
      for pattern, digit in patterns.items():
        count_in = output_digits.count(pattern)
        print(f"there are {count_in} {digit}s in it")
        total_count += count_in

  print(f"total_count is {total_count}")


if __name__ == '__main__':
  main()
