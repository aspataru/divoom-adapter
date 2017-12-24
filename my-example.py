import sys
import time

import divoom_device
import divoom_image


def display_simple_image():
    basename = "images/4.bmp"
    bytes = divoom_image.image_full(basename)
    dev.send(bytes)


DIVOMM_ADR = sys.argv[1]
dev = divoom_device.DivoomDevice(DIVOMM_ADR)

dev.connect()

print("display 4.bmp")
display_simple_image()

time.sleep(1)

dev.disconnect()
