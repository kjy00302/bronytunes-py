#!/usr/bin/env python3
import urllib3
import json
urllib = urllib3.PoolManager()

supportstr = (
    'name',
    'descrption',
    'lyrics',
    'artist_name',
    'album_artist_name',
    'album'
)

supportbool = (
    'has_music_video',
    'allow_downloads',
    'is_part_of_compilation',
    'is_explicit'
)

supportint = (
    'raw_artist_id',
    'artist_id',
    'album_artist_id',
    'bitrate',
    'duration',
    'filesize'
)


def updatesongs():
    songs = open('songs.json', 'bw')
    songs.write(
        urllib.request(
            'GET',
            'https://bronytunes.com/retrieve_songs.php?client_type=web'
            ).data
        )
    songs.close()

'''
def updateartists():
    artists = open('artists.json', 'bw')
    artists.write(
        urllib.request(
            'GET',
            'https://bronytunes.com/retrieve_artists.php?client_type=web'
            ).data
        )
    artists.close()
'''


def downloadsong(song_id):
    site = urllib.request(
        'GET',
        'https://bronytunes.com/retrieve_song.php?song_id=%d&client_type=web'
        % song_id
    )
    for i in songs:
        if(i['song_id'] == str(song_id)):
            name = i['name']
    file = open('%s.mp3' % name, 'bw')
    file.write(site.data)
    file.close()


def songinfo(song_id, key=''):
    slist = []
    for i in songs:
        if(i['song_id'] == str(song_id)):
            for j in i:
                if key == j:
                    if j in supportstr:
                        if i[j] is None:
                            return()
                        else:
                            return(i[j])
                    if j in supportbool:
                        if i[j] is None:
                            return(False)
                        else:
                            return(True)
                    if j in supportint:
                        if i[j] is None:
                            return()
                        else:
                            return(i[j])
                elif key == "":
                    if j in supportstr:
                        if i[j] is None:
                            slist.append(j + ': ' + 'None')
                        else:
                            slist.append(j + ': ' + i[j])
                    if j in supportbool:
                        if i[j] is None:
                            slist.append(j + ': ' + 'No')
                        else:
                            slist.append(j + ': ' + 'Yes')
                    if j in supportint:
                        if i[j] is None:
                            slist.append(j + ': ' + 'None')
                        else:
                            slist.append(j + ': ' + i[j])
                else:
                    pass
    return slist


def searchsong(st, n):
    slist = []
    for i in songs:
        if(-1 != ((i['name'].lower()).find(st.lower()))):
            if(n is True):
                slist.append(i['song_id'])
            else:
                slist.append(i['song_id']+'-'+i['name'])
    return slist


def searchstr(li, co, key, value):
    slist = []
    for i in li:
        if co == '==':
            if i[key] is not None:
                if -1 != ((i[key].lower()).find(value.lower())):
                    slist.append(i)
        if co == '!=':
            if i[key] is not None:
                if -1 == ((i[key].lower()).find(value.lower())):
                    slist.append(i)
    return slist


def searchint(li, co, key, value):
    slist = []
    for i in li:
        if co == '>':
            if int(i[key]) > value:
                slist.append(i)
        if co == '<':
            if int(i[key]) < value:
                slist.append(i)
        if co == '==':
            if int(i[key]) == value:
                slist.append(i)
        if co == '!=':
            if int(i[key]) != value:
                slist.append(i)
        if co == '>=':
            if int(i[key]) >= value:
                slist.append(i)
        if co == '<=':
            if int(i[key]) <= value:
                slist.append(i)
    return slist


def searchbool(li, co, key, value):
    slist = []
    if value.lower() in ('1', 'true', 'yes'):
        value = True
    elif value.lower() in ('0', 'false', 'no'):
        value = False
    else:
        pass
    for i in li:
        if co == '==':
            if bool(i[key]) == bool(value):
                slist.append(i)
        if co == '!=':
            if not(bool(i[key]) == bool(value)):
                slist.append(i)
    return slist


