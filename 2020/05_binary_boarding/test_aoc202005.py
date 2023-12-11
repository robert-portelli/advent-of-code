"""Tests for AoC 5, 2020: Binary Boarding."""

# Standard library imports
import pathlib
from typing import List, Dict
import tomllib

# Third party imports
import aoc202005
import pytest

EXAMPLES_PATH = pathlib.Path(__file__).parent / "EXAMPLES.toml"
EXAMPLES_TOML: Dict[str, Dict[str, str]] = tomllib.loads(
    EXAMPLES_PATH.read_text()
    )
EXAMPLES_INPUT: List[str] = [
    example[1]['input_data']
    for example in EXAMPLES_TOML.items()
    ]

@pytest.fixture
def example1():
    return aoc202005.parse_data(EXAMPLES_INPUT)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202005.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [357, 567, 119, 820]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202005.part1(example1) == 820


def test_part2():
    """Test part 2 on manual input."""
    seat_ids = [3, 9, 4, 8, 5, 10, 7, 11]
    assert aoc202005.part2(seat_ids) == 6


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202005.part2(example2) == ...
