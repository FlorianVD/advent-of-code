with open('input.txt') as f:
    puzzle_input = list(f.readlines())

sum_result = 2020

def part_one():
    num_1, num_2 = -1, -1

    result_map = {}
    i = 0
    while num_1 == -1 and num_2 == -1 or i > len(puzzle_input) - 1:
        cur_num = int(puzzle_input[i])
        rest = sum_result - cur_num
        if (rest_idx := result_map.get(rest, None)) is not None:
            num_1 = int(puzzle_input[rest_idx])
            num_2 = int(puzzle_input[i])
        else: result_map[cur_num] = i 
        i += 1

    print(f'num_1: {num_1}, num_2: {num_2}')
    print('Result: ', num_1 * num_2)

part_one()