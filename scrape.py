import requests
from bs4 import BeautifulSoup
import re
import data_classes


def scrape_smw_hacks(moderated=True, pagination=0):
    hack_list = []
    smw_central_url = "https://smwcentral.net"
    html_parameters = {"p": "section", "a": "list", "s": "smwhacks", "u": 0, "g": 0}
    if not moderated:
        html_parameters["u"] = 1
    if pagination > 0:
        html_parameters["n"] = pagination

    smw_central_page = requests.get(smw_central_url, html_parameters)
    smw_soup = BeautifulSoup(smw_central_page.text, features="html.parser")
    # Pull the basic hack data, which includes hack title, download URL, and time uploaded
    base_hack_data = smw_soup.find_all("td", {"class": "text"})
    for hack_data in base_hack_data:
        current_hack = data_classes.SMWHackInfo()

        # noinspection PyUnresolvedReferences
        _title_url_attribute = hack_data.a
        _date_attribute = hack_data.find_next('time')

        if _title_url_attribute:
            current_hack.title = _title_url_attribute.text if _title_url_attribute else None
            if (not moderated) and ('moderated' in _title_url_attribute.find_parent('td').text):
                _moderator_attribute = _title_url_attribute.find_next('a')
                current_hack.moderator = _moderator_attribute.text
            # TODO: Swap download URL for id attribute
            current_hack.download_url = f"https://smwcentral.net{_title_url_attribute['href']}" \
                if _title_url_attribute['href'] else None

            try:
                # noinspection PyUnresolvedReferences
                current_hack.dates = _date_attribute['datetime']
            except KeyError:
                pass

        # Pull the secondary hack data, which has (in order): demo status, HoF status,
        # exits, difficulty, and author
        # TODO: Add checks to this, make it actually good
        secondary_hack_data = hack_data.find_next_siblings("td", limit=5)
        current_hack.demo = False if secondary_hack_data[0].text == "No" else True
        current_hack.hall_of_fame = False if secondary_hack_data[1].text == "No" else True
        current_hack.exits = re.findall('[0-9]+', secondary_hack_data[2].text)[0]
        current_hack.difficulty = secondary_hack_data[3].text
        current_hack.author = secondary_hack_data[4].find_next('a').text

        hack_list.append(current_hack.serialize())

    return hack_list
