"""AoC 14, 2023: Parabolic Reflector Dish."""

# Standard library imports
import pathlib
import sys
import tomllib
from typing import List, Dict


INPUT_PATH = pathlib.Path(__file__).parent / "INPUT.toml"
INPUT_TOML: Dict[str, List[str]] = tomllib.loads(INPUT_PATH.read_text())
INPUT: List[str] = INPUT_TOML['input_data']

def parse_data(input_data):
    """Parse input."""
    return input_data.split('\n')

def line_length(data):
    return len(data[0])

def columns(line_len, data: List[str]) -> List[List[str]]:
    return [
        [
            line[i]
            for line in data
        ]
        for i in range(line_len)
    ]

def roller(column: List[str]) -> List[str]:
    for i, char in enumerate(column):
        match char:
            case 'O':
                column[i] = char
            case '#':
                column[i] = char
            case '.' if i == len(column) - 1:  # prevent index error
                column[i] = char
            case '.' if column[i+1] == 'O':
                column[i], column[i+1] = column[i+1], column[i]
                roller(column)
    return column

def observations(rolled_col):
    return [{key: 1 for key, value in enumerate(roll) if value == 'O'} for roll in rolled_col]

def recorder(obs):
    records = {}
    for ob in obs:
        for key, value in ob.items():
            records[key] = records.get(key, 0) + value
    return records

def load(line_len, record):
    loads = {line_len - key: value for key, value in record.items()}
    return sum(int(key)*value for (key, value) in loads.items())

def part1(data):
    """Solve part 1."""
    linel = line_length(data)
    cols = columns(linel, data)
    rolled = [roller(col) for col in cols]
    obs = [{key: 1 for key, value in enumerate(roll) if value == 'O'} for roll in rolled]
    record = recorder(obs)
    return load(linel, record)


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
