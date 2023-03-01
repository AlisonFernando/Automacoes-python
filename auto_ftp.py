from ftplib import FTP
import time

ftp = FTP('[host]')

ftp.login('[username]', '[password]')

ftp.cwd('[Pasta no ftp para subir os arquivos]')

arquivos = ("[Arquivos para subir no ftp]")
i = 0
while i < len(arquivos):
    arquivoEnviado = arquivos[i]
    caminho = '[caminho dos arquivos que deseja subir no ftp]' + arquivoEnviado

    with open(caminho, 'rb') as arquivo:
        ftp.storbinary(f'STOR {arquivoEnviado}', arquivo)
    print(f'Arquivo enviado: {arquivoEnviado}')
    i += 1
    time.sleep(1)
