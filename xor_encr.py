

def get_decrypts_8_bit(string):
    keys8 = [int(x) for x in range(256)]
    b = bytes(string, encoding="utf8")
    for key in keys8:
        ints = []
        for c in b:
            d = c ^ int(key)
            ints.append(d)
        print(bytes(ints))


def get_decrypts_16_bit(string):
    keys16 = [int(x) for x in range(65536)]
    b = bytes(string, encoding="utf8")
    for key in keys16:
        ints = []
        for c in b:
            d = c ^ int(key)
            ints.append(d)
        print(bytes(ints))


