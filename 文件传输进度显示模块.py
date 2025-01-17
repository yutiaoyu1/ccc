from tqdm import tqdm
import requests

def upload_file_with_progress(file_path, url):
    with open(file_path, 'rb') as f:
        file_size = os.path.getsize(file_path)
        with tqdm(total=file_size, unit='B', unit_scale=True, desc=file_path) as progress:
            response = requests.post(url, files={'file': f}, stream=True)
            for chunk in response.iter_content(chunk_size=8192):
                progress.update(len(chunk))
    return response

def download_file_with_progress(file_url, save_path):
    response = requests.get(file_url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(save_path, 'wb') as f:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=save_path) as progress:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                progress.update(len(chunk))

