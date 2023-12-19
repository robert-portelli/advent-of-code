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

RIGHT = {'direction': (0, 1), 'heading': 'right', 'char': '>', }
DOWN = {'direction': (1, 0), 'heading': 'down', 'char': 'v', }
LEFT = {'direction': (0, -1), 'heading': 'left', 'char': '<', }
UP = {'direction': (-1, 0), 'heading': 'up', 'char': '^', }


ENCOUNTERS = {
    'right': {
        '.': RIGHT, '|': [UP, DOWN], '-': RIGHT, '/': UP, '\\': DOWN,
    },
    'down': {
        '.': DOWN, '|': DOWN, '-': [LEFT, RIGHT], '/': LEFT, '\\': RIGHT,
    },
    'left': {
        '.': LEFT, '|': [UP, DOWN], '-': LEFT, '/': DOWN, '\\': UP,
    },
    'up': {
        '.': UP, '|': UP, '-': [LEFT, RIGHT], '/': RIGHT, '\\': LEFT,
    },
}

status = {
    'row': 0,
    'col': 0,
    'assets': RIGHT,
}

tracker: Dict[str, List[str]] = {}

def encounter(tile):
    """
    encounter(grid[status['row'], status['col']], status['direction'])
    call encounter until the next tile is OB
    while next tile IB, call encounter with updated row and col and dir
    """
    match tile:
        case '.':
            # update tracker
            tracker[f"{status['row']}, {status['col']}"] = list(status['assets']['char'])

            # update the grid character from . to >, <, ^, or v
            grid[status['row'], status['col']] = status['assets']['char']

            # update ROW, COL to reflect next tile
            status['row'] += ENCOUNTERS[status['assets']['heading']]['.']['direction'][0]
            status['col'] += ENCOUNTERS[status['assets']['heading']]['.']['direction'][1]

        case '>' | '<' | '^' | 'v':
            # update the tracker
            tracker[f"{status['row']}, {status['col']}"].append(status['assets']['char'])

            # change this position's character to be len(chars in tracker for position)
            tile = len(tracker[f"{status['row']}, {status['col']}"])

            # update ROW, COL to reflect next tile
            status['row'] += ENCOUNTERS[status['assets']['heading']]['.']['direction'][0]
            status['col'] += ENCOUNTERS[status['assets']['heading']]['.']['direction'][1]

        case '|':
            splits = ENCOUNTERS[status['assets']['heading']]['|']
            for split in splits:
                status['row'] += split['direction'][0]
                status['col'] += split['direction'][1]
                status['assets'] = split
                encounter(grid[status['row'], status['col']])

        case '-':
            splits = ENCOUNTERS[status['assets']['heading']]['-']
            for split in splits:
                status['row'] += split['direction'][0]
                status['col'] += split['direction'][1]
                encounter(grid[status['row'], status['col']])

        case '/':
            # update ROW, COL to reflect next tile
            status['row'] += ENCOUNTERS[status['assets']['heading']]['/']['direction'][0]
            status['col'] += ENCOUNTERS[status['assets']['heading']]['/']['direction'][1]
            

        case '\\':
            # update ROW, COL to reflect next tile
            status['row'] += ENCOUNTERS[status['assets']['heading']]['\\']['direction'][0]
            status['col'] += ENCOUNTERS[status['assets']['heading']]['\\']['direction'][1]

 # Iterate through the array
while 0 <= status['row'] < grid.shape[0] and 0 <= status['col'] < grid.shape[1]:
    encounter(grid[status['row'], status['col']])
    print(grid)
