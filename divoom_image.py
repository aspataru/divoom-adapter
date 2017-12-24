from itertools import product

from PIL import Image


def process_image(imagedata, sz=11, scale=None):
    img = [0]
    bc = 0
    first = True

    if (scale):
        src = imagedata.resize((sz, sz), scale)
    else:
        src = imagedata.resize((sz, sz))

    for c in product(range(sz), range(sz)):
        y, x = c
        r, g, b, a = src.getpixel((x, y))

        if (first):
            img[-1] = ((r & 0xf0) >> 4) + (g & 0xf0) if a > 32 else 0
            img.append((b & 0xf0) >> 4) if a > 32 else img.append(0)
            first = False
        else:
            img[-1] += (r & 0xf0) if a > 32 else 0
            img.append(((g & 0xf0) >> 4) + (b & 0xf0)) if a > 32 else img.append(0)
            img.append(0)
            first = True
        bc += 1
    return img


def load_image(file, sz=11, scale=None):
    with Image.open(file).convert("RGBA") as imagedata:
        return process_image(imagedata, sz)


def checksum(s):
    ck1 = s & 0x00ff
    ck2 = s >> 8

    return ck1, ck2


def conv_image(data):
    # should be 11x11 px =>
    head = [0xbd, 0x00, 0x44, 0x00, 0x0a, 0x0a, 0x04]
    data = data
    ck1, ck2 = checksum(sum(head) + sum(data))

    msg = [0x01] + head + mask(data) + mask([ck1, ck2]) + [0x02]
    return msg


def mask(bytes):
    _bytes = []
    for b in bytes:
        if (b == 0x01):
            _bytes = _bytes + [0x03, 0x04]
        elif (b == 0x02):
            _bytes = _bytes + [0x03, 0x05]
        elif (b == 0x03):
            _bytes = _bytes + [0x03, 0x06]
        else:
            _bytes += [b]

    return _bytes


def image_full(file):
    return conv_image(load_image(file, scale=Image.BICUBIC))
