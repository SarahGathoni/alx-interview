#!/usr/bin/python3
"""
    A method that determines if all the boxes can be opened.
        - Prototype: def canUnlockAll(boxes)
        - boxes is a list of lists
        - Return True if all boxes can be opened, else return False
"""

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  
    # The first box is initially unlocked
    # Use a stack to keep track of boxes to explore
    boxes_to_unlock= [0]

    while boxes_to_unlock:
        box = boxes_to_unlock.pop()
        # Iterate through the keys in the current box
        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                boxes_to_unlock.append(key)
    # Check if all boxes are unlocked
    return all(unlocked)

