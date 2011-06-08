#!/usr/bin/python3

from urllib import request
import sys
import json
import os

player_command_raw = 'mpg123 --list {0}'
stereomood_url_raw = 'http://stereomood.com/mood/{0}/playlist.json?save&index={1}'
pl_file_name_raw = '/tmp/{0}_{1}.pl'

try:
    mood = sys.argv[1]
except:
    print('usage: %s mood'%sys.argv[0])
    exit(1)

stereomood_url = stereomood_url_raw.format(mood, 1)

# get number of tracks
# this request may be redundant
# but i'm too lazy to fix this now
response = request.urlopen(stereomood_url).read().decode()

playlist = json.loads(response)
total = int(playlist['tracksTotal'])
count = round(total/20) + 1

for i in range(1, count):
    songs = []
    stereomood_url = stereomood_url_raw.format(mood, i)
    pl_file_name = pl_file_name_raw.format(mood, i)
    player_command = player_command_raw.format(pl_file_name)

    response = request.urlopen(stereomood_url).read().decode()
    playlist = json.loads(response)

    for song in playlist['trackList']:
        songs.append(song['location'])

    pl_file = open(pl_file_name, 'w')
    pl_file.write('\n'.join(songs))
    pl_file.close()

    os.system(player_command)
