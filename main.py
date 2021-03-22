from sys import argv

from utils.classes import ArgvCheck


def start():
    argument = ArgvCheck()
    argument.check(argv)
    argument.get_argument()


if __name__ == '__main__':
    start()
