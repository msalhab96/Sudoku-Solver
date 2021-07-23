from typing import Counter
from utils import *
from constants import *

def decode(board_string: str) -> dict:
    values = {
        box: board_string[index] for index, box in enumerate(BOXES)
        }
    return values

def encode(board: dict) -> str:
    return ''.join([board[box] for box in BOXES])

def set_nums(board: dict) -> dict:
    nums = '123456789'
    for key, value in board.items():
        if value == NULL_SYM:
            board[key] = nums
    return board

def apply_elimination(board: dict) -> dict:
    temp_board = board.copy()
    for key, value in board.items():
        if len(value) == 1:
            for peer in PEERS[key]:
                if (key != peer) and len(temp_board[peer]) != 1:
                    temp_board[peer] = temp_board[peer].replace(value, '')
    return temp_board

def get_frequency(peers: list, board: dict) -> dict:
    frequency = dict()
    nums = '123456789'
    for peer in peers:
        for num in nums:
            if num in board[peer]:
                if num in frequency:
                    frequency[num] += 1
                else:
                    frequency[num] = 1
    return frequency

def apply_constraint(board: dict) -> dict:
    counter = {key: get_frequency(PEERS[key], board) for key in board.keys() if len(board[key]) != 1}
    # print(counter)
    for key, freq in counter.items():
        for num, count in freq.items():
            if count == 1:
                for peer in PEERS[key]:
                    if num in board[peer]:
                        board[peer] = num
                        break
    return board

def render(board_string: str) -> None:
    for i in range(LENGTH):
        print('  '.join(board_string[i*LENGTH: (i+1)*LENGTH]))

def solve_without_search(board_string: str, max_iter: int = 100, trials: int = 5) -> str:
    print('new iteration')
    if trials == 0:
        return board_string
    result = decode(board_string)
    result = set_nums(result)
    for _ in range(max_iter):
        result = apply_constraint(result)
        result = apply_elimination(result)
        if sum([len(item) for item in result.values()]) == 81:
            return encode(result)
    else:
        solve_without_search(board_string, max_iter=max_iter, trials=trials-1)

# def search(board: dict):
#     pass


if __name__ == '__main__':
    x = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    render(solve_without_search(x))
