import requests
from bs4 import BeautifulSoup

TPG_VRDO_URL = 'http://www.tpg.ch/horaires/temps-reels?p_p_id=TempsReel_WAR_TempsReelportlet&p_p_lifecycle=0&' \
               'p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&' \
               '_TempsReel_WAR_TempsReelportlet_thermometreTR=1&_TempsReel_WAR_TempsReelportlet_horaireRef=82054&' \
               '_TempsReel_WAR_TempsReelportlet_jspPage=%2Fhtml%2Fthermometre.jsp&' \
               '_TempsReel_WAR_TempsReelportlet_ligne=8&_TempsReel_WAR_TempsReelportlet_arret=VRDO'


def next_VRDO_depart():
    r = requests.get(TPG_VRDO_URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    times = soup.find('span', 'tempsreel_thermo_time tempsreel_time').text
    return times


print(next_VRDO_depart())
