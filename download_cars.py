import urllib.request
import re

urls = [
    "https://commons.wikimedia.org/wiki/File:NIO_ET7_1X7A6681.jpg",
    "https://commons.wikimedia.org/wiki/File:Nio_ET7,_IAA_Mobility_2023,_Munich_(P1110356).jpg",
    "https://commons.wikimedia.org/wiki/File:NIO_ET7_rear_view.jpg"
]

filenames = ["et7_front.jpg", "et7_side.jpg", "et7_rear.jpg"]

for page_url, filename in zip(urls, filenames):
    req = urllib.request.Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'class="fullImageLink".*?href="(https://upload.wikimedia.org/[^"]+)"', html)
        if match:
            img_url = match.group(1)
            print("Found URL for", filename, ":", img_url)
            img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            img_data = urllib.request.urlopen(img_req).read()
            with open("img/" + filename, "wb") as f:
                f.write(img_data)
            print("Saved", filename)
        else:
            print("Could not find image URL in HTML for", page_url)
    except Exception as e:
        print("Error for", page_url, e)

