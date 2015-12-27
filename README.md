#bronytunes-py - unofficial [bronytunes](https://bronytunes.com/) python cli client
    ./bronytunes.py [-s] [-n] mode subarg
##arguments
-s, --simulate : simulate download

-n, --number : print number only
use with search

##modes
###search - search song by name
how to use

    ./bronytunes.py s 'search'
or

    ./bronytunes.py search 'search'

example

    $ ./bronytunes.py s 'music in the treetops'
    7392-Music in the Treetops (ft. Andrea Libman)
    7391-Find The Music In The Treetops
    7402-Music in the Treetops (Extended Version w. Mysterious Bronie)
    9278-Music In The Treetops (latin spanish cover)
    7404-Music in the Treetops (Fluttermix)

###advanced search - search song by comparison
string comparable(possible condition: ==, !=)

 - name, description, lyrics, artist_name, album_artist_name, album

boolean comparable(possible condition: ==, !=)

 - has_music_video, allow_downloads, is_part_of_compilation, is_explicit

integer comparable(possible condition: ==, !=, >, >=, <, <=)

 - raw_artist_id, artist_id, album_artist_id, bitrate, duration, filesize

how to use
    ./bronytunes.py as 'comparison'
or

    ./bronytunes.py advsearch 'comparison'
or

    ./bronytunes.py adancedsearch 'comparison'

example

    $ ./bronytunes.py as 'artist_name==the living tombstone'
    5324-Atomizer (Remix of Renard) (ft. Ibeabronyrapper)
    5779-Babs Seed (The Living Tombstone's Remix)
    5778-Babs Seed (ft. MandoPony) (The Living Tombstone's Remix)
    ...

you can combine comparison more than one

    $ ./bronytunes.py as 'artist_name==the living tombstone' 'name==instrumental'
    9166-Die in a Fire (Instrumental)
    8625-Five Nights at Freddy's (Instrumental)
    5330-Good Girl (ft. Dasha) (Instrumental)
    ...

###information - get song information
how to use

    ./bronytunes.py i 'song_id'

or
    ./bronytunes.py info 'song_id'

or
    ./bronytunes.py information 'song_id'

example

    $ ./bronytunes.py i 7392
    has_music_video: Yes
    name: Music in the Treetops (ft. Andrea Libman)
    is_part_of_compilation: Yes
    ...
you can get certain information only by adding keyword

    $ ./bronytunes.py i 7392 lyrics
    There's music in the treetops
    And there's music in the vale
    And all around the music fills the sky
    ...
###download - download song

how to use

    ./bronytunes.py d 'song_id'

or

    ./bronytunes.py download 'song_id'
example

    $ ./bronytunes.py d 8097
    downloading 8097
you can download more than one song at once

    $ ./bronytunes.py d 8097 7321 3651
    downloading 8097
    downloading 7321
    downloading 3651
or using -n argument and command substitution

    $ ./bronytunes.py d $(./bronytunes.py -n as 'artist_name==Daniel Ingram')
    downloading 7148
    downloading 7174
    downloading 6997
    ...
##to-do
 - show download status
 - exception when downloads fail
 - download limit?
 - separate into modules
 - how about 'ArgumentParser.add_subparsers'?