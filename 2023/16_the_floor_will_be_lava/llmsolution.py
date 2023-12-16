def count_energized_tiles(contraption):
    # Convert the contraption string to a 2D NumPy array
    grid = np.array([list(line) for line in contraption.split('\n')])

    # Initialize the beam's position and direction
    row, col, direction = 0, 0, 'right'

    # Set of energized tiles
    energized_tiles = set()

    while 0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]:
        current_char = grid[row, col]

        # Update the energized_tiles set
        energized_tiles.add((row, col))

        # Move to the next position based on the character
        if current_char == '.':
            # Empty space, continue in the same direction
            row, col = move(row, col, direction)
        elif current_char in {'/', '\\'}:
            # Mirror, reflect the beam
            direction = reflect(direction, current_char)
            row, col = move(row, col, direction)
        elif current_char in {'|', '-'}:
            # Splitter, handle splitting
            row, col = split(row, col, direction)

    # Return the count of energized tiles
    return len(energized_tiles)

def move(row, col, direction):
    # Move to the next position based on the direction
    match direction:
        case 'up':
            return row - 1, col
        case 'down':
            return row + 1, col
        case 'left':
            return row, col - 1
        case 'right':
            return row, col + 1

def reflect(direction, mirror):
    # Reflect the beam based on the mirror type
    if mirror == '/':
        match direction:
            case 'up':
                return 'right'
            case 'down':
                return 'left'
            case 'left':
                return 'down'
            case 'right':
                return 'up'
    elif mirror == '\\':
        match direction:
            case 'up':
                return 'left'
            case 'down':
                return 'right'
            case 'left':
                return 'up'
            case 'right':
                return 'down'

def split(row, col, direction):
    # Split the beam based on the splitter type
    if direction in {'up', 'down'}:
        return row, col  # Pass through the splitter
    elif direction == 'left':
        return row, col - 1  # Split to the left
    elif direction == 'right':
        return row, col + 1  # Split to the right