from pytube import Playlist, YouTube
from song_downloader import SongDownloader

class PlaylistDownloader(SongDownloader): 
    """
    A class for downloading songs from a YouTube playlist.

    Parameters:
    - playlist_url (str): The URL of the YouTube playlist.
    - export_path (str, optional): The path where the downloaded songs will be saved. If not provided, the default path will be used.

    Attributes:
    - export_path (str): The path where the downloaded songs will be saved.
    - playlist (Playlist): The `pytube.Playlist` object representing the YouTube playlist.

    Methods:
    - __init__(self, playlist_url: str, export_path: str = None): 
        Initializes a new instance of the PlaylistDownloader class.

    - download_songs(self) -> None:
        Downloads all songs from the playlist. Prints a message if the playlist is empty or private.
    """
    def __init__(self, playlist_url: str, export_path: str = None):
        self.export_path = export_path or super().__init__(export_path="")
        self.playlist = Playlist(playlist_url)
             
    def download_songs(self) -> None: 
        if not self.playlist:
            print("La lista de reproducción está vacía o es privada.")
            return None
        for url in self.playlist: 
            self.download_song(url)


