
##bronytunes songs json file

    {
        "song_id":strint,
        "sorting_number":strint,
        "name":str,
        "description":str,
        "lyrics":str,
        "purchase_link":str,
        "youtube_id":str,
        "has_music_video":strbool,
        "allow_downloads":strbool,
        "raw_artist_id":strint,
        "artist_id":strint,
        "album_artist_id":strint,
        "release_date":str(YYYY-MM-DD),
        "artist_name":str,
        "album_artist_name":str,
        "album":str,
        "bitrate":strint,
        "duration":strint,
        "filesize":strint,
        "path":"\/\/a",
        "is_part_of_compilation":strbool,
        "visible":null,
        "track_number":strint,
        "is_explicit":strbool
    }

string-searchable - name, description, lyrics, artist_name, album_artist_name, album

boolean-searchable - has_music_video, allow_downloads, is_part_of_compilation, is_explicit

integer-searchable - raw_artist_id, artist_id, album_artist_id, bitrate, duration, filesize

##bronytunes artists json file(not using now)
    {
        "artist_id":strint,
        "artist_name":str,
        "artist_displayname":null,
        "usr_id":strint,
        "song_count":strint
    }
string-searchable - artist_name

integer-searchable - artist_id, usr_id, song_count