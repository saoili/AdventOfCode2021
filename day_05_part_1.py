from collections import defaultdict


INPUT_FILE = 'day_05_test_input_1.txt'
INPUT_FILE = 'day_05_input_1.txt'


class Ocean:
  def __init__(self):
    self.grid = defaultdict(int)

  def add_line_segment(self, x1, y1, x2, y2):
    if x1 != x2 and y1 != y2:
      print('skip')
      return

    if x1 > x2:
      x1, x2 = x2, x1

    if y1 > y2:
      y1, y2 = y2, y1

    print(f'adding line from {x1}, {y1} to {x2}, {y2}')
    for this_x in range(x1, x2+1):
      for this_y in range(y1, y2+1):
        self.grid[(this_x, this_y)] += 1

  def count_points(self):
    points_of_2_or_more = 0

    for co_ords, point in self.grid.items():
      if point >= 2:
        print(f'adding a point for {co_ords}, which has {point}')
        points_of_2_or_more += 1

    return points_of_2_or_more


def main():
  o = Ocean()

  with open(INPUT_FILE, 'r') as file:
    for line in file:
      line = line.strip()

      p1, p2 = line.split(' -> ')
      x1, y1 = [int(c) for c in p1.split(',')]
      x2, y2 = [int(c) for c in p2.split(',')]

      o.add_line_segment(x1, y1, x2, y2)

  print(o.count_points())



if __name__ == '__main__':
  main()
