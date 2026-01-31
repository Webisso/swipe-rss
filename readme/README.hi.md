# Swipe RSS

OPML फॉर्मैट में एक **बहुभाषी RSS फ़ीड लाइब्रेरी**। एक ही OPML URL की सदस्यता लेकर किसी भी RSS रीडर में इस्तेमाल करें।

## फ़ीड URL

अपने RSS/OPML क्लाइंट में यह URL इस्तेमाल करें:

**https://webisso.github.io/swipe-rss/feeds.opml**

## उद्देश्य

- श्रेणी के हिसाब से चुनी हुई RSS फ़ीड्स (विज्ञान, तकनीक, खबरें, मनोरंजन, संस्कृति, खेल, अर्थव्यवस्था आदि)।
- कई भाषाओं का समर्थन (जैसे तुर्की, अंग्रेज़ी)।
- पूरी फ़ीड सूची के लिए एक URL; फ़ीड्स एक-एक कर जोड़ने की ज़रूरत नहीं।

## योगदान

नई फ़ीड्स और श्रेणियाँ स्वागतयोग्य हैं। जोड़ने या बदलाव सुझाने के लिए **Pull Request** खोलें।

- `feeds.opml` में सही श्रेणी और भाषा वाले सेक्शन में फ़ीड्स जोड़ें।
- मौजूदा OPML संरचना और एट्रिब्यूट नाम बनाए रखें (`text`, `title`, `xmlUrl`, `type="rss"`)।

## फ़ीड संरचना उदाहरण

`feeds.opml` में हर फ़ीड एंट्री वही OPML outline एट्रिब्यूट इस्तेमाल करती है। नीचे अलग-अलग श्रेणियों और भाषाओं की 10 उदाहरण पंक्तियाँ हैं।

| भाषा | श्रेणी | प्रकार | शीर्षक | टेक्स्ट | URL |
|------|--------|--------|--------|--------|-----|
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

OPML XML में एक फ़ीड एक `<outline>` एलिमेंट होता है, जैसे:

```xml
<outline type="rss" text="Webrazzi" title="Webrazzi" xmlUrl="https://webrazzi.com/feed"/>
```

- **भाषा** — टॉप-लेवल ग्रुपिंग (`outline language="tr"` या `language="en"`)।
- **श्रेणी** — पैरेंट outline का `text`/`title` (जैसे `baseFeed.science`, `baseFeed.technology`)।
- **प्रकार** — फ़ीड एंट्रीज़ के लिए हमेशा `rss`।
- **शीर्षक** / **टेक्स्ट** — फ़ीड का दिखने वाला नाम (अक्सर एक जैसा)।
- **URL** — `xmlUrl` एट्रिब्यूट में फ़ीड का URL।

## रिपॉज़िटरी

- **feeds.opml** — मुख्य OPML फ़ाइल (ऊपर दिए फ़ीड URL पर सर्व की जाती है)।
- **scripts/** — उपयोगिताएँ (जैसे फ़ीड वैलिडेशन)।
- **.github/workflows/** — ऑटोमेशन (जैसे फ़ीड चेक)।

## लाइसेंस

यह प्रोजेक्ट मुफ़्त और ओपन सोर्स है। विवरण के लिए [LICENSE](../LICENSE) देखें।

---

## अन्य भाषाओं में README

| भाषा | README |
|------|--------|
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
