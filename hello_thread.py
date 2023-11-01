#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time
import queue


class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print('Thread %s is running...' % self.name)
        time.sleep(1)
        print('Thread %s is ended.' % self.name)


def main():
    print('Thread %s is running...' % threading.current_thread().name)
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Thread %s is ended.' % threading.current_thread().name)


class Consumer(threading.Thread):
    def __init__(self, name, cond, product):
        super(Consumer, self).__init__()
        self.name = name
        self.cond = cond
        self.product = product

    def run(self):
        while True:
            self.cond.acquire()
            if len(self.product) == 0:
                self.cond.wait()
            else:
                self.product.pop()
                print('Consumer %s consumed a product.' % self.name)
                self.cond.notify()
            self.cond.release()
            time.sleep(1)


class Producer(threading.Thread):
    def __init__(self, name, cond, product):
        super(Producer, self).__init__()
        self.name = name
        self.cond = cond
        self.product = product

    def run(self):
        while True:
            self.cond.acquire()
            if len(self.product) == 5:
                self.cond.wait()
            else:
                self.product.append(1)
                print('Producer %s produced a product.' % self.name)
                self.cond.notify()
            self.cond.release()
            time.sleep(1)


def write(q):
    for i in range(10):
        q.put(i)
        print('write %s to queue.' % i)
        time.sleep(1)


def read(q):
    while True:
        if not q.empty():
            print('read %s from queue.' % q.get())
            time.sleep(2)
        else:
            break


if __name__ == '__main__':
    # product = []
    # cond = threading.Condition()
    # p1 = Producer('p1', cond, product)
    # p2 = Producer('p2', cond, product)
    # p3 = Producer('p3', cond, product)
    # c1 = Consumer('c1', cond, product)
    # c2 = Consumer('c2', cond, product)
    # c1.start()
    # c2.start()
    # p1.start()
    # p2.start()
    # p3.start()
    q = queue.Queue()
    t1 = threading.Thread(target=write, args=(q,))
    t2 = threading.Thread(target=read, args=(q,))
    t1.start()
    t2.start()
