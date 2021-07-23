from math import sqrt

LENGTH = 9

get_row_peers = lambda boxes, index: set(boxes[
    LENGTH * (index // LENGTH): LENGTH * (index // LENGTH + 1)
    ])

get_cols_peers = lambda boxes, index: {
    boxes[index % LENGTH + LENGTH * i] 
    for i in range(LENGTH)
}

get_normalized = lambda index: index - index % int(sqrt(LENGTH))

get_square_start = lambda index: \
    get_normalized(index // LENGTH) * LENGTH + get_normalized(index % LENGTH)

get_square_elem = lambda boxes, index: \
    [boxes[
        get_square_start(index) + i * LENGTH : get_square_start(index) + int(sqrt(LENGTH)) + i * LENGTH
        ] for i in range(int(sqrt(LENGTH)))]


get_square_peers = lambda boxes, index: set(sum(get_square_elem(boxes, index), []))

get_peers_by_index = lambda boxes, index: \
    get_row_peers(boxes, index).union(
        get_square_peers(boxes, index), 
        get_cols_peers(boxes, index)
        )