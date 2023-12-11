"""AoC 1, 2019: Tyranny of the Rocket Equation."""

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
    return [int(line) for line in input_data]


def part1(data):
    """Solve part 1."""
    return sum(datum // 3 - 2 for datum in data)

def all_fuel(mass):
    """Calculate fuel while taking mass of the fuel into account.

    ## Example:

    >>> all_fuel(1969)
    966
    """
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + all_fuel(mass=fuel)

def part2(data):
    """Solve part 2."""
    return sum(all_fuel(mass) for mass in data)

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
