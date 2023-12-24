from backend.playlist_downloader import PlaylistDownloader
from backend.song_downloader import SongDownloader


song = SongDownloader(export_path='C:\\Users\\SID\\Documents\\proyects\\youtube-to-mp3')
song.download_song('https://music.youtube.com/watch?v=gqF2jGXi_Ak&list=RDAMVMfW8AS2VcIT8')