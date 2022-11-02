import numpy as np
import matplotlib.pyplot as plt
import cell_happines_calc as mf

# Параметры алгоритма Шеллинга
world_size = 20  # размер мира (квадрат nxn)
p_blue = 0.45  # % синих клеток
p_red = 0.45  # % красных клеток
num_for_happy = 2  # клетка счастлива, если у нее 2 и более соседа такого же цвета
max_num_iter = 100

# Generate initial world генерация исходного мира
num_elements = world_size ** 2
Color_map_flat = np.zeros(num_elements)  # создаем нулевую матрицу
num_blue = round(num_elements * p_blue)  # кол-во синих
num_red = round(num_elements * p_red)  # кол-во красных
Color_map_flat[0:num_blue] = -0.6
Color_map_flat[num_blue: num_red + num_blue] = 0.6  # red
np.random.shuffle(Color_map_flat)  # перемешиваем
Color_map = Color_map_flat.reshape((world_size, world_size))


# Итеративно перемещаем случайные несчастливые в случайные пустые
fig, ax = plt.subplots()
happiness_map = np.zeros_like(Color_map)

for iteration in range(max_num_iter):
    # Calculate happiness map
    for i, _ in enumerate(happiness_map):
        for j, _ in enumerate(happiness_map[i]):
            happiness_map[i, j] = mf.cell_happines(Color_map, i, j, num_for_happy)  # карта "счастливых" клеток
    unhappy_x, unhappy_y = np.where((happiness_map == 0) & (Color_map != 0))
    empty_x, empty_y = np.where(Color_map == 0)

    if len(unhappy_x) != 0:  # перемещаем рандомную несчастливую клетку в пустую
        unhappy_to_move_idx = np.random.randint(0, len(unhappy_x))
        empty_to_move_idx = np.random.randint(0, len(empty_x))
        Color_map[empty_x[empty_to_move_idx], empty_y[empty_to_move_idx]] = \
            Color_map[unhappy_x[unhappy_to_move_idx], unhappy_y[unhappy_to_move_idx]]
        Color_map[unhappy_x[unhappy_to_move_idx], unhappy_y[unhappy_to_move_idx]] = 0

        # Plot
        ax.cla()  # clear
        ax.set_title("Iteration {}".format(iteration + 1))
        plt.imshow(Color_map, cmap='bwr', vmin=-1, vmax=1)
        plt.pause(0.5)
    else:
        print("Счастливых клеток не осталось после", iteration, "итераций!")
        print("No unhappy cells!!!")
        break
