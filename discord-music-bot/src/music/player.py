class MusicPlayer:
    def __init__(self):
        self.is_playing = False
        self.current_song = None

    def play(self, song):
        self.current_song = song
        self.is_playing = True
        # Logic to play the song

    def pause(self):
        if self.is_playing:
            self.is_playing = False
            # Logic to pause the song

    def stop(self):
        if self.is_playing:
            self.is_playing = False
            self.current_song = None
            # Logic to stop the song

    def skip(self):
        if self.is_playing:
            # Logic to skip to the next song
            pass