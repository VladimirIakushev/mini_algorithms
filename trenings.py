from __future__ import print_function
from six import Iterator


class MyIterator(Iterator):
    def __init__(self, step=50):
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.step -= 3
# Условие остановки итератора, чтобы он не бежал вечно
        if self.step <= 0:
            raise StopIteration()
        return self.step


myiterator = MyIterator()
for item in myiterator:
    print(item, end=" ")
