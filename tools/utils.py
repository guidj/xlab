import os.path

def download_file(url, filepath=None):
    
    if filepath:
        if filepath.endswith('/'):
            filename = url.split('/')[-1]
            filepath = os.path.join(filepath, filename)
    else:
        filepath = url.split('/')[-1]
            
    r = requests.get(url, stream=True)
    with open(filepath, 'wb') as fp:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                fp.write(chunk)
    return filepath