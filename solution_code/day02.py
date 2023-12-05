from os import write
from aocd.models import Puzzle
from utils import get_test_input, write_solution

"""
Day 2: Cube Conundrum
"""

puzzle = Puzzle(year=2023, day=2)

"""
Part A: 
The Elf would first like to know which games would have been possible 
if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

Example Games:
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
"""

def part_a(test=False):
    data = get_test_input('day02/a') if test else puzzle.input_data
    lines = data.split("\n")
    game_ids = []
    for i, game in enumerate(lines):
        _, game = game.split(': ')
        valid = True
        handfuls = game.split('; ')
        for handful in handfuls:
            balls = handful.split(', ')
            for ball_color in balls:
                num = int(''.join([x for x in ball_color if x.isdigit()]))
                if ('red' in ball_color and num > 12) or ('green' in ball_color and num > 13) or ('blue' in ball_color and num > 14):
                    valid = False
        if valid:
            game_ids.append(i+1)
    return sum(game_ids)

assert(part_a(test=True) == 8)
answer_a = part_a()
write_solution('day02', 'a', answer_a)
puzzle.answer_a = answer_a  


"""
Part B:
In each game you played, what is the fewest number of cubes of each color that could have been 
in the bag to make the game possible?
"""

def part_b(test=False):
    data = get_test_input('day02/b') if test else puzzle.input_data
    lines = data.split("\n")
    ans = 0
    for i, game in enumerate(lines):
        mins = {'red': 0, 'green': 0, 'blue': 0}
        _, game = game.split(': ')
        handfuls = game.split('; ')
        for handful in handfuls:
            balls = handful.split(', ')
            for ball_color in balls:
                num = int(''.join([x for x in ball_color if x.isdigit()]))
                for color in mins.keys():
                    if color in ball_color and num >= mins[color]:
                        mins[color] = num
        ans += mins['red'] * mins['green'] * mins['blue']
                
    return ans

assert(part_b(test=True) == 2286)
answer_b = part_b()
write_solution('day02', 'b', answer_b)
puzzle.answer_b = answer_b