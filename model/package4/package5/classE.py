

class ClassE(object):
    def __init__(self):
        super().__init__()

        self.c = ClassC()
        self.d = ClassD()

    def do_stuff(self):
        print('ClassE doing stuff...')
