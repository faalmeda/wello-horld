# Advent 2025 Day 1

def move_count(step):
    if step: 
        step_no = int(step[1:])
    else:
        return
    return -step_no if step[0] == 'L' else step_no