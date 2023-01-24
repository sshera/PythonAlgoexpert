def riverSizes1(matrix):
    sizes = []
    for (x, y) in matrix:
        if (x, y) == 0:
            return 0
        if (x, y) == 1:
            if (x, y + 1) == 0 and (x + 1, y) == 0:
                return 1
            if (x, y + 1) == 0:
                pass

    riverSize = matrix
    sizes.append(riverSize)

    return sizes


def riverSizes2(list):
    sizes = []

    for i in list:
        if i == 0:
            return 0


# SOLUTION
def riverSizes(matrix):
    marked = set()
    rivers = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1 and (row, col) not in marked:
                cur_river_len = 1
                marked.add((row, col))
                stack = [(row, col)]

                while stack:
                    current = stack.pop()
                    neighbors = get_neighbors(current, matrix)
                    for n in neighbors:
                        y, x = n
                        if matrix[y][x] == 1 and (y, x) not in marked:
                            marked.add((y, x))
                            cur_river_len += 1
                            stack.append((y, x))

                rivers.append(cur_river_len)

    return rivers


def get_neighbors(pos, matrix):
    y, x = pos
    ns = []
    if x >= 1:  # left neighbor
        ns.append((y, x - 1))
    if x < len(matrix[0]) - 1:  # right neighbor
        ns.append((y, x + 1))
    if y >= 1:  # above neighbor
        ns.append((y - 1, x))
    if y < len(matrix) - 1:  # below neighbor
        ns.append((y + 1, x))

    return ns


river1 = [
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
]

river2 = [
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
]

print(riverSizes(river1))
print(riverSizes(river2))
