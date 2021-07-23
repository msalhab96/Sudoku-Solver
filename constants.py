from utils import *
####### Constants ######
LENGTH = 9
COLS = [str(i) for i in range(1,LENGTH + 1)]
ROWS = [chr(i) for i in range(65, 65 + LENGTH)]
BOXES = [row + col for row in ROWS for col in COLS]
PEERS = {box: get_peers_by_index(BOXES, index) for index, box in enumerate(BOXES)}
NULL_SYM = '.'

if __name__ == '__main__':
    # print(BOXES)
    print(PEERS)
    # print(len(PEERS['A2']))
    # print(sorted(GET_ROW_PEERS(BOXES, 43)))
    # print(sorted(GET_COLS_PEERS(BOXES, 0)))
    # print(sorted(GET_SQUARE_PEERS(BOXES, 75)))
    # print(GET_SQUARE_START(37))
    # for key, val in PEERS.items():
    #     if len(PEERS[key]) != 21:
    #         print(key)