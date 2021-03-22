from sys import argv

from config import bases, fbase
from utils.classes import ReadWriteFile

if len(argv) < 2:
    prefix_base = input('Введите имя базы парсера (m, d, t) - ')
else:
    prefix_base = argv[1]


if prefix_base == 'm' or prefix_base == 'd' or prefix_base == 't':
    base = ReadWriteFile(bases, prefix_base + fbase, 0)
    base.read_file()
