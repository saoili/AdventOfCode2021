# INPUT_FILE = 'day_02_test_input_1.txt'
INPUT_FILE = 'day_02_input_1.txt'


class Position:
  def __init__(self):
    self.place = 0
    self.depth = 0

  def move(self, direction, amount):
    amount = int(amount)

    if direction == 'forward':
      self.place += amount
      return

    if direction == 'down':
      self.depth += amount
      return

    if direction != 'up':
      raise Exception(
        f"I didn't think that could happen, direction is {direction}")

    self.depth -= amount

  def print(self):
    print(self.place * self.depth)



def main():
  position = Position()

  with open(INPUT_FILE, 'r') as file:
    for line in file:
      position.move(*line.strip().split())

  position.print()


if __name__ == '__main__':
  main()
