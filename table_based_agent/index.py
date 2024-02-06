# Welcome to Table-Based Agent
# Here, I intend to apply the concept Table-Based Agent
# into the code to link between the conceptual view and 
# coding. Have fun.........

# Here I identified two vars, to be places that the agent
# will go through.

A = "A"
B = "B"

# In this list, we shall store all events that happen 
percepts = []

# This table is the core of this program since it is a dictionary
# of nested tuples. I used tuples over lists due to their immutability
# and fixed hash code, making them better suited to serve as a key.

"""
The 'table' dictionary maps sequences of percepts to 
corresponding actions.
It is a key component of 
the table-driven agent 
implementation.
"""
table = {
    ((A, 'Clean'),): 'Right',
    ((A, 'Dirty'),): 'Clean',
    ((B, 'Clean'),): 'Left',
    ((B, 'Dirty'),): 'Clean',
    ((A, 'Dirty'), (A, 'Clean')): 'Right',
    ((A, 'Dirty'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Dirty')): 'Clean',
    ((A, 'Dirty'), (A, 'Clean'), (B, 'Dirty')): 'Clean',
    ((A, 'Clean'), (A, 'Clean'), (A, 'Clean')): 'Right'
}

def LOOKUP(percepts, table):
    """
    Performs a table lookup to determine the action based on the given set of percepts.

    Parameters:
    - percepts (list): A list of percepts representing the current state.
    - table (dict): A dictionary mapping sequences of percepts to corresponding actions.

    Returns:
    str or None: The action determined by the table lookup, or None if no action is found.
    """
    action = table.get(tuple(percepts))
    return action

def TABLE_DRIVEN_AGENT(percept):
    """
    Updates the list of percepts and determines the action based on the current set of percepts.

    Parameters:
    - percept: A single percept representing the current observation.

    Returns:
    str or None: The action determined by the table lookup, or None if no action is found.
    """
    percepts.append(percept)
    action = LOOKUP(percepts, table)
    return action

def run():
    print('Action\tPercepts')
    print(TABLE_DRIVEN_AGENT((A ,'Dirty')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((A ,'Clean')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((B ,'Dirty')), '\t', percepts)

run()
