from random import randint


class Map:
    GRID_SIZE_x = 10
    GRID_SIZE_y = 30

    def create_grid(self, size_x, size_y):
        return [['-' for _ in range(size_y)] for _ in range(size_x)]

    def grid(self, grid, player_pos_x, player_pos_y):
        grid_with_player = [row[:] for row in grid]  # Faire une copie de la grille
        x = player_pos_x
        y = player_pos_y
        grid_with_player[y][x] = 'x'
        for row in grid_with_player:
            print(' '.join(row))
        print("\n")



map = Map()

print(map.grid(map.create_grid(map.GRID_SIZE_x, map.GRID_SIZE_y), 3, 1))