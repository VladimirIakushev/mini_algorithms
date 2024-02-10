def normalize_url(url):
    url_https = url[:8]
    url_http = url[:7]
    url_norm = []

    if url_https == 'https://':
        url_norm = url
        return url_norm

    if url_http == 'http://':
        url_norm = 'https://' + url[7:]
        return url_norm

    else:
        url_norm = 'https://' + url
        return url_norm


print(normalize_url('https://ya.ru'))  # https://ya.ru
print(normalize_url('google.com'))  # https://google.com
print(normalize_url('http://ai.fi'))  # https://ai.fi