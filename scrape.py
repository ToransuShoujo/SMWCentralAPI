import requests
from bs4 import BeautifulSoup
import re
import data_classes
from datetime import datetime


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
        _url_attribute = hack_data.a

        if _url_attribute:
            current_hack.title = _url_attribute.text if _url_attribute else None
            if (not moderated) and ('moderated' in _url_attribute.find_parent('td').text):
                _moderator_attribute = _url_attribute.find_next('a')
                current_hack.moderator = _moderator_attribute.text
            current_hack.id = re.findall('[0-9]+', _url_attribute['href'])[0] \
                if _url_attribute['href'] else None

            if moderated:
                hack_dates = get_hack_dates(current_hack.id)
                current_hack.submissions = hack_dates[0]
                current_hack.acceptances = hack_dates[1]
            else:
                _date_attribute = hack_data.find_next('time')
                current_hack.submissions = [_date_attribute['datetime']]

        # Pull the secondary hack data, which has (in order): demo status, HoF status,
        # exits, difficulty, and author
        # TODO: Add checks to this, make it actually good
        secondary_hack_data = hack_data.find_next_siblings("td")
        current_hack.demo = False if secondary_hack_data[0].text == "No" else True
        current_hack.hall_of_fame = False if secondary_hack_data[1].text == "No" else True
        current_hack.exits = re.findall('[0-9]+', secondary_hack_data[2].text)[0]
        current_hack.difficulty = secondary_hack_data[3].text
        current_hack.authors = secondary_hack_data[4].text.split(', ')

        hack_list.append(current_hack.serialize())

    return hack_list


def get_hack_dates(hack_id):
    submission_list = []
    approval_list = []
    version_url = f"https://www.smwcentral.net/?p=section&a=versionhistory&id={hack_id}"
    version_page = requests.get(version_url)
    print(version_page)
    version_soup = BeautifulSoup(version_page.text, features="html.parser")

    version_data = version_soup.find_all("tr")
    version_data.pop(0)  # The first element is the table headings, so we just drop it.
    for version_attribute in version_data:
        version_id = re.findall('[0-9]+', version_attribute.a["href"])[0]
        submission_request = requests.head(f"https://dl.smwcentral.net/{version_id}/*.*")
        print(submission_request)
        unformatted_submission = submission_request.headers['last-modified']
        formatted_submission = str(datetime.strptime(unformatted_submission, "%a, %d %b %Y %H:%M:%S GMT"))
        submission_list.append(str.replace(formatted_submission, ' ', 'T'))
        approval_list.append(version_attribute.find_next("time")['datetime'])

    return submission_list, approval_list
