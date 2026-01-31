import xml.etree.ElementTree as ET
import requests
import feedparser
from copy import deepcopy

FEED_FILE = "feeds.opml"
TIMEOUT = 12

tree = ET.parse(FEED_FILE)
root = tree.getroot()

namespaces = {"opml": "http://opml.org/spec2"}
removed = []

def is_feed_broken(url: str) -> str | None:
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8"
        }

        r = requests.get(url, timeout=TIMEOUT, headers=headers)

        if r.status_code != 200:
            return f"HTTP {r.status_code}"

        feed = feedparser.parse(r.content)

        if feed.bozo:
            return "Invalid RSS/XML"

        if not feed.entries:
            return "No entries"

        return None

    except Exception as e:
        return str(e)

for parent in root.findall(".//outline"):
    children = list(parent)
    for child in children:
        url = child.attrib.get("xmlUrl")
        if not url:
            continue

        error = is_feed_broken(url)
        if error:
            removed.append((child.attrib.get("title", url), url, error))
            parent.remove(child)

# Değişiklik varsa dosyayı yaz
if removed:
    tree.write(FEED_FILE, encoding="utf-8", xml_declaration=True)

    print("Removed broken feeds:")
    for title, url, err in removed:
        print(f"- {title} | {url} | {err}")
else:
    print("No broken feeds found")