import os
from pytube import YouTube
import re

class SongDownloader: 
    """
    Clase que permite descargar el audio de un video y exportarlo a mp3. 
    
    params: 
        urls (list): Listado de url de videos y/o canciones para descargar. 

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
        except FileExistsError as e: 
            print(f"La canción {song_title} descargar, ya existe en su dispositivo.")
            for downloaded_file in os.listdir(self.export_path):
                if re.search('mp4', downloaded_file):
                    mp4_path = os.path.join(self.export_path,downloaded_file)
                    os.remove(mp4_path)

