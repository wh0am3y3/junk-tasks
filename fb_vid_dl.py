#!/usr/bin/env python
import requests as r
import re
import sys

url = sys.argv[-1]
html = r.get(url)
video_url = re.search('hd_src:"(.+?)"', html.text).group(1)
print(video_url)
