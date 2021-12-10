import unittest
import day_10_part_1
import day_10_part_2


class Day10Part1Tests(unittest.TestCase):
  def test_process(self):
    input_expected_output_map = {
      r'[({(<(())[]>[[{[]{<()<>>': 0,
      r'[(()[<>])]({[<{<<[]>>(': 0,
      r'{([(<{}[<>[]}>{[]{[(<()>': 1197,
      r'(((({<>}<{<{<>}{[]{[]{}': 0,
      r'[[<[([]))<([[{}[[()]]]': 3,
      r'[{[{({}]{}}([{[{{{}}([]': 57,
      r'{<[[]]>}<{[{[{[]{()[[[]': 0,
      r'[<(<(<(<{}))><([]([]()': 3,
      r'<{([([[(<>()){}]>(<<{{': 25137,
      r'<{([{{}}[<[[[<>{}]]]>[]]': 0,
    }

    for ins, expected_output in input_expected_output_map.items():
      output = day_10_part_1.process(ins)
      self.assertEqual(output, expected_output)


class Day10Part2Tests(unittest.TestCase):
  def test_get_score(self):
    input_expected_output_map = {
      r'}}]])})]': 288957,
      r')}>]})': 5566,
      r'}}>}>))))': 1480781,
      r']]}}]}]}>': 995444,
      r'])}>': 294,
    }

    for ins, expected_output in input_expected_output_map.items():
      output = day_10_part_2.get_score(ins)
      self.assertEqual(output, expected_output)

  def test_process(self):
    input_expected_output_map = {
      r'[({(<(())[]>[[{[]{<()<>>': ['}', '}', ']', ']', ')', '}', ')', ']',],
      r'[(()[<>])]({[<{<<[]>>(': [')', '}', '>', ']', '}', ')',],
      r'{([(<{}[<>[]}>{[]{[(<()>': None,
      r'(((({<>}<{<{<>}{[]{[]{}': ['}', '}', '>', '}', '>', ')', ')', ')', ')',],
      r'[[<[([]))<([[{}[[()]]]': None,
      r'[{[{({}]{}}([{[{{{}}([]': None,
      r'{<[[]]>}<{[{[{[]{()[[[]': [']', ']', '}', '}', ']', '}', ']', '}', '>',],
      r'[<(<(<(<{}))><([]([]()': None,
      r'<{([([[(<>()){}]>(<<{{': None,
      r'<{([{{}}[<[[[<>{}]]]>[]]': [']', ')', '}', '>',],
    }

    for ins, expected_output in input_expected_output_map.items():
      output = day_10_part_2.process(ins)
      self.assertEqual(output, expected_output)

  def test_get_score_answer(self):
    ins = [288957, 5566, 1480781, 995444, 294]
    expected_output = 288957

    output = day_10_part_2.get_score_answer(ins)

    self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
