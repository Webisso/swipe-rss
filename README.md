# Swipe RSS

A **multi-language RSS feed library** in OPML format. Use it in any RSS reader by subscribing to the single OPML URL.

## Feed URL

Use this URL in your RSS/OPML client:

**https://webisso.github.io/swipe-rss/feeds.opml**

## Purpose

- Curated RSS feeds grouped by category (science, technology, news, entertainment, culture, sports, economy, etc.).
- Multiple languages supported (e.g. Turkish, English).
- One URL to get the full feed list; no need to add feeds one by one.

## Contributing

New feeds and categories are welcome. Please open a **Pull Request** to add or suggest changes.

- Add feeds in the correct category and language section in `feeds.opml`.
- Keep the existing OPML structure and attribute names (`text`, `title`, `xmlUrl`, `type="rss"`).

## Example feed structure

Each feed entry in `feeds.opml` uses the same OPML outline attributes. Below are 10 example rows from different categories and languages.

| Language | Category | Type | Title | Text | URL |
|----------|----------|------|-------|------|-----|
| tr | baseFeed.science | rss | Evrim Ağacı | Evrim Ağacı | `https://evrimagaci.org/rss.xml` |
| tr | baseFeed.technology | rss | Webrazzi | Webrazzi | `https://webrazzi.com/feed` |
| tr | baseFeed.entertainment | rss | Kayıp Rıhtım | Kayıp Rıhtım | `https://kayiprihtim.com/feed/` |
| tr | baseFeed.cultureArt | rss | Arkitera | Arkitera | `https://www.arkitera.com/feed/` |
| tr | baseFeed.sports | rss | NTV Spor Futbol | NTV Spor Futbol | `https://www.ntvspor.net/rss/kategori/futbol` |
| tr | baseFeed.news | rss | BBC Türkçe | BBC Türkçe | `https://feeds.bbci.co.uk/turkce/rss.xml` |
| tr | baseFeed.defense | rss | C4 Defence | C4 Defence | `https://www.c4defence.com/feed/` |
| tr | baseFeed.economy | rss | Bloomberg HT | Bloomberg HT | `https://www.bloomberght.com/rss` |
| en | baseFeed.science | rss | ScienceDaily - Top Science | ScienceDaily - Top Science | `https://www.sciencedaily.com/rss/top/science.xml` |
| en | baseFeed.technology | rss | TechCrunch | TechCrunch | `https://techcrunch.com/feed/` |

In OPML XML, a single feed is one `<outline>` element, e.g.:

```xml
<outline type="rss" text="Webrazzi" title="Webrazzi" xmlUrl="https://webrazzi.com/feed"/>
```

- **Language** — Top-level grouping (`outline language="tr"` or `language="en"`).
- **Category** — Parent outline `text`/`title` (e.g. `baseFeed.science`, `baseFeed.technology`).
- **Type** — Always `rss` for feed entries.
- **Title** / **Text** — Display name of the feed (often identical).
- **URL** — Feed URL in the `xmlUrl` attribute.

## Repository

- **feeds.opml** — Main OPML file (served at the feed URL above).
- **scripts/** — Utilities (e.g. feed validation).
- **.github/workflows/** — Automation (e.g. feed checks).

## License

This project is free and open source. See [LICENSE](LICENSE) for details.

---

## Readme in other languages

| Language | Readme |
|----------|--------|
| العربية (ar-SA) | [readme/README.ar-SA.md](readme/README.ar-SA.md) |
| Català (ca) | [readme/README.ca.md](readme/README.ca.md) |
| 简体中文 (zh-Hans) | [readme/README.zh-Hans.md](readme/README.zh-Hans.md) |
| 繁體中文 (zh-Hant) | [readme/README.zh-Hant.md](readme/README.zh-Hant.md) |
| Hrvatski (hr) | [readme/README.hr.md](readme/README.hr.md) |
| Čeština (cs) | [readme/README.cs.md](readme/README.cs.md) |
| Dansk (da) | [readme/README.da.md](readme/README.da.md) |
| Nederlands (nl-NL) | [readme/README.nl-NL.md](readme/README.nl-NL.md) |
| English (en-AU) | [readme/README.en-AU.md](readme/README.en-AU.md) |
| English (en-CA) | [readme/README.en-CA.md](readme/README.en-CA.md) |
| English (en-GB) | [readme/README.en-GB.md](readme/README.en-GB.md) |
| English (en-US) | [readme/README.en-US.md](readme/README.en-US.md) |
| Suomi (fi) | [readme/README.fi.md](readme/README.fi.md) |
| Français (fr-FR) | [readme/README.fr-FR.md](readme/README.fr-FR.md) |
| Français (fr-CA) | [readme/README.fr-CA.md](readme/README.fr-CA.md) |
| Deutsch (de-DE) | [readme/README.de-DE.md](readme/README.de-DE.md) |
| Ελληνικά (el) | [readme/README.el.md](readme/README.el.md) |
| עברית (he) | [readme/README.he.md](readme/README.he.md) |
| हिन्दी (hi) | [readme/README.hi.md](readme/README.hi.md) |
| Magyar (hu) | [readme/README.hu.md](readme/README.hu.md) |
| Bahasa Indonesia (id) | [readme/README.id.md](readme/README.id.md) |
| Italiano (it) | [readme/README.it.md](readme/README.it.md) |
| 日本語 (ja) | [readme/README.ja.md](readme/README.ja.md) |
| 한국어 (ko) | [readme/README.ko.md](readme/README.ko.md) |
| Bahasa Melayu (ms) | [readme/README.ms.md](readme/README.ms.md) |
| Norsk (no) | [readme/README.no.md](readme/README.no.md) |
| Polski (pl) | [readme/README.pl.md](readme/README.pl.md) |
| Slovenščina (sl) | [readme/README.sl.md](readme/README.sl.md) |
| Português (pt) | [readme/README.pt.md](readme/README.pt.md) |
| فارسی (fa) | [readme/README.fa.md](readme/README.fa.md) |
| ਪੰਜਾਬੀ (pa) | [readme/README.pa.md](readme/README.pa.md) |
| Português (pt-BR) | [readme/README.pt-BR.md](readme/README.pt-BR.md) |
| Português (pt-PT) | [readme/README.pt-PT.md](readme/README.pt-PT.md) |
| Română (ro) | [readme/README.ro.md](readme/README.ro.md) |
| Русский (ru) | [readme/README.ru.md](readme/README.ru.md) |
| Slovenčina (sk) | [readme/README.sk.md](readme/README.sk.md) |
| Español (es-MX) | [readme/README.es-MX.md](readme/README.es-MX.md) |
| Español (es-ES) | [readme/README.es-ES.md](readme/README.es-ES.md) |
| Svenska (sv) | [readme/README.sv.md](readme/README.sv.md) |
| ไทย (th) | [readme/README.th.md](readme/README.th.md) |
| Türkçe (tr) | [readme/README.tr.md](readme/README.tr.md) |
| Українська (uk) | [readme/README.uk.md](readme/README.uk.md) |
| Tiếng Việt (vi) | [readme/README.vi.md](readme/README.vi.md) |
