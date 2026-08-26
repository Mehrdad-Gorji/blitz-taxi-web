import urllib.request
import re
import time

page_url = "https://commons.wikimedia.org/wiki/File:NIO_ET7_rear_view.jpg"
filename = "et7_rear.jpg"

time.sleep(2) # avoid 429
req = urllib.request.Request(page_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'class="fullImageLink".*?href="(https://upload.wikimedia.org/[^"]+)"', html)
    if match:
        img_url = match.group(1).replace("&amp;", "&")
        print("Found URL for", filename, ":", img_url)
        img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        img_data = urllib.request.urlopen(img_req).read()
        with open("img/" + filename, "wb") as f:
            f.write(img_data)
        print("Saved", filename)
    else:
        print("Could not find image URL in HTML for", page_url)
except Exception as e:
    print("Error for", page_url, e)

