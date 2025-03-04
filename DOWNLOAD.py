import os
import requests

HEADERS = {"User-Agent": "Mozilla/5.0"}

def download_file(url, save_path):
    """
    Baixa um arquivo da URL fornecida e sobrescreve se já existir.
    """
    try:
        print(f"Baixando arquivo de: {url}")
        response = requests.get(url, headers=HEADERS, timeout=10)

        if response.status_code == 200:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Arquivo salvo: {save_path}")
        else:
            print(f"Falha ao baixar {url}. Código: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar {url}: {e}")

if __name__ == "__main__":
    output_dir = os.path.join(os.getcwd(), "iMPlayer")
    os.makedirs(output_dir, exist_ok=True)

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

    for ext, urls in files_to_download.items():
        for index, url in enumerate(urls, start=1):
            save_path = os.path.join(output_dir, f"iMPlayer_{index}.{ext}")
            download_file(url, save_path)
