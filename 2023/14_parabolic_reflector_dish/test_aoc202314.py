"""Tests for AoC 14, 2023: Parabolic Reflector Dish."""

# Standard library imports
import pathlib
from typing import List, Dict
import tomllib

# Third party imports
import aoc202314
import pytest

EXAMPLES_PATH = pathlib.Path(__file__).parent / "EXAMPLES.toml"
EXAMPLES_TOML: Dict[str, Dict[str, str]] = tomllib.loads(
    EXAMPLES_PATH.read_text()
    )
EXAMPLES_INPUT: str = [
    example[1]['input_data']
    for example in EXAMPLES_TOML.items()
    ][0]

@pytest.fixture
def example1():
    return aoc202314.parse_data(EXAMPLES_INPUT)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202314.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ['O....#....', 'O.OO#....#', '.....##...', 'OO.#O....O', '.O.....O#.', 'O.#..O.#.#', '..O..#O..O', '.......O..', '#....###..', '#OO..#....']


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202314.part1(example1) == 136


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202314.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202314.part2(example2) == ...

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
    return column


if __name__ == '__main__':
    splits = aoc202314.parse_data(EXAMPLES_INPUT)
    first_column = [line[0] for line in splits]
    fourth_column = [line[3] for line in splits]
    roller(fourth_column)
    # completed = []
"""     def roller(splits):
        #rolled = []
        for line in splits:
            for i, char in enumerate(line):
                match char:
                    case '.' if line[i+1] == '0':
                        print('a blank followed by a rock')
                        line[i], line[i+1] = line[i+1], line[i]
                    case '#':
                        print('a cube')
                    case '0':
                        print('a round') """


        
    