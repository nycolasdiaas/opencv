import yt_dlp

# URL do vídeo que você deseja baixar
url = 'https://www.youtube.com/watch?v=Gr0HpDM8Ki8&list=PLcQZGj9lFR7y5WikozDSrdk6UCtAnM9mB&index=5'

ydl_opts = {
    'format': 'best',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download concluído!")