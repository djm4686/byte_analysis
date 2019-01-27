from matplotlib import pyplot
from collections import OrderedDict
import sys


def generate_file_byte(filename, n=None):

    with open(filename, "rb") as f:
        byte = f.read(1)
        i = 0
        print("hi")
        while byte != b"" and (n is None or i < n):
            yield byte
            i += 1
            byte = f.read(1)


def get_byte_count_map(filename, n=None):
    byte_count = OrderedDict()
    for byte in generate_file_byte(filename, n):
        byte = int.from_bytes(byte, byteorder=sys.byteorder)
        if byte in byte_count:
            byte_count[byte] += 1
        else:
            byte_count[byte] = 1
    return byte_count


def show_plot(filename, n=None):
    byte_count = get_byte_count_map(filename, n)
    pyplot.bar(byte_count.keys(), byte_count.values())
    pyplot.show()


def get_top_x(filename, x, n=None):
    byte_count = get_byte_count_map(filename, n)
    byte_count = sorted(byte_count.items(), key=lambda x: x[1])
    byte_count.reverse()
    i = 0
    while i < x:
        yield byte_count[i]
        i += 1


if __name__ == "__main__":
    show_plot("tests/vrfauto.dll")
    # for x in get_top_x("tests/card_template_600.xcf", 10):
    #     print(x)
