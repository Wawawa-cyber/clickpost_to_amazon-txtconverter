 # 設定ファイルガイド
 
 このディレクトリには、ツールの動作を制御する設定ファイルが含まれます。
 
 ## ファイル一覧
 
 | ファイル | 説明 | 形式 | 必須 |
 |---------|------|------|------|
 | `config.json` | 共通設定（入出力・形式・出力制御） | UTF-8 | 必須 |
 | `mapping.json` | 列マッピング設定 | UTF-8 | 必須 |
 | `template_columns.json` | Amazonテンプレート情報（ヘッダー行と列順） | UTF-8 | 必須 |
 
 ---
 
 ## config.json
 
 ツール全体の共通設定を管理します。
 
 ### 設定例
 
 ```json
 {
   "io": {
     "encoding": "auto",
     "columns_path": "config/template_columns.json"
   },
   "format": {
     "input_date_format": "yyyy/MM/dd",
     "output_date_format": "yyyy-MM-dd"
   },
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
 
 ### 設定詳細
 
 - `io.encoding`: 入力CSVのエンコード指定。`auto`/`cp932`/`utf-8` など。
 - `io.columns_path`: テンプレート列定義のパス（`template_columns.json`）。
 - `format.input_date_format`: 入力日付の書式（例: `yyyy/MM/dd`）。
 - `format.output_date_format`: 出力日付の書式（例: `yyyy-MM-dd`）。
 - `output.write_txt`: TXT出力（タブ/CP932/56列固定）を有効化。
 - `output.write_csv`: CSV出力（UTF-8、検証用）を有効化。
 - `output.write_xlsx`: XLSX出力は非推奨（Excelテンプレート未使用）。
 - `txt_name`/`csv_name`/`xlsx_name`: 出力ファイル名（タイムスタンプ付与）。
 
 ---
 
 ## mapping.json
 
 入力CSVの列を Amazon テンプレート列に対応付ける設定です。`encoding` や日付形式を上書き指定することもできます（`config.json`より優先）。
 
 ### 基本構造
 
 ```json
 {
   "encoding": "cp932",
   "input_date_format": "yyyyMMdd",
   "output_date_format": "yyyy-MM-dd",
   "mappings": {
     "Amazon列名": { "source": "入力CSV列名" }
   }
 }
 ```
 
 備考: `mappings` キーを省略し、最上位をマッピング辞書として書くことも可能です。
 
 ### マッピング方法
 
 - 列名で指定: `{ "source": "注文明細" }`
 - 列インデックスで指定: `{ "index": 0 }`（0始まり）
 - 固定値: `{ "value": "日本郵便" }`
 - 日付変換: `{ "source": "出荷日", "parse_date": true }`
 - 追加抽出: `{ "source": "商品名×1", "extract": "after_multiply" }`
 
 サポートする `extract` 値
 - `paren_inner`（`inside_paren`/`paren` 同義）: 「xxxx(YYYY)」の YYYY を抽出
 - `paren_before`（`before_paren` 同義）: 「xxxx(YYYY)」の xxxx を抽出
 - `after_multiply`（`after_times`/`qty_after_times` 同義）: 末尾の乗算記号（×/x/X/*/＊）の後の数字を抽出
 
 ### 設定例（抜粋）
 
 ```json
 {
   "mappings": {
     "order-id":       { "source": "注文管理番号", "index": 0, "extract": "paren_inner" },
     "order-item-id":  { "source": "注文管理番号", "index": 0, "extract": "paren_before" },
     "quantity":       { "source": "数量", "index": 4, "extract": "after_multiply" },
     "ship-date":      { "source": "出荷日", "parse_date": true },
     "tracking-number":{ "source": "お問合せ番号" },
     "ship-method":    { "value": "クリックポスト" },
     "carrier-code":   { "value": "Japan Post" },
     "carrier-name":   { "value": "日本郵便" }
   }
 }
 ```
 
 ### 注意事項
 
 - マッピング対象の Amazon 列名は `template_columns.json` の `columns` に一致させてください。
 - 本ファイルは UTF-8 で保存してください。
 - ここで指定した `encoding`/日付形式は `config.json` より優先されます。
 
 ---
 
 ## template_columns.json
 
 Amazon テンプレートのヘッダー行と列順を定義します。
 
 ### 構造
 
 ```json
 {
   "header_rows": [
     ["TemplateType=OrderFulfillment", "Version=2011.1102", "注意文..."],
     ["注文番号", "注文商品番号", "出荷数", "..."]
   ],
   "columns": [
     "order-id",
     "order-item-id",
     "quantity",
     "ship-date",
     "..."
   ]
 }
 ```
 
 ### 設定詳細
 
 - `header_rows`: 出力ファイルの先頭にそのまま書き出すヘッダー行。
 - `columns`: データ行で出力する列名（順序を保持）。`mapping.json` のマッピング対象。
 
 ---
 
 ## 設定の優先順位
 
 | 優先度 | ファイル | 説明 |
 |-------|---------|------|
 | 高    | `mapping.json` | 個別のマッピング・上書き設定 |
 | 中    | `config.json`  | 共通設定 |
 | 低    | スクリプト既定 | ツール内のデフォルト値 |
 
 ---
 
 ## トラブルシューティング
 
 - JSON 形式エラー: 構文ミス。`python -m json.tool` で検証。
 - 列名不一致: `mapping.json` のキーが `template_columns.json` の `columns` に無い。
 - エンコード不一致: 入力と `encoding` が合わない。`auto` か適切な値に変更。
 - 日付変換エラー: `input_date_format` と `output_date_format` を見直し。
 
 ヒント: 動作確認はメインの `README.md` の手順を参照してください。

