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


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202314.part2(example1) == 64


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202314.part2(example2) == ...



""" if __name__ == '__main__':
    splits = aoc202314.parse_data(EXAMPLES_INPUT)
    first_column = [line[0] for line in splits]
    fourth_column = [line[3] for line in splits]  # {0: 1}
    column = roller(fourth_column)
    record = recorder(column)
    for key, value in record.items():
        RECORDS[key] = RECORDS.get(key, 0) + value """
