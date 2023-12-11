"""AoC 5, 2020: Binary Boarding."""

# Standard library imports
import pathlib
import sys
import tomllib
from typing import List, Dict


INPUT_PATH = pathlib.Path(__file__).parent / "INPUT.toml"
INPUT_TOML: Dict[str, List[str]] = tomllib.loads(INPUT_PATH.read_text())
INPUT: List[str] = INPUT_TOML['input_data']

BP2BINARY = str.maketrans({"F": "0", "B": "1", "L": "0", "R": "1"})


def parse_data(puzzle_input):
    """Parse input."""
    return [
        int(bp.translate(BP2BINARY), base=2)
        for bp in puzzle_input
    ]


def part1(data):
    """Solve part 1."""
    return max(data)


def part2(data):
    """Solve part 2."""
    all_ids = set(range(min(data), max(data) + 1))
    return (all_ids - set(data)).pop()


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
