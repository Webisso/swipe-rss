# Swipe RSS

Une **bibliothèque de flux RSS multilingue** au format OPML. Utilisez-la dans tout lecteur RSS en vous abonnant à l’unique URL OPML.

## URL du flux

Utilisez cette URL dans votre client RSS/OPML :

**https://webisso.github.io/swipe-rss/feeds.opml**

## Objectif

- Flux RSS sélectionnés et regroupés par catégorie (science, technologie, actualités, divertissement, culture, sport, économie, etc.).
- Plusieurs langues prises en charge (ex. turc, anglais).
- Une seule URL pour obtenir la liste complète des flux ; pas besoin d’ajouter les flux un par un.

## Contribuer

Les nouveaux flux et catégories sont les bienvenus. Ouvrez une **Pull Request** pour proposer des ajouts ou des modifications.

- Ajoutez les flux dans la bonne catégorie et la section de langue dans `feeds.opml`.
- Conservez la structure OPML et les noms d’attributs existants (`text`, `title`, `xmlUrl`, `type="rss"`).

## Exemple de structure d’un flux

Chaque entrée de flux dans `feeds.opml` utilise les mêmes attributs outline OPML. Voici 10 lignes d’exemple issues de différentes catégories et langues.

| Langue | Catégorie | Type | Titre | Texte | URL |
|--------|-----------|------|-------|-------|-----|
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

En XML OPML, un flux correspond à un élément `<outline>`, par ex. :

```xml
<outline type="rss" text="Webrazzi" title="Webrazzi" xmlUrl="https://webrazzi.com/feed"/>
```

- **Langue** — Regroupement de premier niveau (`outline language="tr"` ou `language="en"`).
- **Catégorie** — `text`/`title` de l’outline parent (ex. `baseFeed.science`, `baseFeed.technology`).
- **Type** — Toujours `rss` pour les entrées de flux.
- **Titre** / **Texte** — Nom d’affichage du flux (souvent identique).
- **URL** — URL du flux dans l’attribut `xmlUrl`.

## Dépôt

- **feeds.opml** — Fichier OPML principal (servi à l’URL ci-dessus).
- **scripts/** — Utilitaires (ex. validation des flux).
- **.github/workflows/** — Automatisation (ex. vérifications des flux).

## Licence

Ce projet est gratuit et open source. Voir [LICENSE](../LICENSE) pour les détails.

---

## README dans d’autres langues

| Langue | README |
|--------|--------|
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
