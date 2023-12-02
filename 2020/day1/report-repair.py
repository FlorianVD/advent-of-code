import functools

with open('input.txt') as f:
    puzzle_input = list(f.readlines())

sum_result = 2020

def pretty_print(nums):
    print(f'Numbers {nums}')
    print('Result: ', functools.reduce(lambda a,b: a * b, nums, 1))

def part_one(required_sum, inputs):
    """
    Given a list of numbers, find the 2 numbers which sum up to '2020'.
    Multiply those numbers to receive your reward.
    """
    nums = []

    result_map = {}
    i = 0
    while len(nums) != 2 and i < len(inputs) - 1:
        cur_num = int(inputs[i])
        rest = required_sum - cur_num
        if (rest_idx := result_map.get(rest, None)) is not None:
            nums.append(int(inputs[rest_idx]))
            nums.append(int(inputs[i]))
        else: result_map[cur_num] = i
        i += 1

    return nums

def part_two(required_sum, inputs):
    """
    Same as above, but you have to find 3 numbers instead
    """
    nums = []

    i = 0
    while len(nums) != 3 and i < len(inputs) - 1:
        cur_num = int(inputs[i])
        rest = required_sum - cur_num
        found_nums = part_one(rest, inputs)
        if len(found_nums) > 0:
            nums = found_nums
            nums.append(cur_num)
        i += 1
    
    return nums

pretty_print(part_one(sum_result, puzzle_input)) # Correct -> 956091
pretty_print(part_two(sum_result, puzzle_input)) # Correct -> 79734368
