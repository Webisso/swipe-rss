# Swipe RSS

Et **flersproget RSS-feed-bibliotek** i OPML-format. Brug det i enhver RSS-læser ved at abonnere på den enkelte OPML-URL.

## Feed-URL

Brug denne URL i din RSS/OPML-klient:

**https://webisso.github.io/swipe-rss/feeds.opml**

## Formål

- Udvalgte RSS-feeds grupperet efter kategori (videnskab, teknologi, nyheder, underholdning, kultur, sport, økonomi osv.).
- Flere sprog understøttet (f.eks. tyrkisk, engelsk).
- Én URL til hele feed-listen; ingen grund til at tilføje feeds én ad gangen.

## Bidrag

Nye feeds og kategorier er velkomne. Åbn en **Pull Request** for at tilføje eller foreslå ændringer.

- Tilføj feeds i den rigtige kategori og sprogsektion i `feeds.opml`.
- Bevar den eksisterende OPML-struktur og attributnavne (`text`, `title`, `xmlUrl`, `type="rss"`).

## Eksempel på feed-struktur

Hver feed-posting i `feeds.opml` bruger de samme OPML-outline-attributter. Nedenfor er 10 eksempelrækker fra forskellige kategorier og sprog.

| Sprog | Kategori | Type | Titel | Tekst | URL |
|-------|----------|------|-------|-------|-----|
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

I OPML XML er én feed ét `<outline>`-element, f.eks.:

```xml
<outline type="rss" text="Webrazzi" title="Webrazzi" xmlUrl="https://webrazzi.com/feed"/>
```

- **Sprog** — Gruppering på øverste niveau (`outline language="tr"` eller `language="en"`).
- **Kategori** — Overordnet outlines `text`/`title` (f.eks. `baseFeed.science`, `baseFeed.technology`).
- **Type** — Altid `rss` for feed-poster.
- **Titel** / **Tekst** — Feedens visningsnavn (ofte ens).
- **URL** — Feed-URL i attributten `xmlUrl`.

## Repository

- **feeds.opml** — Hoved-OPML-fil (serveret på feed-URL'en ovenfor).
- **scripts/** — Værktøjer (f.eks. feed-validering).
- **.github/workflows/** — Automatisering (f.eks. feed-tjek).

## Licens

Dette projekt er gratis og open source. Se [LICENSE](../LICENSE) for detaljer.

---

## README på andre sprog

| Sprog | README |
|-------|--------|
| العربية (ar-SA) | [README.ar-SA.md](README.ar-SA.md) |
| Català (ca) | [README.ca.md](README.ca.md) |
| 简体中文 (zh-Hans) | [README.zh-Hans.md](README.zh-Hans.md) |
| 繁體中文 (zh-Hant) | [README.zh-Hant.md](README.zh-Hant.md) |
| Hrvatski (hr) | [README.hr.md](README.hr.md) |
| Čeština (cs) | [README.cs.md](README.cs.md) |
| Dansk (da) | [README.da.md](README.da.md) |
| Nederlands (nl-NL) | [README.nl-NL.md](README.nl-NL.md) |
| English (en-AU) | [README.en-AU.md](README.en-AU.md) |
| English (en-CA) | [README.en-CA.md](README.en-CA.md) |
| English (en-GB) | [README.en-GB.md](README.en-GB.md) |
| English (en-US) | [README.en-US.md](README.en-US.md) |
| Suomi (fi) | [README.fi.md](README.fi.md) |
| Français (fr-FR) | [README.fr-FR.md](README.fr-FR.md) |
| Français (fr-CA) | [README.fr-CA.md](README.fr-CA.md) |
| Deutsch (de-DE) | [README.de-DE.md](README.de-DE.md) |
| Ελληνικά (el) | [README.el.md](README.el.md) |
| עברית (he) | [README.he.md](README.he.md) |
| हिन्दी (hi) | [README.hi.md](README.hi.md) |
| Magyar (hu) | [README.hu.md](README.hu.md) |
| Bahasa Indonesia (id) | [README.id.md](README.id.md) |
| Italiano (it) | [README.it.md](README.it.md) |
| 日本語 (ja) | [README.ja.md](README.ja.md) |
| 한국어 (ko) | [README.ko.md](README.ko.md) |
| Bahasa Melayu (ms) | [README.ms.md](README.ms.md) |
| Norsk (no) | [README.no.md](README.no.md) |
| Polski (pl) | [README.pl.md](README.pl.md) |
| Slovenščina (sl) | [README.sl.md](README.sl.md) |
| Português (pt) | [README.pt.md](README.pt.md) |
| فارسی (fa) | [README.fa.md](README.fa.md) |
| ਪੰਜਾਬੀ (pa) | [README.pa.md](README.pa.md) |
| Português (pt-BR) | [README.pt-BR.md](README.pt-BR.md) |
| Português (pt-PT) | [README.pt-PT.md](README.pt-PT.md) |
| Română (ro) | [README.ro.md](README.ro.md) |
| Русский (ru) | [README.ru.md](README.ru.md) |
| Slovenčina (sk) | [README.sk.md](README.sk.md) |
| Español (es-MX) | [README.es-MX.md](README.es-MX.md) |
| Español (es-ES) | [README.es-ES.md](README.es-ES.md) |
| Svenska (sv) | [README.sv.md](README.sv.md) |
| ไทย (th) | [README.th.md](README.th.md) |
| Türkçe (tr) | [README.tr.md](README.tr.md) |
| Українська (uk) | [README.uk.md](README.uk.md) |
| Tiếng Việt (vi) | [README.vi.md](README.vi.md) |
