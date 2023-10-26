from pytube import YouTube
import sys

# Insira o link do vídeo do YouTube
video_link = "https://www.youtube.com/watch?v=ZOgeWOds-Ek"

# Crie uma instância do objeto YouTube
yt = YouTube(video_link)

# Selecione a melhor resolução disponível
video = yt.streams.get_highest_resolution()

# Faça o download do vídeo
video.download()

# Finalize o código após o término do download
sys.exit()
