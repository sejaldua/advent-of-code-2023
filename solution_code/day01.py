from os import write
from aocd.models import Puzzle
from ..utils import get_test_input, write_solution

"""
Day 1: Trebuchet?!
"""

puzzle = Puzzle(year=2023, day=1)

"""
Part A: 
Sum up the first and last digit in each line
"""

def part_a(test=False):
    data = get_test_input('day01/a') if test else Puzzle(year=2023, day=1).input_data
    lines = data.split("\n")
    ans = 0
    for l in lines:
        nums = [str(x) for x in l if x.isdigit()]
        num = int(nums[0] + nums[-1])
        ans += num
    return ans
    

assert(part_a(test=True) == 142)
answer_a = part_a()
write_solution('day01', 'a', answer_a)
puzzle.answer_a = answer_a  


"""
Part B:
Same problem as A but now 'one', 'two', 'three', 'four', 'five',
'six', 'seven', 'eight', and 'nine' are also valid digits
"""

def part_b(test=False):
    data = get_test_input('day01/b') if test else Puzzle(year=2023, day=1).input_data
    lines = data.split("\n")
    ans = 0
    NUMS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for l in lines:
        nums = []
        for i, x in enumerate(l):
            if x.isdigit():
                nums.append(str(x))
                continue
            else:
                for k, v in NUMS.items():
                    if l[i:i+len(k)] == k:
                        nums.append(str(v))
        num = int(nums[0] + nums[-1])
        ans += num
    return ans

assert(part_b(test=True) == 281)
answer_b = part_b()
write_solution('day01', 'b', answer_b)
puzzle.answer_b = answer_b