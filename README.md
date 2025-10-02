# クリックポスト → Amazon 出荷通知 変換ツール

クリックポストの出力CSVを、Amazonの「出荷通知アップロード」用フォーマット（CP932、タブ区切り、全56列固定、CRLF）に変換します。Python版（推奨）とブラウザ版（簡易）を同梱しています。

## 目次

- 必要なファイル
- Python版（推奨）
- ブラウザ版（簡易）
- 設定ファイル
- トラブルシューティング

## 必要なファイル

| ファイル | 説明 |
|---------|------|
| `input/*.csv` | クリックポストの出力ファイル（任意名、エンコード自動判定） |
| `config/template_columns.json` | Amazonテンプレートのヘッダー・列定義（JSON） |
| `config/mapping.json` | 列マッピング設定（UTF-8、`sample/mapping_prompt.txt`参照） |
| `config/config.json` | 入出力や日付形式、出力制御の共通設定 |

## Python版（推奨）

### 動作条件
- Python 3.6 以上
- 追加ライブラリ不要（標準ライブラリのみ）

### 使い方
1. 設定ファイルを用意
   - `config/config.json` に共通設定を記述
   - `config/mapping.json` にマッピング設定を記述
2. CSV を配置
   - `input/` フォルダへ任意名の CSV を配置（UTF-8/Shift_JIS/CP932 対応）
3. 変換を実行（以下のいずれか）
   - `python tools/clickpost_to_amazon.py`
   - `run-clickpost-to-amazon.bat`
   - ファイルを指定: `python tools/clickpost_to_amazon.py --input input/my_file.csv`

### 入出力

| 種別 | パス | 形式 | 説明 |
|------|------|------|------|
| 入力 | `input/*.csv` | 自動判定 | クリックポストの出力CSV |
| 出力 | `output/shipping_confirmation_YYYYMMDD_HHMMSS.txt` | CP932/タブ/全56列固定 | Amazon用出荷通知TXT |
| 出力（任意） | `output/shipping_confirmation_YYYYMMDD_HHMMSS.csv` | UTF-8/CSV | デバッグ・確認用（既定では無効） |

注記: CSV 出力を有効にするには `config/config.json` の `output.write_csv` を `true` にしてください。

## ブラウザ版（簡易）

### ビルド
1. HTML 生成
   - `python tools/build_web_index.py`
   - または `build-web-index.bat`
   - ルートに `index.html` が生成されます
2. 設定の埋め込み
   - `config/template_columns.json` を `TEMPLATE_COLUMNS` として埋め込み
   - `config/mapping.json` を `MAPCFG` として埋め込み

### 使い方
1. 生成された `index.html` をブラウザで開く
2. CSV をドラッグ&ドロップまたは「ファイルを選択」で読み込み（任意エンコード）
3. `shipping_confirmation_YYYYMMDD_HHMMSS.txt`（CP932/全56列固定）が自動ダウンロードされます

### エンコードに関する注意
- 正確な CP932 入出力のため、`vendor/encoding.min.js`（約 27KB）の配置が必要です（encoding-japanese を使用）。

## 設定ファイル概要

`config/config.json`（例）
```
{
  "io": { "encoding": "auto", "columns_path": "config/template_columns.json" },
  "format": { "input_date_format": "yyyy/MM/dd", "output_date_format": "yyyy-MM-dd" },
  "output": {
    "write_txt": true,
    "write_csv": false,
    "write_xlsx": false,
    "txt_name": "shipping_confirmation.txt",
    "csv_name": "shipping_confirmation.csv",
    "xlsx_name": "AmazonShippingConfirmation_output.xlsx"
  }
}
```

`config/mapping.json`（例：クリックポスト向け抜粋）
```
{
  "mappings": {
    "order-id":       { "source": "注文管理番号", "index": 0, "extract": "paren_inner" },
    "order-item-id":  { "source": "注文管理番号", "index": 0, "extract": "paren_before" },
    "quantity":       { "source": "数量", "index": 4, "extract": "after_multiply" },
    "ship-date":      { "source": "出荷日", "index": 2, "parse_date": true },
    "tracking-number":{ "source": "お問合せ番号", "index": 1 },
    "ship-method":    { "value": "クリックポスト" },
    "carrier-code":   { "value": "Japan Post" },
    "carrier-name":   { "value": "日本郵便" }
  }
}
```

抽出ルール（`extract`）
- `paren_inner`: 「xxxx(YYYY)」の YYYY 部分を抽出
- `paren_before`: 「xxxx(YYYY)」の xxxx 部分を抽出
- `after_multiply`: 「商品名×1」など末尾の乗算記号（×/x/*）の後ろの数字を抽出

## トラブルシューティング

- 文字化けする
  - Python版: `encoding: auto` で自動判定。うまくいかない場合は `cp932` などを明示
  - ブラウザ版: `vendor/encoding.min.js` が正しく配置されているか確認
- 日付がおかしい
  - `config/config.json` の `format` を確認（`yyyy/MM/dd` ↔ `yyyy-MM-dd`）
  - ブラウザ版は再ビルドして `index.html` を更新
- マッピングエラー
  - `template_columns.json` の `columns` と `mapping.json` のキー名が一致しているか確認

## プロジェクト構成
```
.
├── config/
│  ├── config.json
│  ├── mapping.json
│  └── template_columns.json
├── input/
│  └── *.csv
├── output/
│  └── shipping_confirmation_YYYYMMDD_HHMMSS.txt
├── tools/
│  ├── clickpost_to_amazon.py
│  └── build_web_index.py
├── vendor/
│  └── encoding.min.js
├── run-clickpost-to-amazon.bat
├── build-web-index.bat
└── index.html
```

