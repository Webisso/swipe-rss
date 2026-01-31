import xml.etree.ElementTree as ET
import requests
import feedparser

FEED_FILE = "feeds.opml"
TIMEOUT = 12

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8"
}


def check_feed(url: str):
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)

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


def find_parent(root, child):
    for parent in root.iter():
        if child in list(parent):
            return parent
    return None


tree = ET.parse(FEED_FILE)
root = tree.getroot()

total = 0
success_count = 0
failed = []

outlines = list(root.findall(".//outline"))

for outline in outlines:
    url = outline.attrib.get("xmlUrl")
    if not url:
        continue

    total += 1
    ok, reason = check_feed(url)

    if ok:
        success_count += 1
        continue

    failed.append({
        "title": outline.attrib.get("title", "—"),
        "url": url,
        "reason": reason
    })

    parent = find_parent(root, outline)
    if parent is not None:
        parent.remove(outline)

if failed:
    tree.write(FEED_FILE, encoding="utf-8", xml_declaration=True)


print(f"TOTAL={total}")
print(f"SUCCESS={success_count}")
print(f"FAILED={len(failed)}")

print("TABLE<<EOF")
print("| Title | URL | Status |")
print("|------|-----|--------|")

for f in failed:
    print(f"| {f['title']} | {f['url']} | ❌ {f['reason']} |")

if success_count:
    print(f"| — | {success_count} feeds | ✅ OK |")

print("EOF")
