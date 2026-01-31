import xml.etree.ElementTree as ET
import requests
import feedparser
import uuid
from datetime import datetime

FEED_FILE = "feeds.opml"
TIMEOUT = 12

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8"
}

def check_feed(url: str):
    try:
        r = requests.get(url, timeout=TIMEOUT, headers=headers)

        if r.status_code != 200:
            return False, f"HTTP {r.status_code}"

        feed = feedparser.parse(r.content)

        if feed.bozo:
            return False, "Invalid RSS/XML"

        if not feed.entries:
            return False, "No entries"

        return True, "OK"

    except Exception as e:
        return False, str(e)


tree = ET.parse(FEED_FILE)
root = tree.getroot()

total = 0
ok = 0
failed = []

# sadece child outline’ları dolaş
for parent in root.findall(".//outline"):
    for child in list(parent):
        url = child.attrib.get("xmlUrl")
        if not url:
            continue

        total += 1
        success, reason = check_feed(url)

        if success:
            ok += 1
        else:
            failed.append({
                "title": child.attrib.get("title", "—"),
                "url": url,
                "reason": reason
            })
            parent.remove(child)

if failed:
    tree.write(FEED_FILE, encoding="utf-8", xml_declaration=True)

print(f"TOTAL={total}")
print(f"SUCCESS={ok}")
print(f"FAILED={len(failed)}")

print("TABLE<<EOF")
print("| Title | URL | Status |")
print("|------|-----|--------|")

for f in failed:
    print(f"| {f['title']} | {f['url']} | ❌ {f['reason']} |")

if ok:
    print(f"| — | {ok} feeds | ✅ OK |")

print("EOF")
