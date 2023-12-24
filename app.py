from flask import Flask, render_template, request
from song_downloader import SongDownloader
from playlist_downloader import PlaylistDownloader

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        urls = request.form.getlist('urls')
        download_type = request.form['download_type']
        path = request.form['path']
        if not urls:
            return render_template('index.html', message='Se necesita al menos una URL para descargar.')

        if download_type == 'single':
            #downloader = SongDownloader(urls=urls)
            downloader = SongDownloader(urls=urls, export_path=path)
        elif download_type == 'playlist':
            downloader = PlaylistDownloader()
            return render_template('index.html', message='Descarga de listas de reproducción no implementada aún.')

        downloader.download_songs()

        return render_template('index.html', message='Descarga completada. Verifica la consola para detalles.')

if __name__ == '__main__':
    app.run(debug=True)
