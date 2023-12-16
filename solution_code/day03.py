from os import write
from aocd.models import Puzzle
from utils import get_test_input, write_solution
import re
import string
from collections import defaultdict

"""
Day 3: Gear Ratios
"""

puzzle = Puzzle(year=2023, day=3)
SYMBOLS = set(string.punctuation) - set(".")
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def check_neighbors(grid, i, j):
    for dx, dy in DIRECTIONS:
        if (i + dx) >= 0 and (i + dx) < len(grid) and (j + dy) >= 0 and (j + dy) < len(grid[0]):
            if grid[i+dx][j+dy] in SYMBOLS:
                return True
            
    return False

def check_star_index(grid, star_indexes, i, j, num):
    for dx, dy in DIRECTIONS:
        if (i + dx) >= 0 and (i + dx) < len(grid) and (j + dy) >= 0 and (j + dy) < len(grid[0]):
            if grid[i+dx][j+dy] == '*':
                star_indexes[(i+dx, j+dy)].append(num)
                return True, star_indexes

    return False, star_indexes


"""
Part A: 
The engine schematic (your puzzle input) consists of a visual representation of the engine. 
Any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
Periods (.) do not count as a symbol.
"""

def part_a(test=False):
    data = get_test_input('day03/a') if test else puzzle.input_data
    grid = [[x for x in line] for line in data.split("\n")]
    ans = 0
    for i, row in enumerate(grid):
        # Extract the numbers using regular expressions
        number_indices = re.finditer(r"\d+", "".join(row))
        for n in number_indices:
            if any([check_neighbors(grid, i, j) for j in range(n.start(), n.end())]):
                ans += int(n.group())
    return ans
    

# assert(part_a(test=True) == 4361)
part_a(test=True)
answer_a = part_a()
write_solution('day03', 'a', answer_a)
puzzle.answer_a = answer_a  


"""
Part B:
The missing part wasn't the only issue - one of the gears in the engine is wrong. 
A gear is any * symbol that is adjacent to exactly two part numbers. Its gear 
ratio is the result of multiplying those two numbers together.
"""

def part_b(test=False):
    star_indexes = defaultdict(list)
    data = get_test_input('day03/a') if test else puzzle.input_data
    grid = [[x for x in line] for line in data.split("\n")]
    for i, row in enumerate(grid):
        # Extract the numbers using regular expressions
        number_indices = re.finditer(r"\d+", "".join(row))
        for n in number_indices:
            for j in range(n.start(), n.end()):
                found, star_indexes = check_star_index(grid, star_indexes, i, j, n.group())
                if found:
                    break

    return sum(int(num[0]) * int(num[1]) for num in star_indexes.values() if len(num) == 2)


assert(part_b(test=True) == 467835)
star_indexes = defaultdict(list)
answer_b = part_b()
write_solution('day03', 'b', answer_b)
puzzle.answer_b = answer_b