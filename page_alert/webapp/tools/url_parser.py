from urllib.parse import urlparse

def prettify_url(url:str):
    parse_result = urlparse(url)
    return parse_result.netloc
