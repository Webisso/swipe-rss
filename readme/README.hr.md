# Swipe RSS

**Višejezična knjižnica RSS feedova** u OPML formatu. Koristite je u bilo kojem RSS čitaču pretplatom na jednu OPML adresu.

## URL feeda

U svom RSS/OPML klijentu koristite ovu adresu:

**https://webisso.github.io/swipe-rss/feeds.opml**

## Svrha

- Odabrani RSS feedovi grupirani po kategorijama (znanost, tehnologija, vijesti, zabava, kultura, sport, ekonomija itd.).
- Podrška za više jezika (npr. turski, engleski).
- Jedna adresa za cijeli popis feedova; nema potrebe dodavati feedove jedan po jedan.

## Doprinos

Novi feedovi i kategorije su dobrodošli. Otvorite **Pull Request** za dodavanje ili prijedlog izmjena.

- Dodajte feedove u odgovarajuću kategoriju i jezičnu sekciju u `feeds.opml`.
- Zadržite postojeću OPML strukturu i nazive atributa (`text`, `title`, `xmlUrl`, `type="rss"`).

## Primjer strukture feeda

Svaki unos feeda u `feeds.opml` koristi iste OPML outline atribute. Ispod je 10 primjera iz različitih kategorija i jezika.

| Jezik | Kategorija | Tip | Naslov | Tekst | URL |
|-------|------------|-----|--------|-------|-----|
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

U OPML XML-u jedan feed je jedan element `<outline>`, npr.:

```xml
<outline type="rss" text="Webrazzi" title="Webrazzi" xmlUrl="https://webrazzi.com/feed"/>
```

- **Jezik** — Grupiranje na najvišoj razini (`outline language="tr"` ili `language="en"`).
- **Kategorija** — `text`/`title` roditeljskog outlinea (npr. `baseFeed.science`, `baseFeed.technology`).
- **Tip** — Za unose feeda uvijek `rss`.
- **Naslov** / **Tekst** — Prikazni naziv feeda (često isti).
- **URL** — Adresa feeda u atributu `xmlUrl`.

## Repozitorij

- **feeds.opml** — Glavna OPML datoteka (dostupna na gornjoj adresi).
- **scripts/** — Alati (npr. provjera feedova).
- **.github/workflows/** — Automatizacija (npr. provjere feedova).

## Licenca

Ovaj je projekt besplatan i otvorenog koda. Pojedinosti u [LICENSE](../LICENSE).

---

## README na drugim jezicima

| Jezik | README |
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
