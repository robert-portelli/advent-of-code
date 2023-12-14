"""Tests for AoC 5, 2021: Hydro Thermal Venture."""

# Standard library imports
import pathlib
from typing import List, Dict
import tomllib

# Third party imports
import aoc202105
import pytest

EXAMPLES_PATH = pathlib.Path(__file__).parent / "EXAMPLES.toml"
EXAMPLES_TOML: Dict[str, Dict[str, str]] = tomllib.loads(
    EXAMPLES_PATH.read_text()
    )
EXAMPLE_INPUT: str = [
    example[1]['input_data']
    for example in EXAMPLES_TOML.items()
    ][0]

EXAMPLE_MANUAL = '2,0 -> 0,2\n0,2 -> 2,2\n0,0 -> 0,2\n0,0 -> 2,2'

@pytest.fixture
def example1():
    return aoc202105.parse_data(EXAMPLE_MANUAL)


@pytest.fixture
def example2():
    return aoc202105.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        (2, 0, 0, 2),
        (0, 2, 2, 2),
        (0, 0, 0, 2),
        (0, 0, 2, 2),
    ]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202105.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202105.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202105.part2(example2) == ...
