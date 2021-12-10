# INPUT_FILE = 'day_03_test_input_1.txt'
INPUT_FILE = 'day_03_input_1.txt'


def get_most_and_least_common(bits):
  count_0s = bits.count('0')
  count_1s = bits.count('1')

  if count_0s == count_1s:
    return None, None

  if count_0s > count_1s:
    return '0', '1'

  return '1', '0'


def get_bin_numbers():
  bin_numbers = []

  with open(INPUT_FILE, 'r') as file:
    for line in file:
      bin_numbers.append(line.strip())      

  return bin_numbers


class Processor:
  def __init__(self, bin_numbers):
    self.bin_numbers = bin_numbers

  def process(self):
    for bit in range(len(self.bin_numbers[0])):
      new_bin_numbers = []
      
      for bin_number in self.bin_numbers:
        if self.matches_bit_criteria(bin_number, bit):
          new_bin_numbers.append(bin_number)

      if len(new_bin_numbers) == 1:
        return int(new_bin_numbers[0], 2)

      self.bin_numbers = new_bin_numbers

    raise Exception("I didn't expect to get here")


class OxygenGenerator(Processor):
  def matches_bit_criteria(self, bin_number, bit):
    all_at_bit = [bn[bit] for bn in self.bin_numbers]
    most, least = get_most_and_least_common(all_at_bit)
    if most is None:
      most = '1'
    return bin_number[bit] == most


class CO2Scrubber(Processor):
  def matches_bit_criteria(self, bin_number, bit):
    all_at_bit = [bn[bit] for bn in self.bin_numbers]
    most, least = get_most_and_least_common(all_at_bit)
    if least is None:
      least = '0'
    return bin_number[bit] == least



def main():
  all_bin_numbers = get_bin_numbers()

  og = OxygenGenerator(all_bin_numbers)
  co2 = CO2Scrubber(all_bin_numbers)

  ogp = og.process()
  co2p = co2.process()
  print(f'oxygen generator number is {ogp}, Co2 scrubber number is {co2p}')
  print(f'so the answer is {ogp*co2p}')



if __name__ == '__main__':
  main()
