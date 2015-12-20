#!/usr/bin/env python3
import urllib3
import json
urllib = urllib3.PoolManager()

def updatesongs():
    songs = open('songs.json', 'w')    
    songs.write(urllib.request('GET', 'https://bronytunes.com/retrieve_songs.php?client_type=web').data)
    songs.close()

def updateartists():
    artists = open('artists.json', 'w')
    artists.write(urllib.request('GET', 'https://bronytunes.com/retrieve_artists.php?client_type=web').data)
    artists.close()

def downloadsong(song_id):
    site = urllib.request('GET', 'https://bronytunes.com/retrieve_song.php?song_id=%d&client_type=web'%song_id)
    for i in songs:
        if(i['song_id'] == str(song_id)):
            name = i['name']
    file = open('%s.mp3'% name, 'bw')
    file.write(site.data)
    file.close()

def songinfo(song_id):
    for i in songs:               
        if(i['song_id'] == str(song_id)):
            for j in i:
                print(i[j])

def searchsong(st):
    for i in songs:
        if ( -1 != ((i['name'].lower()).find(st.lower()))):
            print(i['song_id']+'-'+i['name'])

try:
    songs = json.load(open('songs.json', 'r'))
except:
    updatesongs()

try:
    artists = json.load(open('artists.json', 'r'))
except:
    updateartists()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='bronytunes')
    parser.add_argument('mode', type=str)
    parser.add_argument('arg2', type=str)

    args = parser.parse_args()

    if (args.mode == "d"):
        downloadsong(int(args.arg2))
    elif (args.mode == "s"):
        searchsong(args.arg2)
    elif (args.mode == "i"):
        songinfo(int(args.arg2))
    else:
        pass
