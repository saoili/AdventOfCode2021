from collections import defaultdict


# INPUT_FILE = 'day_03_test_input_1.txt'
INPUT_FILE = 'day_03_input_1.txt'


def get_most_and_least_common(digits):
  count_0s = digits.count('0')
  count_1s = digits.count('1')

  if count_0s == count_1s:
    raise Exception("I didn't think that was supposed to happen")

  if count_0s > count_1s:
    return '0', '1'

  return '1', '0'



def main():
  all_thingies = defaultdict(list)

  with open(INPUT_FILE, 'r') as file:
    for line in file:
      line = line.strip()
      for i, digit in enumerate(line):
        all_thingies[i].append(digit)

  gamma_bin = ''
  epsilon_bin = ''

  for i, digits in all_thingies.items():
    print(f'looking at digit in place {i}')
    most, least = get_most_and_least_common(digits)
    gamma_bin = gamma_bin + most
    epsilon_bin = epsilon_bin + least

  print(f'gamma_bin is {gamma_bin}')
  print(f'epsilon_bin is {epsilon_bin}')

  gamma = int(gamma_bin, 2)
  epsillon = int(epsilon_bin, 2)

  print(f'gamma is {gamma}, epsillon is {epsillon}')
  print(f'so the answer is {gamma * epsillon}')



if __name__ == '__main__':
  main()
