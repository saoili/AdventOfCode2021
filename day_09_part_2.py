INPUT_FILE = 'day_09_test_input_1.txt'
INPUT_FILE = 'day_09_input_1.txt'


def directions(x, y):
  return (x-1, y), (x, y-1), (x+1, y), (x, y+1)


class Heatmap:
  def __init__(self):
    self.grid = {}
    self.y = 0
    self.max_y = 0
    self.max_x = 0
    self.basins = {}

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

    for ox, oy in directions(x, y):
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

  def _iterate_on(self, x, y):
    # print(f"iterating on {x, y}")
    new_basin = self.basins[(x, y)].copy()
    for location in self.basins[(x, y)]:
      lx, ly = location
      for neighbour in directions(lx, ly):
        nx, ny = neighbour
        value_at_other = self.grid.get((nx, ny))
        # print(f"value at {nx, ny} is {value_at_other}", end=" ")
        if value_at_other is not None and value_at_other != 9:
          # print(f"so we're adding it")
          new_basin.add((nx, ny))
          # print(f"self.basins[({x, y})] is now {self.basins[(x, y)]}")
        # else:
        #   print(f"so we're not adding it")
    self.basins[(x, y)] = new_basin


  def get_basins(self):
    for y in range(self.max_y + 1):
      for x in range(self.max_x + 1):
        if self.is_low_point(x, y):
          # print(f"\n\n\n\nlow point {x, y}")
          set_before = {}
          self.basins[(x, y)] = {(x, y)}
          while set_before != self.basins[(x, y)]:
            set_before = self.basins[(x, y)].copy()
            self._iterate_on(x, y)


  def multiply_largest(self):
    basin_sizes = []    

    for low_point, basin_set in self.basins.items():
      basin_size = len(basin_set)
      # print(f"basin centered on {low_point} is size {basin_size}")
      basin_sizes.append(basin_size)

    basin_sizes.sort()

    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


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
  # print(hm.get_sum())
  hm.get_basins()
  print(hm.multiply_largest())



if __name__ == '__main__':
  main()
