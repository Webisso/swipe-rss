# Swipe RSS

Uma **biblioteca de feeds RSS multilingue** em formato OPML. Use-a em qualquer leitor RSS subscrevendo o único URL OPML.

## URL do feed

Utilize este URL no seu cliente RSS/OPML:

**https://webisso.github.io/swipe-rss/feeds.opml**

## Objetivo

- Feeds RSS curados agrupados por categoria (ciência, tecnologia, notícias, entretenimento, cultura, desporto, economia, etc.).
- Vários idiomas suportados (ex.: turco, inglês).
- Um URL para a lista completa de feeds; não é preciso adicionar feeds um a um.

## Contribuir

Novos feeds e categorias são bem-vindos. Abra um **Pull Request** para adicionar ou sugerir alterações.

- Adicione feeds na categoria e secção de idioma correctas em `feeds.opml`.
- Mantenha a estrutura OPML e os nomes dos atributos existentes (`text`, `title`, `xmlUrl`, `type="rss"`).

## Exemplo de estrutura de feed

Cada entrada de feed em `feeds.opml` utiliza os mesmos atributos outline OPML. Abaixo estão 10 linhas de exemplo de diferentes categorias e idiomas.

| Idioma | Categoria | Tipo | Título | Texto | URL |
|--------|-----------|------|--------|-------|-----|
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

Em OPML XML, um feed é um elemento `<outline>`, por ex.:

```xml
<outline type="rss" text="Webrazzi" title="Webrazzi" xmlUrl="https://webrazzi.com/feed"/>
```

- **Idioma** — Agrupamento de topo (`outline language="tr"` ou `language="en"`).
- **Categoria** — `text`/`title` do outline pai (ex.: `baseFeed.science`, `baseFeed.technology`).
- **Tipo** — Para entradas de feed é sempre `rss`.
- **Título** / **Texto** — Nome de exibição do feed (muitas vezes igual).
- **URL** — URL do feed no atributo `xmlUrl`.

## Repositório

- **feeds.opml** — Ficheiro OPML principal (servido no URL do feed acima).
- **scripts/** — Utilitários (ex.: validação de feeds).
- **.github/workflows/** — Automação (ex.: verificações de feeds).

## Licença

Este projeto é gratuito e de código aberto. Consulte [LICENSE](../LICENSE) para detalhes.

---

## README noutros idiomas

| Idioma | README |
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
