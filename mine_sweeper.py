import numpy as np


class Minesweeper:
    def __init__(self, array):
        self.__set_array(array)
        self.__set_rowCount_and_colCount()
        self.__mines_list = []
        self.__find_mines()
        self.__hint_numbers_generator()

    def __str__(self):
        output_str = ''
        for i in range(0, self.__rowCount):
            for j in range(0, self.__colCount):
                output_str += str(self.__array[i, j])
            output_str += "\n"
        return output_str

    def __set_rowCount_and_colCount(self):
        self.__rowCount, self.__colCount = self.__array.shape

    def __set_array(self, array):
        if isinstance(array, np.ndarray):
            self.__array = array

    def __find_mines(self):
        self.__mines_list = np.where(self.__array == '*')

    def __hint_numbers_generator(self):
        if len(self.__mines_list[0]) != self.__array.size:
            if len(self.__mines_list) == 0:
                self.__array[np.where(self.__array == '.')] = '0'
            elif len(self.__mines_list[0]) <= (self.__array.size - len(self.__mines_list[0])):
                self.__hint_number_generator_surrounding_mine()
            else:
                self.__hint_number_generator_counting_mines()

    def __hint_number_generator_surrounding_mine(self):
        self.__array[np.where(self.__array == '.')] = '0'
        rows, cols = self.__mines_list[0], self.__mines_list[1]
        for i in range(0, len(rows)):
            row, col = rows[i], cols[i]

            upper_right = self.__upper_right(row, col)
            if upper_right is not None and upper_right[0] != '*':
                self.__array[upper_right[1], upper_right[2]] = str(int(upper_right[0])+1)

            upper_left = self.__upper_left(row, col)
            if upper_left is not None and upper_left[0] != '*':
                self.__array[upper_left[1], upper_left[2]] = str(int(upper_left[0])+1)

            up = self.__up(row, col)
            if up is not None and up[0] != '*':
                self.__array[up[1], up[2]] = str(int(up[0])+1)

            right = self.__right(row, col)
            if right is not None and right[0] != '*':
                self.__array[right[1], right[2]] = str(int(right[0])+1)

            left = self.__left(row, col)
            if left is not None and left[0] != '*':
                self.__array[left[1], left[2]] = str(int(left[0])+1)

            down_right = self.__down_right(row, col)
            if down_right is not None and down_right[0] != '*':
                self.__array[down_right[1], down_right[2]] = str(int(down_right[0])+1)

            down_left = self.__down_left(row, col)
            if down_left is not None and down_left[0] != '*':
                self.__array[down_left[1], down_left[2]] = str(int(down_left[0])+1)

            down = self.__down(row, col)
            if down is not None and down[0] != '*':
                self.__array[down[1], down[2]] = str(int(down[0])+1)

    def __hint_number_generator_counting_mines(self):
        not_mine_list = np.where(self.__array == '.')
        rows, cols = not_mine_list[0], not_mine_list[1]
        for i in range(0, len(rows)):
            value = 0
            row, col = rows[i], cols[i]
            upper_right = self.__upper_right(row, col)
            if upper_right is not None and str(upper_right[0]) == '*':
                value += 1
            upper_left = self.__upper_left(row, col)
            if upper_left is not None and str(upper_left[0]) == '*':
                value += 1
            up = self.__up(row, col)
            if up is not None and str(up[0]) == '*':
                value += 1
            right = self.__right(row, col)
            if right is not None and str(right[0]) == '*':
                value += 1
            left = self.__left(row, col)
            if left is not None and str(left[0]) == '*':
                value += 1
            down_right = self.__down_right(row, col)
            if down_right is not None and str(down_right[0]) == '*':
                value += 1
            down_left = self.__down_left(row, col)
            if down_left is not None and str(down_left[0]) == '*':
                value += 1
            down = self.__down(row, col)
            if down is not None and str(down[0]) == '*':
                value += 1
            if self.__array[row, col] != '*':
                self.__array[row, col] = str(value)

    def __upper_left(self, row, col):
        if 0 <= row - 1 < self.__rowCount and 0 <= col - 1 < self.__colCount:
            return self.__array[row - 1, col - 1], row - 1, col - 1

    def __upper_right(self, row, col):
        if 0 <= row - 1 < self.__rowCount and 0 <= col + 1 < self.__colCount:
            return self.__array[row - 1, col + 1], row - 1, col + 1

    def __down_left(self, row, col):
        if 0 <= row + 1 < self.__rowCount and 0 <= col - 1 < self.__colCount:
            return self.__array[row + 1, col - 1], row + 1, col - 1

    def __down_right(self, row, col):
        if 0 <= row + 1 < self.__rowCount and 0 <= col + 1 < self.__colCount:
            return self.__array[row + 1, col + 1], row + 1, col + 1

    def __up(self, row, col):
        if 0 <= row - 1 < self.__rowCount:
            return self.__array[row-1, col], row-1, col

    def __down(self, row, col):
        if 0 <= row + 1 < self.__rowCount:
            return self.__array[row+1, col], row+1, col

    def __right(self, row, col):
        if 0 <= col + 1 < self.__colCount:
            return self.__array[row, col+1], row, col+1

    def __left(self, row, col):
        if 0 <= col - 1 < self.__colCount:
            return self.__array[row, col-1], row, col-1


if __name__ == '__main__':
    input_file = open('mines.txt', 'r')
    output_file = open('minesweeper_output.txt', 'w')
    r, c = input_file.readline().split()
    count = 0
    while int(r) != 0 and int(c) != 0:
        mine_array = np.zeros((int(r), int(c)), str)
        for val in range(0, int(r)):
            mine_array[val] = list(input_file.readline().strip('\n'))
        mine = Minesweeper(mine_array)
        count += 1
        output_file.write('Field #' + str(count) + ':\n' + str(mine) + '\n')
        r, c = input_file.readline().split()
