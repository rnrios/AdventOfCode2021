import numpy as np


def num_lantern_fish(array, n):
    n -= 1
    array -= 1 
    print('After {} days: \t{}'.format(N-n, array))
    if n == 0:
        return 
    num_zeros = np.sum((array==0))
    array[array==0] = 7
    new_fishes = 9*np.ones(num_zeros).astype(int)
    array = np.hstack((array, new_fishes))
    num_lantern_fish(array, n)



f = open('test_input.txt').readlines()
initial_num_fishes = np.array([int(x) for x in f[0].split(',') if x != ','])
N = 30
num_lantern_fish(initial_num_fishes, N)
