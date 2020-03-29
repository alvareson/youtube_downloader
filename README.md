youtube_downloader

Also need to edit the file .../lib/python3.6/site-packages/pytube/compat.py, add these lines under elif PY3:

elif PY3:
    from urllib import request
    from urllib.parse import quote, urlencode, parse_qsl, unquote
    from urllib.request import urlopen
