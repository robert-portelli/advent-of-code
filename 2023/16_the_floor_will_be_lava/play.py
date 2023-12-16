import numpy as np
from typing import Dict, List

# Sample 2D array
grid = np.array([
    ['.', '|', '.', '.', '.', '\\', '.', '.', '.', '.'],
    ['|', '.', '-', '.', '\\', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '|', '-', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '|', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '\\'],
    ['.', '.', '.', '.', '/', '.', '\\', '\\', '.', '.'],
    ['.', '-', '.', '-', '/', '.', '.', '|', '.', '.'],
    ['.', '|', '.', '.', '.', '.', '-', '|', '.', '\\'],
    ['.', '.', '/', '/', '.', '|', '.', '.', '.', '.']
], dtype='<U1')


RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)

BEAMS = {
    'right': {'char': '>', },
    'down': {'char': 'v', },
    'left': {'char': '<', },
    'up': {'char': '^', },
}
ENCOUNTERS = {
    'right': {
        '.': RIGHT, '|': [(UP, 'up'), (DOWN, 'down')], '-': RIGHT, '/': UP, '\\': DOWN,
    },
    'down': {
        '.': DOWN, '|': DOWN, '-': [(LEFT, 'left'), (RIGHT, 'right')], '/': LEFT, '\\': RIGHT,
    },
    'left': {
        '.': LEFT, '|': [(UP, 'up'), (DOWN, 'down')], '-': LEFT, '/': DOWN, '\\': UP,
    },
    'up': {
        '.': UP, '|': UP, '-': [(LEFT, 'left'), (RIGHT, 'right')], '/': RIGHT, '\\': LEFT,
    },
}

status: Dict[str, int | str] = {
    'row': 0,
    'col': 0,
    'direction': 'right',
}

tracker: Dict[str, List[str]] = {}

def encounter(tile, heading):
    """
    encounter(grid[status['row'], status['col']], status['direction'])
    call encounter until the next tile is OB
    while next tile IB, call encounter with updated row and col and dir
    """
    match tile:
        case '.':
            # update tracker
            tracker[f"{status['row']}, {status['col']}"] = list(BEAMS[heading]['char'])

            # change the grid character from . to >, <, ^, or v
            grid[status['row'], status['col']] = BEAMS[heading]['char']

            # update ROW, COL to reflect next tile
            status['row'] += ENCOUNTERS[heading]['.'][0]
            status['col'] += ENCOUNTERS[heading]['.'][1]

        case '>' | '<' | '^' | 'v':
            # update the tracker
            tracker[f"{status['row']}, {status['col']}"].append(BEAMS[heading]['char'])

            # change this position's character to be len(chars in tracker for position)
            tile = len(tracker[f"{status['row']}, {status['col']}"])

            # update ROW, COL to reflect next tile
            status['row'] += ENCOUNTERS[heading]['.'][0]
            status['col'] += ENCOUNTERS[heading]['.'][1]

        case '|':
            # update ROW, COL to reflect next tile
            # write a function to handle splitter
            """ for split in ENCOUNTERS[heading]['|']:
                status['direction'] = BEAMS[split]
                encounter() """
            pass

        case '-':
            # write a function to handle splitter
            print('a hyphen')

        case '/':
            # update ROW, COL to reflect next tile
            status['row'] += ENCOUNTERS[heading]['/'][0]
            status['col'] += ENCOUNTERS[heading]['/'][1]

        case '\\':
            # update ROW, COL to reflect next tile
            status['row'] += ENCOUNTERS[heading]['\\'][0]
            status['col'] += ENCOUNTERS[heading]['\\'][1]


""" # Iterate through the array
while 0 <= status['row'] < grid.shape[0] and 0 <= status['col'] < grid.shape[1]:
    encounter(grid[status['row'], status['col']], status['direction']) """
