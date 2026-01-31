# Advent 2025 Day 1

def move_count(step):
    if step: 
        step_no = int(step[1:])
    else:
        return
    return -step_no if step[0] == 'L' else step_no

def main_day1p1(input_list, start_pos=0):
    at_zero = 0
    if input_list:
        for i in input_list:
            start_pos += move_count(i)
            if start_pos == 0:
                at_zero += 1
            elif start_pos % 100 == 0:
                at_zero += 1
        return at_zero
    else:
        return 0
    
if __name__ == '__main__':
    puzzle = 'D:/0 Coding Projects/wello-horld/day1/adventday1.txt'
    
    with open('adventday1.txt', 'r') as f:
        lines = f.read().splitlines()

    print(main_day1p1(lines))