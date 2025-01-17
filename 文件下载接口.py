import requests

def upload_file(file_path, url):
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
    return response

def download_file(file_url, save_path):
    response = requests.get(file_url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

