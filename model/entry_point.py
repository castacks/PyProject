
from package1 import ClassA
from package2 import ClassB
from package4.package5 import ClassE

def main():

    # ClassA.
    a = ClassA()
    a.do_stuff()

    # ClassB.
    b = ClassB()
    b.do_stuff()

    # ClassE.
    e = ClassE()
    e.do_stuff()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
