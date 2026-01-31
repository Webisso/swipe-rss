# Swipe RSS

OPML 형식의 **다국어 RSS 피드 라이브러리**입니다. 하나의 OPML URL만 구독하면 어떤 RSS 리더에서든 사용할 수 있습니다.

## 피드 URL

RSS/OPML 클라이언트에서 다음 URL을 사용하세요:

**https://webisso.github.io/swipe-rss/feeds.opml**

## 목적

- 카테고리별로 정리된 RSS 피드(과학, 기술, 뉴스, 엔터테인먼트, 문화, 스포츠, 경제 등).
- 여러 언어 지원(예: 터키어, 영어).
- 하나의 URL로 전체 피드 목록을 받을 수 있으며, 피드를 하나씩 추가할 필요가 없습니다.

## 기여

새 피드와 카테고리를 환영합니다. 추가나 변경을 제안하려면 **Pull Request**를 열어 주세요.

- `feeds.opml`에서 올바른 카테고리와 언어 섹션에 피드를 추가하세요.
- 기존 OPML 구조와 속성 이름(`text`, `title`, `xmlUrl`, `type="rss"`)을 유지하세요.

## 피드 구조 예시

`feeds.opml`의 각 피드 항목은 동일한 OPML outline 속성을 사용합니다. 아래는 서로 다른 카테고리와 언어에서 가져온 10개 예시 행입니다.

| 언어 | 카테고리 | 유형 | 제목 | 텍스트 | URL |
|------|----------|------|------|--------|-----|
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

OPML XML에서 하나의 피드는 하나의 `<outline>` 요소입니다. 예:

```xml
<outline type="rss" text="Webrazzi" title="Webrazzi" xmlUrl="https://webrazzi.com/feed"/>
```

- **언어** — 최상위 그룹(`outline language="tr"` 또는 `language="en"`).
- **카테고리** — 부모 outline의 `text`/`title`(예: `baseFeed.science`, `baseFeed.technology`).
- **유형** — 피드 항목은 항상 `rss`.
- **제목** / **텍스트** — 피드 표시 이름(대부분 동일).
- **URL** — `xmlUrl` 속성의 피드 URL.

## 저장소

- **feeds.opml** — 메인 OPML 파일(위 피드 URL로 제공).
- **scripts/** — 유틸리티(예: 피드 검증).
- **.github/workflows/** — 자동화(예: 피드 검사).

## 라이선스

이 프로젝트는 무료이며 오픈 소스입니다. 자세한 내용은 [LICENSE](../LICENSE)를 참조하세요.

---

## 다른 언어의 README

| 언어 | README |
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
