import requests
import json
import urllib.request
import re
import shutil

callback = re.compile('callback\((.*)\);')

# Get a radio id
def get_id_list():
    # Make an API call
    radio_list_url = 'http://www.onsen.ag/api/shownMovie/shownMovie.json'
    r = requests.get(radio_list_url)
    response_dict = r.json()
    radio_dicts = response_dict['result']
    
    # Print the list
    print("\nList of radio name key for API:")
    for radio_dict in radio_dicts:
        print('id:', radio_dict)

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
    
def get_mp3(radio_id):
    # Make an API call
    url = urllib.request.urlopen("http://www.onsen.ag/data/api/getMovieInfo/" + radio_id)
    body = callback.search(url.read().decode('utf8')).group(1)
    response = json.loads(body)

    bangumi_urls = response['moviePath']
    mp3_url = bangumi_urls['pc']

    file_name = response['title'] + ' ' + response['update'] + ' ' + response['count'] + '回.mp3'

    # Download mp3 file 
    with urllib.request.urlopen(mp3_url) as mp3_response, open(file_name,'wb') as out_file:
        data = mp3_response.read()
        out_file.write(data)

    print("Download Complete!")

