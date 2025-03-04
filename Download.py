import os
import shutil
import requests

# Configurações globais
HEADERS = {"User-Agent": "Mozilla/5.0"}
OUTPUT_DIR = os.path.join(os.getcwd(), "iMPlayer")

def download_file(url, save_path):
    """
    Baixa um arquivo da URL fornecida e sobrescreve se já existir.
    """
    try:
        print(f"Baixando arquivo de: {url}")
        response = requests.get(url, headers=HEADERS, timeout=10)

        if response.status_code == 200:
            # Garante que o diretório de destino exista
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            # Salva o conteúdo do arquivo
            with open(save_path, 'wb') as file:
                file.write(response.content)
            
            # Verifica se o arquivo foi salvo corretamente
            if os.path.getsize(save_path) > 0:
                print(f"Arquivo salvo com sucesso: {save_path}")
            else:
                print(f"Erro: Arquivo vazio ou corrompido: {save_path}")
        else:
            print(f"Falha ao baixar {url}. Código: {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"Erro: Timeout ao baixar {url}")
    except requests.exceptions.ConnectionError:
        print(f"Erro: Problema de conexão ao baixar {url}")
    except Exception as e:
        print(f"Erro inesperado ao baixar {url}: {e}")

if __name__ == "__main__":
    # Remove a pasta iMPlayer antes de baixar os arquivos
    print("Limpando diretório anterior...")
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Lista de arquivos para download
    files_to_download = {
        "m3u": [
            "http://m3u4u.com/m3u/3wk1y24kx7uzdevxygz7",
            "http://m3u4u.com/m3u/jq2zy9epr3bwxmgwyxr5",
            "http://m3u4u.com/m3u/782dyqdrqkh1xegen4zp",
            "https://gitlab.com/josieljefferson12/playlists/-/raw/main/PiauiTV.m3u",
            "https://gitlab.com/josieljefferson12/playlists/-/raw/main/m3u4u_proton.me.m3u"
        ],
        "xml.gz": [
            "http://m3u4u.com/epg/3wk1y24kx7uzdevxygz7",
            "http://m3u4u.com/epg/jq2zy9epr3bwxmgwyxr5",
            "http://m3u4u.com/epg/782dyqdrqkh1xegen4zp"
        ]
    }

    # Processa o download dos arquivos
    print("Iniciando download dos arquivos...")
    for ext, urls in files_to_download.items():
        for index, url in enumerate(urls, start=1):
            save_path = os.path.join(OUTPUT_DIR, f"iMPlayer_{index}.{ext}")
            download_file(url, save_path)

    print("Download concluído.")
