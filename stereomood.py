#!/usr/bin/python3

from urllib import request
import sys
import json
import os

player_command = 'mpg123 --list {0}'
stereomood_url = 'http://stereomood.com/mood/{0}/playlist.json?save'
referer = 'http://stereomood.com/mood/{0}'
pl_file_name = '/tmp/{0}.pl'
songs = []

try:
    mood = sys.argv[1]
    stereomood_url = stereomood_url.format(mood)
    referer = referer.format(mood)
    pl_file_name = pl_file_name.format(mood)
    player_command = player_command.format(pl_file_name)
except:
    print('usage: %s mood'%sys.argv[0])
    exit(1)

req = request.Request(stereomood_url)
req.add_header('Referer', referer)
response = request.urlopen(stereomood_url).read().decode()
import pdb;pdb.set_trace()
playlist = json.loads(response)

pl_file = open(pl_file_name, 'w')

for song in playlist['trackList']:
    songs.append(song['location'])

pl_file.write('\n'.join(songs))
pl_file.close()

os.system(player_command)
