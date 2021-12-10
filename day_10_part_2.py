import math


INPUT_FILE = 'day_10_test_input_1.txt'
INPUT_FILE = 'day_10_input_1.txt'


BRACKET_PAIRS = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}

POINTS_VALUES = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4,
}


def process(line):
  # print(f"\n\nprocessing {line}")
  line = line.strip()
  open_brackets = []
  closing_brackets = []

  for char in line:
    if char in '([{<':
      open_brackets.append(char)
    else:
      if not BRACKET_PAIRS[open_brackets.pop()] == char:
        # print(f'{line} is corrupted')
        return None

  open_brackets_left = open_brackets[::-1]
  # print(f"open_brackets is {open_brackets}")
  # print(f"open_brackets_left is {open_brackets_left}")

  for open_bracket in open_brackets_left:
    closing_brackets.append(BRACKET_PAIRS[open_bracket])

  # print(f'{line} is incomplete')
  # print(f'returning {closing_brackets}')
  return closing_brackets


def get_score(brackets):
  score = 0
  for bracket in brackets:
    score *= 5
    score += POINTS_VALUES[bracket]

  return score


def get_score_answer(scores):
  return sorted(scores)[math.floor(len(scores)/2)]


def main():
  line_scores = []

  with open(INPUT_FILE, 'r') as file:
    for line in file:
      closing_brackets = process(line)
      if closing_brackets is not None:
        score = get_score(closing_brackets)
        # print(f'closing_brackets is {"".join(closing_brackets)} score is {score}')
        line_scores.append(get_score(closing_brackets))

  print(get_score_answer(line_scores))



if __name__ == '__main__':
  main()
