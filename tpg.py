import requests
from bs4 import BeautifulSoup

TPG_VRDO_URL = 'https://m.tpg.ch/stopDisplay.htm?mnemo=VRDO'
# TPG_VRDO_URL = 'https://m.tpg.ch/stopDisplay.htm?mnemo=AERO'


def extract_time_tags(content):
    soup = BeautifulSoup(content, 'html.parser')
    tags = soup.find_all("span", {"class": "timeText"})
    time_strings = [tag.text for tag in tags]
    return time_strings


def parse_minutes(the_list):
    minutes = []
    for elem in the_list:
        elem_str = str(elem)
        # todo ~ should be handled differently
        if elem_str != '':
            minutes.append(int(elem_str.replace('\'', '').replace('~','')))
    return minutes


def next_departures():
    r = requests.get(TPG_VRDO_URL)
    time_tags = extract_time_tags(r.content)
    minutes = parse_minutes(time_tags)
    return minutes


if __name__ == '__main__':
    print(next_departures())
