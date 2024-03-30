
from .. import ClassD
from ...package2.package3 import ClassC

class ClassE(object):
    def __init__(self):
        super().__init__()

        self.c = ClassC()
        self.d = ClassD()

    def do_stuff(self):
        print('ClassE doing stuff...')
