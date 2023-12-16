from os import write
from aocd.models import Puzzle
from utils import get_test_input, write_solution
import re
import string

"""
Day 4: Scratchcards
"""

puzzle = Puzzle(year=2023, day=4)

"""
Part A: 
The first match makes the card worth one point and each match after 
the first doubles the point value of that card.
"""

def part_a(test=False):
    data = get_test_input('day04/a') if test else puzzle.input_data
    ans = 0
    for line in data.split("\n"):
        _, nums = line.split(": ")
        left, right = nums.split(" | ")
        winning_nums = list(map(int, (re.findall(r"\d+", left))))
        nums = list(map(int, (re.findall(r"\d+", right))))
        points = 0
        for n in nums:
            if n in winning_nums:
                points = 1 if points == 0 else points * 2
        ans += points
    return ans
    
assert(part_a(test=True) == 13)
answer_a = part_a()
write_solution('day04', 'a', answer_a)
puzzle.answer_a = answer_a  


"""
Part B:
Specifically, you win copies of the scratchcards below the winning card 
equal to the number of matches. So, if card 10 were to have 5 matching numbers, 
you would win one copy each of cards 11, 12, 13, 14, and 15.
"""

def part_b(test=False):
    data = get_test_input('day04/a') if test else puzzle.input_data
    scratchcards = {i+1: 1 for i in range(len(data.split("\n")))}
    for i, line in enumerate(data.split("\n")):
        card_num = i+1
        _, nums = line.split(": ")
        left, right = nums.split(" | ")
        winning_nums = list(map(int, (re.findall(r"\d+", left))))
        nums = list(map(int, (re.findall(r"\d+", right))))
        for _ in range(scratchcards[card_num]):
            cards_won = sum([1 for n in nums if n in winning_nums])
            for i in range(card_num + 1, card_num + 1 + cards_won):
                scratchcards[i] += 1
    return sum(list(scratchcards.values()))

assert(part_b(test=True) == 30)
answer_b = part_b()
write_solution('day04', 'b', answer_b)
puzzle.answer_b = answer_b