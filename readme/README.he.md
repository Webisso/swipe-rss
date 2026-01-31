# Swipe RSS

**ספריית פידים RSS רב־לשונית** בפורמט OPML. השתמשו בה בכל קורא RSS על ידי הרשמה לכתובת OPML אחת.

## כתובת הפיד

השתמשו בכתובת הזו בקליינט RSS/OPML שלכם:

**https://webisso.github.io/swipe-rss/feeds.opml**

## מטרה

- פידים RSS נבחרים מקובצים לפי קטגוריה (מדע, טכנולוגיה, חדשות, בידור, תרבות, ספורט, כלכלה וכו').
- תמיכה במספר שפות (למשל טורקית, אנגלית).
- כתובת אחת לקבלת רשימת הפידים המלאה; אין צורך להוסיף פידים אחד־אחד.

## תרומה

פידים וקטגוריות חדשים מתקבלים בברכה. פתחו **Pull Request** כדי להוסיף או להציע שינויים.

- הוסיפו פידים בקטגוריה ובמקטע השפה הנכונים ב־`feeds.opml`.
- שמרו על מבנה ה־OPML הקיים ושמות המאפיינים (`text`, `title`, `xmlUrl`, `type="rss"`).

## דוגמת מבנה פיד

כל רשומת פיד ב־`feeds.opml` משתמשת באותם מאפייני outline של OPML. להלן 10 שורות דוגמה מקטגוריות ושפות שונות.

| שפה | קטגוריה | סוג | כותרת | טקסט | URL |
|-----|---------|-----|-------|------|-----|
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

ב־XML של OPML, פיד אחד הוא אלמנט `<outline>` אחד, למשל:

```xml
<outline type="rss" text="Webrazzi" title="Webrazzi" xmlUrl="https://webrazzi.com/feed"/>
```

- **שפה** — קיבוץ ברמה העליונה (`outline language="tr"` או `language="en"`).
- **קטגוריה** — `text`/`title` של ה־outline האב (למשל `baseFeed.science`, `baseFeed.technology`).
- **סוג** — תמיד `rss` לרשומות פיד.
- **כותרת** / **טקסט** — שם התצוגה של הפיד (לעתים זהים).
- **URL** — כתובת הפיד במאפיין `xmlUrl`.

## מאגר

- **feeds.opml** — קובץ OPML הראשי (משודר בכתובת הפיד למעלה).
- **scripts/** — כלי עזר (למשל אימות פידים).
- **.github/workflows/** — אוטומציה (למשל בדיקות פידים).

## רישיון

הפרויקט הזה חינמי וקוד פתוח. לפרטים ראו [LICENSE](../LICENSE).

---

## README בשפות אחרות

| שפה | README |
|-----|--------|
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
