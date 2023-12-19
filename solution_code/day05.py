from os import write
from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 4: Scratchcards
"""

puzzle = Puzzle(year=2023, day=5)

"""
Part A: 
Iterate through each mapping and map seed to soil, soil to fertilizer,
fertilizer to water, water to light, light to temperapture, temperature to humidity,
and humidity to location. 
What is the lowest location number that corresponds to any of the initial seed numbers?
"""

def part_a(test=False):
    data = get_test_input('day05/a') if test else puzzle.input_data
    mappings = data.split("\n\n")
    M = []
    _, seeds = mappings[0].split("\n")[0].split(': ')
    seed_nums = list(map(int, seeds.split(' ')))
    for mapping in mappings[1:]:
        ranges = [tuple(map(int, numbers.split())) for numbers in mapping.split("\n")[1:]]
        # print(ranges)
        outputs = []
        for seed in seed_nums:
            for dest, src, length in ranges:
                if seed in range(src, src + length):
                    outputs.append(seed - src + dest)
                    break
            else:
                outputs.append(seed)
        seed_nums = outputs

    return min(seed_nums)
    
assert(part_a(test=True) == 35)
answer_a = part_a()
write_solution('day05', 'a', answer_a)
puzzle.answer_a = answer_a  


"""
Part B:
The values on the initial seeds: line come in pairs. Within each pair, the first value 
is the start of the range and the second value is the length of the range. So, in the 
first line of the example above:
Consider all of the initial seed numbers listed in the ranges on the first line of the 
almanac. What is the lowest location number that corresponds to any of the initial 
seed numbers?
"""

def part_b(test=False):
    data = get_test_input('day05/a') if test else puzzle.input_data
    mappings = data.split("\n\n")
    M = []
    _, seeds = mappings[0].split("\n")[0].split(': ')
    numbers = list(map(int, seeds.split(' ')))
    seed_nums = [
        (numbers[i], numbers[i] + numbers[i + 1])
        for i in range(0, len(numbers), 2)
    ]
    for mapping in mappings[1:]:
        ranges = [tuple(map(int, numbers.split())) for numbers in mapping.split("\n")[1:]]
        outputs = []
        while seed_nums:
            start, end = seed_nums.pop()
            for dest, src, length in ranges:
                overlap_start = max(start, src)
                overlap_end = min(end, src + length)
                if overlap_start < overlap_end:
                    outputs.append(
                        (
                            overlap_start - src + dest,
                            overlap_end - src + dest,
                        )
                    )
                    if overlap_start > start:
                        seed_nums.append((start, overlap_start))
                    if end > overlap_end:
                        seed_nums.append((overlap_end, end))
                    break
            else:
                outputs.append((start, end))
        seed_nums = outputs

    return min(seed_nums)[0]

assert(part_b(test=True) == 46)
answer_b = part_b()
write_solution('day04', 'b', answer_b)
puzzle.answer_b = answer_b