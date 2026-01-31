# Swipe RSS

OPML形式の**多言語RSSフィードライブラリ**です。1つのOPML URLを登録するだけで、どのRSSリーダーでも利用できます。

## フィードURL

RSS/OPMLクライアントで次のURLを使用してください：

**https://webisso.github.io/swipe-rss/feeds.opml**

## 目的

- カテゴリ別に整理されたRSSフィード（科学、技術、ニュース、エンタメ、文化、スポーツ、経済など）。
- 複数言語対応（例：トルコ語、英語）。
- 1つのURLでフィード一覧を取得；フィードを1つずつ追加する必要はありません。

## 貢献

新しいフィードやカテゴリを歓迎します。追加や変更の提案は**Pull Request**でお願いします。

- `feeds.opml`の適切なカテゴリと言語セクションにフィードを追加してください。
- 既存のOPML構造と属性名（`text`、`title`、`xmlUrl`、`type="rss"`）を維持してください。

## フィード構造の例

`feeds.opml`内の各フィードエントリは同じOPML outline属性を使用します。以下は異なるカテゴリと言語からの10行の例です。

| 言語 | カテゴリ | タイプ | タイトル | テキスト | URL |
|------|----------|--------|----------|----------|-----|
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

OPML XMLでは、1つのフィードが1つの`<outline>`要素です。例：

```xml
<outline type="rss" text="Webrazzi" title="Webrazzi" xmlUrl="https://webrazzi.com/feed"/>
```

- **言語** — 最上位のグループ（`outline language="tr"` または `language="en"`）。
- **カテゴリ** — 親outlineの`text`/`title`（例：`baseFeed.science`、`baseFeed.technology`）。
- **タイプ** — フィードエントリは常に`rss`。
- **タイトル** / **テキスト** — フィードの表示名（多くの場合同じ）。
- **URL** — `xmlUrl`属性のフィードURL。

## リポジトリ

- **feeds.opml** — メインOPMLファイル（上記フィードURLで配信）。
- **scripts/** — ユーティリティ（例：フィード検証）。
- **.github/workflows/** — 自動化（例：フィードチェック）。

## ライセンス

このプロジェクトは無料かつオープンソースです。詳細は[LICENSE](../LICENSE)を参照してください。

---

## 他の言語のREADME

| 言語 | README |
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
