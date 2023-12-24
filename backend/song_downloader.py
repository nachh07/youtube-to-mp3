import os
from pytube import YouTube

class SongDownloader: 
    """
    Clase que permite descargar el audio de un video y exportarlo a mp3. 
    
    params: 
        urls (list): Listado de url de videos y/o canciones para descargar. 

    """
    def __init__(self, urls: list = None, export_path: str = "", auth: bool = True):
        self.urls = urls or []
        self.export_path = export_path or os.path.dirname(os.path.realpath(__file__))
        self.auth = auth

    def download_song(self, url: str) -> None: 
        try:
            song = (
                YouTube(url, use_oauth = self.auth)
                .streams
                .filter(only_audio=True)
                .first()
            )
            downloaded_file = song.download(self.export_path)
            self.export_song(downloaded_file)
        except Exception as e: 
            print(f"Error al intentar descargar la canción: {e}")
    
    def download_songs(self) -> None: 
        if not self.urls: 
            print("Se necesita al menos una canción para descargar")
            return None
        for url in self.urls: 
            self.download_song(url)

    def export_song(self, downloaded_file: str) -> None: 
        try: 
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, os.path.join(self.export_path, new_file))
            print(f"La canción se ha descargado correctamente en la siguiente ruta:" + self.export_path)
        except FileExistsError as e: 
            print("La canción que está intentando de descargar, ya existe en su dispositivo.")


song = SongDownloader(export_path='C:\\Users\\SID\\Documents\\proyects\\youtube-to-mp3\\songs')

song.download_song('https://music.youtube.com/watch?v=gqF2jGXi_Ak&list=RDAMVMfW8AS2VcIT8')