def advancedsearch(conds):
    slist = []
    findlist = songs
    for i in conds:
        if i.find('==') != -1:
            if i[:i.find('==')] in supportstr:
                findlist = searchstr(findlist,
                                     '==',
                                     i[:i.find('==')],
                                     i[i.find('==')+2:].strip()
                                     )
            elif i[:i.find('==')] in supportint:
                findlist = searchint(findlist,
                                     '==',
                                     i[:i.find('==')],
                                     int(i[i.find('==')+2:].strip())
                                     )
            elif i[:i.find('==')] in supportbool:
                findlist = searchbool(findlist,
                                      '==',
                                      i[:i.find('==')],
                                      i[i.find('==')+2:].strip()
                                      )
            else:
                pass

        if i.find('!=') != -1:
            if i[:i.find('!=')] in supportstr:
                findlist = searchstr(findlist,
                                     '!=',
                                     i[:i.find('!=')],
                                     i[i.find('!=')+2:].strip()
                                     )
            elif i[:i.find('!=')] in supportint:
                findlist = searchint(findlist,
                                     '!=',
                                     i[:i.find('!=')],
                                     int(i[i.find('!=')+2:].strip())
                                     )
            elif i[:i.find('!=')] in supportbool:
                findlist = searchbool(findlist,
                                      '!=',
                                      i[:i.find('!=')],
                                      i[i.find('!=')+2:].strip()
                                      )
            else:
                pass
        if i.find('>') != -1:
            if i[:i.find('>')] in supportstr:
                pass
            elif i[:i.find('>')] in supportint:
                findlist = searchint(findlist,
                                     '>',
                                     i[:i.find('>')],
                                     int(i[i.find('>')+1:].strip())
                                     )
            elif i[:i.find('>')] in supportbool:
                pass
            else:
                pass
        if i.find('<') != -1:
            if i[:i.find('<')] in supportstr:
                pass
            elif i[:i.find('<')] in supportint:
                findlist = searchint(findlist,
                                     '<',
                                     i[:i.find('<')],
                                     int(i[i.find('<')+1:].strip())
                                     )
            elif i[:i.find('<')] in supportbool:
                pass
            else:
                pass
        if i.find('>=') != -1:
            if i[:i.find('>=')] in supportstr:
                pass
            elif i[:i.find('>=')] in supportint:
                findlist = searchint(findlist,
                                     '>=',
                                     i[:i.find('>=')],
                                     int(i[i.find('>=')+2:].strip())
                                     )
            elif i[:i.find('>=')] in supportbool:
                pass
            else:
                pass
        if i.find('<=') != -1:
            if i[:i.find('<=')] in supportstr:
                pass
            elif i[:i.find('<=')] in supportint:
                findlist = searchint(findlist,
                                     '<=',
                                     i[:i.find('<=')],
                                     int(i[i.find('<=')+2:].strip())
                                     )
            elif i[:i.find('<=')] in supportbool:
                pass
            else:
                pass
    for i in findlist:
        if(args.n is True):
            slist.append(i['song_id'])
        else:
            slist.append(i['song_id']+'-'+i['name'])
    return slist

try:
    songs = json.load(open('songs.json', 'r'))
except:
    updatesongs()

'''
try:
    artists = json.load(open('artists.json', 'r'))
except:
    updateartists()
'''

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description='bronytunes.py - unofficial bronytunes python cli client'
        )
    parser.add_argument('mode', type=str)
    parser.add_argument('subarg', type=str, nargs='*')
    parser.add_argument(
        '-n', '--number',
        action='store_true',
        help='print number only. use with command substitution \'$()\''
        )
    parser.add_argument(
        '-s', '--simulate',
        action='store_true',
        help='simulate. do not download'
        )

    args = parser.parse_args()

    if (args.s is True):
        import time
        print('simulating...')

    if (args.mode.lower() in ('d', 'download')):
        if len(args.subarg) > 0:
            for i in args.subarg:
                print('downloading %d' % int(i))
                if (args.s is True):
                    time.sleep(1)
                else:
                    downloadsong(int(i))
        else:
            print('usage: %s song_id [song_id ...]' % args.mode)
    elif (args.mode.lower() in ('s', 'search')):
        if len(args.subarg) > 0:
            for i in searchsong(args.subarg[0], args.n):
                print(i)
        else:
            print('usage: %s song_id [-n]' % args.mode)
    elif (args.mode.lower() in ('as', 'advsearch', 'advancedsearch')):
        if len(args.subarg) > 0:
            for i in advancedsearch(args.subarg):
                print(i)
        else:
            print(
                "usage: %s 'comparison' ['comparison' ...] [-n]" % args.mode
                )
    elif (args.mode.lower() in ('i', 'info', 'information')):
        if len(args.subarg) > 0:
            if len(args.subarg) >= 2:
                print(songinfo(int(args.subarg[0]), args.subarg[1]))
            else:
                for i in songinfo(int(args.subarg[0])):
                    print(i)
        else:
            print('usage: %s song_id [keyword]' % args.mode)
    elif (args.mode.lower() in ('u', 'update')):
        # updateartists()
        updatesongs()
    else:
        pass
