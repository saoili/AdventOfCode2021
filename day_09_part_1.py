INPUT_FILE = 'day_09_test_input_1.txt'
INPUT_FILE = 'day_09_input_1.txt'


class Heatmap:
  def __init__(self):
    self.grid = {}
    self.y = 0
    self.max_y = 0
    self.max_x = 0

  def add_line(self, line):
    line = line.strip()
    for x, value in enumerate(line):
      self.grid[(x, self.y)] = int(value)

    self.max_x = x
    self.max_y = self.y
    self.y += 1

  def is_low_point(self, x, y):
    # if x == 0 and y == 1:
    #   print(f"x is {x}, y is {y}")
    this_value = self.grid[(x, y)]

    for ox, oy in ((x-1, y), (x, y-1), (x+1, y), (x, y+1)):
      # out of range will be None
      value_at_other = self.grid.get((ox, oy))
      # if x == 0 and y == 1:
      #   print(f"other is {ox, oy}, value {value_at_other}")

      if value_at_other is not None and value_at_other <= this_value:
        # print(f"{x, y}: {this_value} is not a low point")
        return False

    # print(f"{x, y}: {this_value} is a low point")
    return True

  def get_risk_level(self, x, y):
    return self.grid[(x, y)] + 1

  def get_sum(self):
    total = 0

    for y in range(self.max_y + 1):
      for x in range(self.max_x + 1):
        if self.is_low_point(x, y):
          total += self.get_risk_level(x, y)

    return total

  def print(self):
    for y in range(self.max_y + 1):
      for x in range(self.max_x + 1):
        print(self.grid[(x, y)], end="")
      print()


def main():
  hm = Heatmap()

  with open(INPUT_FILE, 'r') as file:
    for line in file:
      hm.add_line(line)

  # hm.print()
  print(hm.get_sum())


if __name__ == '__main__':
  main()
