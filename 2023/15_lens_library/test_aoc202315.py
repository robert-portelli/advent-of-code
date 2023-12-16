"""Tests for AoC 15, 2023: Lens Library."""

# Standard library imports
import pathlib
from typing import List, Dict
import tomllib

# Third party imports
import aoc202315
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
    return aoc202315.parse_data(EXAMPLES_INPUT)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202315.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ['rn=1', 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7']


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202315.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202315.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202315.part2(example2) == ...

data = aoc202315.parse_data(EXAMPLES_INPUT)

LIGHT_BOX: Dict[int, List[tuple]] = {i: [] for i in range(256)}

def lens_sorter(strings: List[str]):
    for string in strings:
        if '=' in string:
            ass_op(string)
        else:
            neg_op(string)

def ass_op(string):
    label, power = string.split('=')
    box = aoc202315.hash_algorithm(label)
    lens = (str(label), int(power))
    if not LIGHT_BOX[box]:
        LIGHT_BOX[box].append(lens)
    else:
        found_match = False
        for i, boxed_lens in enumerate(LIGHT_BOX[box]):
            if lens[0] == boxed_lens[0]:
                LIGHT_BOX[box][i] = lens
                found_match = True
                break

        if not found_match:
            LIGHT_BOX[box].append(lens)

def neg_op(string):
    label = string.replace('-', '')
    box = aoc202315.hash_algorithm(label)
    lens = (label,)

    found_match = False
    for i, boxed_lens in enumerate(LIGHT_BOX[box]):
        if lens[0] in LIGHT_BOX[box][i][0]:
            found_match = True
            LIGHT_BOX[box].remove(boxed_lens)
            break

    if found_match:
        # Move remaining lenses forward
        LIGHT_BOX[box] = [l for l in LIGHT_BOX[box] if l[0] != label]

def focusing_power(light_box: Dict[int, List[tuple]]) -> int:
    total: int = 0
    for box, lens_box in light_box.items():
        box_power = 1 + int(box)
        for i, boxed_lens in enumerate(lens_box):
            index_power = i + 1
            focal_power = boxed_lens[1]
            total += box_power * index_power * focal_power

    return total



if __name__ == '__main__':
    lens_sorter(data)






