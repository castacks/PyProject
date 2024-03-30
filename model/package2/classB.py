
from ..package1 import ClassA
from .package3 import ClassC

class ClassB(object):
    def __init__(self):
        super().__init__()

        self.a = ClassA()
        self.c = ClassC()

    def do_stuff(self):
        print('ClassB doing stuff...')
