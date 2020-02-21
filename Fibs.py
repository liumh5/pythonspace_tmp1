# -*- coding: utf-8 -*-
class Fibs(object):


    def __init__(self,max):
        self.max = max
        self.a = 0
        self.b = 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if self.idx == self.max :
            raise StopIteration

        self.idx = self.idx + 1
        self.a,self.b = self.b ,self.a + self.b
        return fib


if __name__ == "__main__" :
    fibs = Fibs(100)
    print(list(fibs))