import numpy as np
import time
start_time = time.time()

with open('mines.txt', 'r') as input_file:
    with open('minesweeper_output.txt', 'w') as output_file:
        r, c = input_file.readline().split()
        count = 0
        while int(r) != 0 and int(c) != 0:
            r, c = int(r), int(c)
            mine_array = np.zeros((r, c), str)
            for val in range(0, r):
                mine_array[val] = list(input_file.readline().strip('\n'))

            for row in range(r):
                for col in range(c):
                    if mine_array[row, col] != '*':
                        value = 0
                        if 0 <= row - 1 < r and 0 <= col - 1 < c and mine_array[row-1, col-1] == '*':
                            value +=1
                        if 0 <= row - 1 < r and 0 <= col + 1 < c and mine_array[row-1, col+1] == '*':
                            value +=1
                        if 0 <= row + 1 < r and 0 <= col - 1 < c and mine_array[row+1, col-1] == '*':
                            value +=1
                        if 0 <= row + 1 < r and 0 <= col + 1 < c and mine_array[row+1, col+1] =='*':
                            value +=1
                        if 0 <= row - 1 < r and mine_array[row-1, col] == '*':
                            value +=1
                        if 0 <= row + 1 < r and mine_array[row + 1, col] == '*':
                            value += 1
                        if 0 <= col + 1 < c and mine_array[row, col+1] == '*':
                            value += 1
                        if 0 <= col - 1 < c and mine_array[row, col-1] == '*':
                            value += 1
                        mine_array[row, col] = str(value)

            output_str = ''
            for i in range(0, r):
                for j in range(0, c):
                    output_str += str(mine_array[i, j])
                output_str += "\n"
            count +=1
            output_file.write('Field #' + str(count) + ':\n' + str(output_str) + '\n')
            r, c = input_file.readline().split()

print("--- %s seconds ---" % (time.time() - start_time))