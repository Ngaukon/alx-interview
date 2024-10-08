#!/usr/bin/python3
'''A module for working with lockboxes.
Each box contains keys (indices) to other boxes, and the goal
is to determine if all the boxes can be unlocked.
'''

def canUnlockAll(boxes):
    '''Determines if all boxes can be unlocked given a list of boxes, 
    where each box contains a set of keys (indices) to other boxes. 
    The first box (box 0) is always unlocked.
    
    Args:
        boxes (list of list of int): A list of boxes, each containing 
        keys (indices) to other boxes.
    
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''
    n = len(boxes)  # Total number of boxes
    seen_boxes = set([0])  # Set of boxes that have been unlocked
    unseen_boxes = set(boxes[0]).difference(set([0]))  # Keys to unlock new boxes
    
    # While there are still boxes that haven't been checked
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()  # Take a key to a new box
        
        # Skip if the key is invalid (out of bounds or invalid index)
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        
        # If the box hasn't been unlocked yet
        if boxIdx not in seen_boxes:
            # Add the keys from the new box to unseen_boxes for future unlocking
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)  # Mark the box as unlocked
    
    # Return True if all boxes have been unlocked
    return n == len(seen_boxes)
