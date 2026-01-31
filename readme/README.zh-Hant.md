# Swipe RSS

OPML 格式的**多語系 RSS 訂閱庫**。在任一 RSS 閱讀器中訂閱此單一 OPML 網址即可使用。

## 訂閱網址

請在您的 RSS/OPML 用戶端中使用此網址：

**https://webisso.github.io/swipe-rss/feeds.opml**

## 用途

- 依類別整理的 RSS 訂閱源（科學、科技、新聞、娛樂、文化、體育、經濟等）。
- 支援多種語言（如土耳其語、英語）。
- 單一網址取得完整訂閱清單，無需逐筆新增。

## 參與貢獻

歡迎新增訂閱源或類別。請開啟 **Pull Request** 以新增或建議變更。

- 在 `feeds.opml` 中將訂閱源加入正確的類別與語言區塊。
- 維持現有 OPML 結構與屬性名稱（`text`、`title`、`xmlUrl`、`type="rss"`）。

## 訂閱源結構範例

`feeds.opml` 中每一筆訂閱源皆使用相同的 OPML outline 屬性。以下為來自不同類別與語言的 10 筆範例。

| 語言 | 類別 | 類型 | 標題 | 文字 | URL |
|------|------|------|------|------|-----|
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

在 OPML XML 中，一筆訂閱源對應一個 `<outline>` 元素，例如：

```xml
<outline type="rss" text="Webrazzi" title="Webrazzi" xmlUrl="https://webrazzi.com/feed"/>
```

- **語言** — 最上層分組（`outline language="tr"` 或 `language="en"`）。
- **類別** — 父層 outline 的 `text`/`title`（如 `baseFeed.science`、`baseFeed.technology`）。
- **類型** — 訂閱源條目一律為 `rss`。
- **標題** / **文字** — 訂閱源顯示名稱（通常相同）。
- **URL** — `xmlUrl` 屬性中的訂閱網址。

## 儲存庫

- **feeds.opml** — 主 OPML 檔（由上述網址提供）。
- **scripts/** — 工具（如訂閱源驗證）。
- **.github/workflows/** — 自動化（如訂閱源檢查）。

## 授權

本專案免費且開源。詳見 [LICENSE](../LICENSE)。

---

## 其他語言 README

| 語言 | README |
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
