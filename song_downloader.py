import os
from pytube import YouTube
import re

class SongDownloader: 
    """
     Class for downloading songs from YouTube and exporting them in mp3 format.

    Parameters:
    - urls (list, optional): List of URLs of songs to download. If not provided, the list will be empty.
    - export_path (str, optional): Path where downloaded songs will be saved. If not provided, the current file's directory will be used.

    Methods:
    - __init__(self, urls: list = None, export_path: str = ""):
        Initializes a new instance of the SongDownloader class.

    - download_song(self, url: str) -> None:
        Downloads a song from YouTube and exports it in mp3 format.

    - download_songs(self) -> None:
        Downloads all songs from the provided list of URLs.

    - export_song(self, downloaded_file: str, song_title: str) -> None:
        Exports the downloaded file in mp3 format and handles error cases.

    Attributes:
    - urls (list): List of URLs of songs to download.
    - export_path (str): Path where downloaded songs will be saved.
    """
    def __init__(self, urls: list = None, export_path: str = ""):
        self.urls = urls or []
        self.export_path = export_path or os.path.dirname(os.path.realpath(__file__))
        
    def download_song(self, url: str) -> None: 
        try:
            song = (
                YouTube(url, use_oauth = True)
                .streams
                .filter(only_audio=True)
                .first()
            )
            song_title = song.title
            downloaded_file = song.download(self.export_path)
            self.export_song(downloaded_file, song_title)
        except Exception as e: 
            print(f"Error al intentar descargar la canción: {e}")
    
    def download_songs(self) -> None: 
        if not self.urls: 
            print("Se necesita al menos una canción para descargar")
            return None
        for url in self.urls: 
            self.download_song(url)

    def export_song(self, downloaded_file: str, song_title: str) -> None: 
        try: 
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, os.path.join(self.export_path, new_file))
            print(f"La canción se ha descargado correctamente en la siguiente ruta:" + self.export_path)
        except FileExistsError: 
            print(f"La canción {song_title} descargar, ya existe en su dispositivo.")
            for downloaded_file in os.listdir(self.export_path):
                if re.search('mp4', downloaded_file):
                    mp4_path = os.path.join(self.export_path,downloaded_file)
                    os.remove(mp4_path)
