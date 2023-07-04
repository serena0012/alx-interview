def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  # First box is initially unlocked
    keys = boxes[0]  # Start with the keys in the first box

    # Iterate through the keys and update unlocked_boxes accordingly
    while keys:
        key = keys.pop()
        if key < num_boxes and not unlocked_boxes[key]:
            unlocked_boxes[key] = True
            keys.extend(boxes[key])

    return all(unlocked_boxes)

