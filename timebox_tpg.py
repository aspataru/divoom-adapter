import time
import sys
import divoom_device
import divoom_image
from tpg import next_depart


def send_image(device, path):
    bytes = divoom_image.image_full(path)
    device.send(bytes)


def run(address: str):
    dev = divoom_device.DivoomDevice(address)
    dev.connect()
    i = 0

    while i < 12:
        print('Calling TPG service')
        send_image(dev, "images/loading.bmp")
        minutes = next_depart()
        if minutes is None:
            send_image(dev, "images/fail.bmp")
        else:
            print('Got', minutes, 'from TPG service')
        i += 1
        time.sleep(5)


if __name__ == '__main__':
    run(sys.argv[1])
