"""AoC 15, 2023: Lens Library."""

# Standard library imports
import pathlib
import sys
import tomllib
from typing import List, Dict


INPUT_PATH = pathlib.Path(__file__).parent / "INPUT.toml"
INPUT_TOML: Dict[str, List[str]] = tomllib.loads(INPUT_PATH.read_text())
INPUT: List[str] = INPUT_TOML['input_data']
CURRENT_VALUE = 0

def parse_data(input_data):
    """Parse input."""
    return input_data.replace('\n', '').split(',')

def hash_algorithm(input_str: str) -> int:
    current_value = 0

    for char in input_str:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256

    return current_value

def part1(data):
    """Solve part 1."""
    # Calculate the sum of the HASH algorithm results for each step
    hash_sum = sum(hash_algorithm(step) for step in data)

    return hash_sum


LIGHT_BOX: Dict[int, List[tuple]] = {i: [] for i in range(256)}


def lens_sorter(strings: List[str]):
    for string in strings:
        if '=' in string:
            ass_op(string)
        else:
            neg_op(string)


def ass_op(string):
    label, power = string.split('=')
    box = hash_algorithm(label)
    lens = (str(label), int(power))
    for i, boxed_lens in enumerate(LIGHT_BOX[box]):
        if lens == boxed_lens:
            LIGHT_BOX[box][i] = lens
        else:
            LIGHT_BOX[box].append(lens)


def neg_op(string):
    label = string.split('-')
    box = hash_algorithm(label)
    lens = (label,)
    for i, boxed_lens in enumerate(LIGHT_BOX[box]):
        if lens[0] in LIGHT_BOX[box][i][0]:
            LIGHT_BOX[box].remove(boxed_lens)


def focusing_power(light_box: Dict[int, List[tuple]]) -> int:
    total: int = 0
    for box, lens_box in light_box.items():
        box_power = 1 + int(box)
        for i, boxed_lens in enumerate(lens_box):
            index_power = i + 1
            focal_power = boxed_lens[1]
            total += box_power * index_power * focal_power

    return total


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(INPUT)
        print("\n".join(str(solution) for solution in solutions))
