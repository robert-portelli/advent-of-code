"""Tests for AoC 1, 2019: Tyranny of the Rocket Equation."""

# Standard library imports
import pathlib
from typing import List, Dict
import tomllib

# Third party imports
import aoc201901
import pytest

EXAMPLES_PATH = pathlib.Path(__file__).parent / "EXAMPLES.toml"
EXAMPLES_TOML: Dict[str, Dict[str, str]] = tomllib.loads(
    EXAMPLES_PATH.read_text()
    )
EXAMPLES_INPUT: List[str] = [
    example[1]['input_data']
    for example in EXAMPLES_TOML.items()
    ]
EXAMPLES_ANSWER_A: List[str] = [
    example[1]['answer_a']
    for example in EXAMPLES_TOML.items()
]

@pytest.fixture
def example1():
    return aoc201901.parse_data(EXAMPLES_INPUT)



def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [12, 14, 1969, 100756]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201901.part1(example1) == 2 + 2 + 654 + 33583


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201901.part2(example1) == 2 + 2 + 966 + 50346