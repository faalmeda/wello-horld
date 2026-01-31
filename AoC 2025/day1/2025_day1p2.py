def move_count(step):
    if step:
        step_no = int(step[1:])
    else:
        return
    return -step_no if step[0] == 'L' else step_no

def main_day1p2(input_list, start_pos=0):
    passed_zero = 0
    
    if input_list:
        for i in input_list:
            steps = move_count(i)
            for i in range(abs(steps)):
                if steps < 0:
                    start_pos -= 1
                else:
                    start_pos += 1
                    
                if start_pos == 0 or start_pos % 100 == 0:
                    passed_zero += 1
        
        return passed_zero
    
    else:
        return 0
    
if __name__ == '__main__':
    puzzle = 'D:/0 Coding Projects/wello-horld/day1/adventday1.txt'
    
    with open(puzzle, 'r') as f:
        lines = f.read().splitlines()

    print(main_day1p2(lines,50))