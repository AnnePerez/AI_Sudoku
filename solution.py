assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Get all the boxes with two values
    boxes_with_two = [box for box in values.keys() if len(values[box]) == 2]
    
    # Loop through these boxes
    for box_with_two in boxes_with_two:
        
        # Get that box's values
        box_values = values[box_with_two]
        
        # Peers that have the same two values:
        same_peers = [peer for peer in peers[box_with_two] if values[peer] == box_values]
        
        # Peers that have the same two values:
        if len(same_peers) == 1:

            # Peers that have the same two values:
            box_with_two_peers = same_peers[0]
            
            # Get the peers of each box
            peers_1, peers_2 = peers[box_with_two], peers[box_with_two_peers] 
            
            # Get boxes that are peers of both
            peers_of_both = [peer2 for peer2 in peers_2 if peer2 in peers_1]    

            # For each "peer of both"
            for peer_of_both in peers_of_both:

                # Eliminate the values from box's values
                for value in box_values:
                
                    # Eliminate the values from box's values
                    values[peer_of_both] = values[peer_of_both].replace(value, '')

            print("Eliminated", box_values, "from", peers_of_both, "using naked twins.")    
    return values
    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]
    # pass
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def grid_values(grid, blanks='.'):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(blanks)
        elif c in all_digits:
            values.append(c)
    return dict(zip(boxes, values))
    # pass

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return
    # pass

# grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'    
# values_su = grid_values(grid, blanks='123456789')

# grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'


# before_naked_twins_2 = {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9',
#                             'A9': '1', 'B1': '6', 'B2': '9', 'B3': '8', 'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237',
#                             'B8': '5', 'B9': '237', 'C1': '23', 'C2': '5', 'C3': '1', 'C4': '23', 'C5': '379',
#                             'C6': '2379', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8', 'D2': '17', 'D3': '9',
#                             'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
#                             'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9',
#                             'F1': '4', 'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6',
#                             'F8': '8', 'F9': '257', 'G1': '1', 'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345',
#                             'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7', 'H2': '2', 'H3': '4', 'H4': '9',
#                             'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3', 'I3': '5',
#                             'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'}


# display(before_naked_twins_2)
# after_naked_twins_2 = naked_twins(before_naked_twins_2)
# display(after_naked_twins_2)

def eliminate(values):
    # Get all the solved boxes
    solved_boxes = [box for box in values.keys() if len(values[box]) == 1]

    # For a given solved box...
    for box in solved_boxes:
        
        # ...get the value in the box
        digit = values[box]
        
        # ...and for each of that box's "peers"...
        for peer in peers[box]:
            
            # ...delete that value from the possible values in that box
            values[peer] = values[peer].replace(digit,'')
            print("Eliminated ", digit, "from box ", peer, " using the 'eliminate' strategy.")
            
    return values

def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1 and values[dplaces[0]] != digit:
                values[dplaces[0]] = digit
                print("Placed value ", digit, " in box ", dplaces[0])
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Naked Twins Strategy        
        values = naked_twins(values)
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    pass

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    print("Displaying the grid: ")
    grid_vals = grid_values(grid, blanks='.')
    display(grid_vals)
    print("Solving the puzzle: ")
    grid_vals_puzzle = grid_values(grid, blanks='123456789')
    final_values = reduce_puzzle(grid_vals_puzzle)
    display(final_values)

# solve(grid)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
