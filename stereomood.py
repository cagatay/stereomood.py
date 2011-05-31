#!/usr/bin/python3

from urllib import request
import sys
import json
import os

player_command = 'mpg123 --list {0}'
stereomood_url = 'http://stereomood.com/activity/{0}/playlist.json'
pl_file_name = '/tmp/{0}.pl'
songs = []

try:
    mood = sys.argv[1]
    stereomood_url = stereomood_url.format(mood)
    pl_file_name = pl_file_name.format(mood)
    player_command = player_command.format(pl_file_name)
except:
    print('usage: %s mood'%sys.argv[0])
    exit(1)

response = request.urlopen(stereomood_url).read().decode()
playlist = json.loads(response)

pl_file = open(pl_file_name, 'w')

for song in playlist['trackList']:
    songs.append(song['location'])

pl_file.write('\n'.join(songs))
pl_file.close()

os.system(player_command)
