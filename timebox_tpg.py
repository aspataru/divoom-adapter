import time
import sys
import divoom_device
import divoom_image
from tpg import next_departures
from os import listdir
from os.path import isfile, join, splitext

NB_IMAGES_PATH = 'images/nb/'


def retrieve_image_for_time(minutes):
    nb_files = [f for f in listdir(NB_IMAGES_PATH) if isfile(join(NB_IMAGES_PATH, f))]
    nb_files_noext = {splitext(f)[0] for f in nb_files}
    nb_files_noext_int = {int(f) for f in nb_files_noext}
    # min_file_present = min(nb_files_noext)
    max_file_present = int(max(nb_files_noext_int))
    if minutes in nb_files_noext_int:
        return NB_IMAGES_PATH + str(minutes) + '.bmp'
    elif minutes > max_file_present:
        return 'images/max.bmp'
    else:
        return 'images/min.bmp'


def send_image(device, path):
    bytes = divoom_image.image_full(path)
    device.send(bytes)


def run(address):
    dev = divoom_device.DivoomDevice(address)
    dev.connect()
    i = 0

    while i < 120:
        print('Calling TPG service')
        send_image(dev, "images/loading.bmp")
        minutes = next_departures()
        img_to_send = ''
        if minutes is None:
            img_to_send = "images/fail.bmp"
        else:
            print('Got', minutes, 'from TPG service')
            minutes_sorted = sorted(minutes)
            next_bus_minutes = minutes_sorted[0]

            print('Next bus in', next_bus_minutes, 'minutes')
            img_to_send = retrieve_image_for_time(next_bus_minutes)

        print('Sending image', img_to_send)
        send_image(dev, img_to_send)

        i += 1
        time.sleep(5)


if __name__ == '__main__':
    run(sys.argv[1])
