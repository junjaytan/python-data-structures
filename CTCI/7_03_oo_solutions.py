"""musical juke box OO example
Things you might want do do are:
    flip cd forward/backward
    play cd
    insert money (?)
    add_cd (administrator)
    remove_cd (administrator)

"""


class Album(object):
    def __init__(self, title, artist, songs):
        """ song is a list of Song objects, title is name of album, artist is name of artist """
        self.title = title
        self.artist = artist
        self.songs = songs
        self._current_song = 0

    def get_num_songs(self):
        return len(self.songs)

    def next_song(self):
        """ get next song"""

    def prev_song(self):
        get
        previous
        song

    def current_song(self):
        """ return name and artist of current song """

    def play_song(self):
        """ play currently selected song"""


class Song(object):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Jukebox(object):
    def __init__(self):
        self._albums = []
        self._capacity = 10
        self._current_album = 0

    def next_album(self):
        if not self._albums:  # if no albums exist in jukebox, return none
            return None
        if self._current_album < len(self._albums) - 1:  # if there are other albums, cycle to next album
            self._current_album += 1
        return self.albums[self._current_album]  # if final album in jukebox, return current album

    def prev_album(self):
        if not self._albums:  # if no albums exist in jukebox, return none
            return None
        if self._current_album > 0:  # if there are other before current album, cycle to previous album
            self._current_album -= 1
        return self.albums[self._current_album]  # if first album in jukebox, return current album

    def play_album(self):
        """ play current album, starting at selected song"""

    def list_songs(self):
        """ lists all songs in current album """

    def current_song(self):
        """ list the currently selected song """



