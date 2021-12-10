
for i in range(5, 10):
  with open('day_02_part_1.py', 'r') as input_file:
    print(f"i is {i}")
    with open(f'day_0{i}_part_1.py', 'w') as output_file:
      for line in input_file:
        output_file.write(line.replace('2', str(i)))
for i in range(10, 25):
  with open('day_02_part_1.py', 'r') as input_file:
    print(f"i is {i}")
    with open(f'day_{i}_part_1.py', 'w') as output_file:
      for line in input_file:
        output_file.write(line.replace('02', str(i)))