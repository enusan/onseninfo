import requests
import json
import urllib.request
import re

callback = re.compile('callback\((.*)\);')

# Get a radio id
def get_key_list():
    # Make an API call
    radio_list_url = 'http://www.onsen.ag/api/shownMovie/shownMovie.json'
    r = requests.get(radio_list_url)
    response_dict = r.json()
    radio_dicts = response_dict['result']
    
    # Print the list
    print("\nList of radio name key for API:")
    for radio_dict in radio_dicts:
        print('Key:', radio_dict)

# Get a radio infomation
def get_radio_info(radio_id):  
    # Make an API call
    url = urllib.request.urlopen("http://www.onsen.ag/data/api/getMovieInfo/" + radio_id)
    body = callback.search(url.read().decode('utf8')).group(1)
    response = json.loads(body)

    bangumi_urls = response['moviePath']

    print("TItle:", response['title'])
    print("Personality:", response['personality'])
    print("Update date:", response['update'])
    print("Count:", response['count'])
    print("Bangumi URL:",bangumi_urls['pc'])
    
