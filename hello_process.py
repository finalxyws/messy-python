#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing
import time


def worker(interval, name):
    print('Worker %s is running...started at: {0}'.format(time.ctime()) % name)
    time.sleep(interval)
    print('Worker %s is ended.' % name)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=worker, args=(2, 'p1'))
    p2 = multiprocessing.Process(target=worker, args=(3, 'p2'))
    p3 = multiprocessing.Process(target=worker, args=(4, 'p3'))
    p1.start()
    p2.start()
    p3.start()
    print('The number of CPU is: ', multiprocessing.cpu_count())
    for p in multiprocessing.active_children():
        print('Child process name: %s, id: %s' % (p.name, p.pid))
    p1.join()
    p2.join()
    p3.join()
    print('All processes are ended.')