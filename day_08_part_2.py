INPUT_FILE = 'day_08_test_input_1.txt'
INPUT_FILE = 'day_08_test_input_2.txt'
INPUT_FILE = 'day_08_input_1.txt'


LENGTH_MAP = {2: 1, 4: 4, 3: 7, 7: 8}
LENGTH_MAP_MULTI = {6: [0, 6, 9], 5: [2, 3, 5]}
ORIGINAL_MAPPING = {
  'abcdfg': 9,
  'abcefg': 0,
  'abdefg': 6,
  'abdfg': 5,
  'acdeg': 2,
  'acdfg': 3,
}


def get_letter_mapping(signal_patterns, digit_to_pattern):
  # key is replacement, value is original
  letter_mapping = {}

  # 7 is like 1 with a in it
  for letter in digit_to_pattern[7]:
    if letter not in digit_to_pattern[1]:
      # print(f"so what's in there as {letter} is a")
      letter_mapping[letter] = 'a'

  c_or_f = ""
  b_or_d = ""

  # 4 is like 1 with b and d in it
  for letter in digit_to_pattern[4]:
    if letter in digit_to_pattern[1]:
      # print(f"so what's in there as {letter} is either c or f")
      c_or_f = c_or_f + letter
    else:
      # print(f"so what's in there as {letter} is either b or d")
      b_or_d = b_or_d + letter

  # there are three digits with 6 letters, 'c' is in 2 and 'f' is in all
  patterns_with_6 = [sp for sp in signal_patterns if len(sp) == 6]
  for letter in c_or_f:
    if sum([d.count(letter) for d in patterns_with_6]) == 2:
      # print(f"so what's in there as {letter} is c")
      letter_mapping[letter] = 'c'
    elif sum([d.count(letter) for d in patterns_with_6]) == 3:
      # print(f"so what's in there as {letter} is f")
      letter_mapping[letter] = 'f'
    else:
      print('huh?')

  patterns_with_5 = [sp for sp in signal_patterns if len(sp) == 5]
  # print(f"patterns_with_5 is {patterns_with_5}")

  # there are three digits with 5 letters, 'b' is only in one of them
  for letter in b_or_d:
    if sum([d.count(letter) for d in patterns_with_5]) == 1:
      # print(f"so what's in there as {letter} is b")
      letter_mapping[letter] = 'b'
    elif sum([d.count(letter) for d in patterns_with_5]) == 3:
      # print(f"so what's in there as {letter} is d")
      letter_mapping[letter] = 'd'
    else:
      print(f'huh?, sum([d.count({letter}) for d in patterns_with_5]) is {sum([d.count(letter) for d in patterns_with_5])}')

  e_or_g = ''

  for letter in 'abcdefg':
    if letter not in letter_mapping.keys():
      e_or_g += letter

  # print(f"e_or_g is {e_or_g}")

  # there are three digits with 5 letters, 'e' is only in one of them
  for letter in e_or_g:
    if sum([d.count(letter) for d in patterns_with_5]) == 1:
      # print(f"so what's in there as {letter} is e")
      letter_mapping[letter] = 'e'
    elif sum([d.count(letter) for d in patterns_with_5]) == 3:
      # print(f"so what's in there as {letter} is g")
      letter_mapping[letter] = 'g'
    else:
      print(f'huh?, sum([d.count({letter}) for d in patterns_with_5]) is {sum([d.count(letter) for d in patterns_with_5])}')



  # print(f"letter_mapping is {letter_mapping}")
  # for new_letter in sorted(letter_mapping.keys()):
  #   print(f"so {new_letter} represents {letter_mapping[new_letter]}")

  return letter_mapping


def get_patterns(signal_patterns):
  pattern_to_digit = {}
  digit_to_pattern = {}

  for signal_pattern in signal_patterns:
    spl = len(signal_pattern)
    if spl in LENGTH_MAP:
      pattern_to_digit[signal_pattern] = LENGTH_MAP[spl]
      digit_to_pattern[LENGTH_MAP[spl]] = signal_pattern

  letter_mapping = get_letter_mapping(signal_patterns, digit_to_pattern)

  # print(f"letter_mapping is {letter_mapping}")
  # print(f"pattern_to_digit is {pattern_to_digit}")

  for signal_pattern in signal_patterns:
    if signal_pattern not in pattern_to_digit:
      # print(f"but what is {signal_pattern}?")
      original_letters = ''
      for letter in signal_pattern:
        original_letters = original_letters + letter_mapping[letter]
      original_letters = "".join(sorted(original_letters))
      pattern_to_digit[signal_pattern] = ORIGINAL_MAPPING[original_letters]
      # print(f"it's {ORIGINAL_MAPPING[original_letters]}")

  return pattern_to_digit


def parse_line(line):
  line = line.strip()
  signal_patterns, output_digits = line.split('|')

  signal_patterns = ["".join(sorted(sp)) for sp in signal_patterns.split()]
  output_digits = ["".join(sorted(od)) for od in output_digits.split()]

  return signal_patterns, output_digits


def main():
  total = 0

  with open(INPUT_FILE, 'r') as file:
    for line in file:
      this_line = ''
      # print(f"\n\nline is {line.strip()}")
      signal_patterns, output_digits = parse_line(line)
      # print(signal_patterns, '\n', output_digits)
      patterns = get_patterns(signal_patterns)
      # print(patterns)

      for output_digits in output_digits:
        digit = str(patterns.get(output_digits))
        # print(digit, end="")
        this_line = this_line + digit

      total += int(this_line)

  print(f"the total is {total}")


if __name__ == '__main__':
  main()
