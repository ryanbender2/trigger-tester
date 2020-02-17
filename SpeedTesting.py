"""Testing class for multithreading."""

import numpy as np
import time
import multiprocessing

def f(x):
    t = list()
    for i in range(x):
        for j in range(x):
            t.append(float(i * j))
    return t


def main():
    # test array
    arr = np.full((10000), 50)
    
    # multithreading test
    # p = multiprocessing.Pool(5)
    # test = list(p.map(f, arr))
    
    # single thread test
    test = list(map(f, arr))


if __name__ == '__main__':
    s_time = time.process_time()
    main()
    e_time = time.process_time()
    print('Run time: ' + str(float(e_time - s_time)) + ' seconds.')