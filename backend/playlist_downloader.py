from pytube import Playlist, YouTube
from song_downloader import SongDownloader

class PlaylistDownloader(SongDownloader): 
    def __init__(self, playlist_url: str, export_path: str = None):
        self.export_path = export_path or super().__init__(export_path="")
        self.playlist = Playlist(playlist_url)
             
    def download_songs(self) -> None: 
        if not self.playlist:
            print("La lista de reproducción está vacía.")
            return None
        for url in self.playlist: 
            self.download_song(url)
