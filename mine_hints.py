import numpy as np
import time
start_time = time.time()

class Minesweeper:
    """
    Given an input array 4 4 :
    *...
    ....
    .*..
    ....
    (generates hints number adjacent to the mines)
    updates the array as:
    *100
    2210
    1*10
    1110

    """
    def __init__(self, array):
        self.__set_array(array)
        self.__set_rowCount_and_colCount()
        self.__not_mine_list = []
        self.__find_not_mines()
        self.__update_hints()

    def __str__(self):
        """ return the string representation of the array after the hint numbers are updated"""
        output_str = ''
        for i in range(0, self.__rowCount):
            output_str += ''.join(self.__array[i]) + "\n"
        return output_str

    def __set_rowCount_and_colCount(self):
        """ sets the row and column count from the size of the input array"""
        self.__rowCount, self.__colCount = self.__array.shape

    def __set_array(self, array):
        """validates if the given array is numpy array and sets the __array"""
        if isinstance(array, np.ndarray):
            self.__array = array

    def __find_not_mines(self):
        """ updates the list of __not_mine_list with the row and col value of '.' elements in the __array """
        self.__not_mine_list = np.where(self.__array == '.')

    def __update_hints(self):
        """ checks the number of '.' in the __array and selects a method to update the hint number"""
        if 0 < len(self.__not_mine_list[0]) <= self.__array.size // 2:
        # checks if the number of non-mine elements are less than or equal to half the size of __array
            self.__update_elements_counting_mine()
        elif len(self.__not_mine_list[0]) > self.__array.size // 2:
        # checks if the number of non-mine elements are more than half the size of __array
            self.__update_elements_surrounding_mines()
        elif len(self.__not_mine_list[0]) == self.__array.size:
        # checks if the number of non-mine elements are equal to the size of __array
            self.__array[self.__not_mine_list] = '0' # update all elements to '0'

    def __update_elements_counting_mine(self):
        """
        updates each '.' with the number if mines adjacent to it.
        if no mine is adjacent then updates the elemnt as '0'
        """
        rows, cols = self.__not_mine_list[0], self.__not_mine_list[1]
        for i in range(len(rows)): # loops on the list of non_mines('.')
            value = 0
            row, col = rows[i], cols[i]
            if 0 <= row - 1 < r and 0 <= col - 1 < c and self.__array[row - 1, col - 1] == '*': # upper_left
                value += 1
            if 0 <= row - 1 < r and 0 <= col + 1 < c and self.__array[row - 1, col + 1] == '*': # upper_right
                value += 1
            if 0 <= row + 1 < r and 0 <= col - 1 < c and self.__array[row + 1, col - 1] == '*': # down_left
                value += 1
            if 0 <= row + 1 < r and 0 <= col + 1 < c and self.__array[row + 1, col + 1] == '*': # down_right
                value += 1
            if 0 <= row - 1 < r and self.__array[row - 1, col] == '*': # up
                value += 1
            if 0 <= row + 1 < r and self.__array[row + 1, col] == '*': # down
                value += 1
            if 0 <= col + 1 < c and self.__array[row, col + 1] == '*': # left
                value += 1
            if 0 <= col - 1 < c and self.__array[row, col - 1] == '*': # right
                value += 1
            self.__array[row, col] = str(value)

    def __update_elements_surrounding_mines(self):
        """
        updates all elements adjacent to the mine elements
        """
        mine_list = np.where(self.__array == '*') # list of mines in the __array
        self.__array[self.__not_mine_list] = '0'  # updates all '.' elements to '0'
        rows, cols = mine_list[0], mine_list[1]
        for i in range(len(rows)): # loops on the list of mines('*')
            row, col = rows[i], cols[i]
            if 0 <= row - 1 < r and 0 <= col - 1 < c and self.__array[row - 1, col - 1] != '*': # upper_left
                self.__array[row-1, col-1] = str(int(self.__array[row-1, col-1]) +1)

            if 0 <= row - 1 < r and 0 <= col + 1 < c and self.__array[row - 1, col + 1] != '*': # upper_right
                self.__array[row - 1, col + 1] = str(int(self.__array[row - 1, col + 1])+1)

            if 0 <= row + 1 < r and 0 <= col - 1 < c and self.__array[row + 1, col - 1] != '*': # down_left
                self.__array[row + 1, col - 1] = str(int(self.__array[row + 1, col - 1])+1)

            if 0 <= row + 1 < r and 0 <= col + 1 < c and self.__array[row + 1, col + 1] != '*': # down_right
                self.__array[row + 1, col + 1] = str(int(self.__array[row + 1, col + 1])+1)

            if 0 <= row - 1 < r and self.__array[row - 1, col] != '*': # up
                self.__array[row - 1, col] = str(int(self.__array[row - 1, col])+1)

            if 0 <= row + 1 < r and self.__array[row + 1, col] != '*': # down
                self.__array[row + 1, col] = str(int(self.__array[row + 1, col])+1)

            if 0 <= col + 1 < c and self.__array[row, col + 1] != '*': # right
                self.__array[row, col + 1] = str(int(self.__array[row, col + 1])+1)

            if 0 <= col - 1 < c and self.__array[row, col - 1] != '*': # left
                self.__array[row, col - 1] = str(int(self.__array[row, col - 1])+1)

if __name__ == '__main__':
    with open('mines.txt', 'r') as input_file:
        with open('minesweeper_output.txt', 'w') as output_file:
            count = 0
            r, c = input_file.readline().split()
            while int(r) != 0 and int(c) != 0:
                r, c = int(r), int(c)
                mine_array = np.zeros((r, c), str)
                for val in range(0, r):
                    mine_array[val] = list(input_file.readline().strip('\n'))
                mine = Minesweeper(mine_array)
                count +=1
                output_file.write('Field #' + str(count) + ':\n' + str(mine) + '\n')
                r, c = input_file.readline().split()
    print("--- %s seconds ---" % (time.time() - start_time))
