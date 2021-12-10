INPUT_FILE = 'day_04_test_input_1.txt'
INPUT_FILE = 'day_04_input_1.txt'


CARD_SIZE = 5


class Board:
  def __init__(self, id):
    self.grid = {}
    self.row = -1
    self.id = id

  def add_row(self, text):
    self.row += 1

    splity = text.split()
    # print(f'this numbers, text is {text}, text.split is {splity}')
    numbers = [int(n) for n in text.split()]
    for i, number in enumerate(numbers):
      self.grid[(i, self.row)] = [number, False]

  def get_row(self, row_num):
    row = []

    for column_num in range(CARD_SIZE):
      row.append(self.grid[(column_num, row_num)])

    return row

  def get_column(self, column_num):
    column = []

    for row_num in range(CARD_SIZE):
      column.append(self.grid[(column_num, row_num)])

    return column

  def __str__(self):
    rows = []

    for row_num in range(CARD_SIZE):
      row = self.get_row(row_num)
      row_str = ''

      for number, called in row:
        # print(f'number is {number}, called is {called}')
        number_padded = f'{number:02}'
        if called:
          row_str = f'{row_str} \033[1m{number_padded}\033[0m'
          # print(f'row_str is {row_str}')
        else:
          row_str = f'{row_str} {number_padded}'

      rows.append(row_str)

    return '\n'.join(rows)

  def call(self, number):
    number = int(number)

    for row_num in range(CARD_SIZE):
      for column_num in range(CARD_SIZE):
        if self.grid[(column_num, row_num)][0] == number:
          self.grid[(column_num, row_num)][1] = True
          # print(f'setting self.grid[({column_num}, {row_num})][1] to True')

  def check_for_win(self):
    for row_num in range(CARD_SIZE):
      row = self.get_row(row_num)
      if all([r[1] for r in row]):
        return True

    for column_num in range(CARD_SIZE):
      column = self.get_column(column_num)
      if all([c[1] for c in column]):
        return True

    return False

  def get_score(self, number):
    number = int(number)
    total = 0

    for row_num in range(CARD_SIZE):
      row = self.get_row(row_num)
      for column_num in range(CARD_SIZE):
        location = self.grid[(column_num, row_num)]
        # print(f'grid at {column_num}, {row_num} is unmarked, adding {location[1]}')
        # print(f'total is now {total}')
        if not location[1]:
          total += location[0]

    return total * number


def parse_file():
  numbers = None
  board = None
  boards = []
  board_id = 1
  
  with open(INPUT_FILE, 'r') as file:
    for line in file:
      line = line.strip()

      if numbers is None:
        # print('that numbers')
        numbers = line.split(',')
      elif line == '':
        if board is not None:
          boards.append(board)
        board = Board(board_id)
        board_id += 1
      else:
        # print(f'about to add row {line}')
        board.add_row(line)

    boards.append(board)

  return numbers, boards


def play(numbers, boards):

  for number in numbers:
    winning_boards = []
    # print('\n\nno wins yet, boards look like')
    # for board in boards:
    #   print()
    #   print(board)

    print(f'calling {number}')
    any_wins = False
    for board in boards:
      board.call(number)
      if board.check_for_win():
        print(f'This board {board.id} wins with a score of {board.get_score(number)}')
        winning_boards.append(board)

    for winning_board in winning_boards:
      boards.remove(winning_board)


def main():
  numbers, boards = parse_file()
  print(f"numbers is {numbers}")
  print(f"boards is")
  for board in boards:
    print()
    print(board)

  play(numbers, boards)




if __name__ == '__main__':
  main()
