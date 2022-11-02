def cell_happines(world, i, j, num_same_for_happiness):
    cur_happy = 0
    cur_cell_value = world[i, j]
    x, y = world.shape
    if j + 1 < y:
        if cur_cell_value == world[i, j + 1]:
            cur_happy += 1

    if j - 1 >= 0:
        if cur_cell_value == world[i, j - 1]:
            cur_happy += 1

    if (i + 1 < x) & (j - 1 >= 0):
        if cur_cell_value == world[i + 1, j - 1]:
            cur_happy += 1

    if i + 1 < x:
        if cur_cell_value == world[i + 1, j]:
            cur_happy += 1

    if (i + 1 < x) & (j + 1 < y):
        if cur_cell_value == world[i + 1, j + 1]:
            cur_happy += 1

    if (i - 1 >= 0) & (j - 1 >= 0):
        if cur_cell_value == world[i - 1, j - 1]:
            cur_happy += 1

    if (i - 1 >= 0) & (j + 1 < y):
        if cur_cell_value == world[i - 1, j + 1]:
            cur_happy += 1

    if i - 1 >= 0:
        if cur_cell_value == world[i - 1, j]:
            cur_happy += 1

    if cur_happy >= num_same_for_happiness:  # Hitler's inequality
        return True
    return False
