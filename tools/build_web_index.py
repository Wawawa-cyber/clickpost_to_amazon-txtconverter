import json
from pathlib import Path

TEMPLATE_PATH = Path("config/template_columns.json")
MAPPING_PATH = Path("config/mapping.json")
CONFIG_PATH = Path("config/config.json")
VENDOR_ENCODING_JS = Path("vendor/encoding.min.js")


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError:
        return json.loads(path.read_text(encoding="utf-8-sig"))


def main() -> None:
    print("=== ブラウザ版 HTML ビルドツール ===")
    print("index.html を生成します...")

    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"テンプレートが見つかりません: {TEMPLATE_PATH}")

    cols_raw = read_json(TEMPLATE_PATH)
    if isinstance(cols_raw, dict):
        columns = cols_raw.get("columns", [])
        header_rows = cols_raw.get("header_rows", [])
    else:
        columns = cols_raw
        header_rows = [columns]

    if not MAPPING_PATH.exists():
        raise FileNotFoundError(f"マッピングが見つかりません: {MAPPING_PATH}")
    mapping = read_json(MAPPING_PATH)

    config = {}
    if CONFIG_PATH.exists():
        config = read_json(CONFIG_PATH)

    encoding_js = ""
    if VENDOR_ENCODING_JS.exists():
        encoding_js = VENDOR_ENCODING_JS.read_text(encoding="utf-8")

    # JavaScriptコードを外部で構築
    js_code = f"""
function mapDate(val, inFmt, outFmt) {{
  const s = String(val || '').trim();
  if (!s) return '';
  if (inFmt === 'yyyyMMdd' && outFmt === 'yyyy-MM-dd') {{
    if (/^\\d{{8}}$/.test(s)) return s.slice(0,4)+'-'+s.slice(4,6)+'-'+s.slice(6,8);
  }}
  if (inFmt === 'yyyy/MM/dd' && outFmt === 'yyyy-MM-dd') {{
    if (/^\\d{{4}}\/\\d{{1,2}}\/\\d{{1,2}}$/.test(s)) {{
      const parts = s.split('/');
      const Y = parts[0];
      const M = parts[1].padStart(2,'0');
      const D = parts[2].padStart(2,'0');
      return `${{Y}}-${{M}}-${{D}}`;
    }}
  }}
  return s;
}}

function parseCSV(text) {{
  const lines = text.replace(/\\r\\n/g, '\\n').replace(/\\r/g, '\\n').split('\\n');
  while (lines.length && !lines[lines.length-1]) lines.pop();
  if (!lines.length) return [];
  const toCells = (line) => {{
    const cells = [];
    let cur = '';
    let q = false;
    for (let i=0;i<line.length;i++){{
      const ch = line[i];
      if (q){{
        if (ch === '"' && line[i+1] === '"'){{ cur += '"'; i++; }}
        else if (ch === '"'){{ q = false; }}
        else {{ cur += ch; }}
      }} else {{
        if (ch === ','){{ cells.push(cur); cur=''; }}
        else if (ch === '"'){{ q = true; }}
        else {{ cur += ch; }}
      }}
    }}
    cells.push(cur);
    return cells;
  }};
  const header = toCells(lines[0]);
  return lines.slice(1).map(line => {{
    const cells = toCells(line);
    const obj = {{ __cells__: cells }};
    header.forEach((h, i) => obj[h] = cells[i] ?? '');
    return obj;
  }});
}}

function extractValue(raw, mode) {{
  const s = String(raw || '').trim();
  if (!s) return '';
  if (mode === 'paren_inner' || mode === 'paren' || mode === 'inside_paren') {{
    const m = s.match(/[\(（]([^（）\)]+)[\)）]/);
    return m ? m[1].trim() : '';
  }}
  if (mode === 'paren_before' || mode === 'before_paren') {{
    const idx = s.indexOf('(') >= 0 ? s.indexOf('(') : s.indexOf('（');
    return idx >= 0 ? s.slice(0, idx).trim() : s;
  }}
  if (mode === 'after_multiply' || mode === 'after_times' || mode === 'qty_after_times') {{
    const marks = ['×','x','X','ｘ','Ｘ','*','＊'];
    let pos = -1;
    for (const m of marks) pos = Math.max(pos, s.lastIndexOf(m));
    if (pos >= 0 && pos + 1 < s.length) {{
      const tail = s.slice(pos + 1);
      const m2 = tail.match(/(\d+)/);
      return m2 ? m2[1] : tail.trim();
    }}
    const m3 = s.match(/(\d+)$/);
    return m3 ? m3[1] : '';
  }}
  return s;
}}

function transformRow(row, mapcfg){{
  const out = {{}};
  const inFmt = mapcfg.input_date_format || (CONFIG && CONFIG.format && CONFIG.format.input_date_format) || 'yyyyMMdd';
  const outFmt = mapcfg.output_date_format || (CONFIG && CONFIG.format && CONFIG.format.output_date_format) || 'yyyy-MM-dd';
  const mappings = mapcfg.mappings || {{}};
  for (const col of TEMPLATE_COLUMNS){{
    const rule = mappings[col];
    if (typeof rule === 'string') {{
      out[col] = row[rule] ?? '';
    }} else if (rule && typeof rule === 'object') {{
      if ('value' in rule) out[col] = rule.value;
      else if ('source' in rule || 'index' in rule){{
        let raw = '';
        if ('index' in rule) {{
          const idx = Number(rule.index);
          raw = Number.isInteger(idx) ? (row.__cells__ || [])[idx] || '' : '';
        }} else {{
          raw = row[rule.source] ?? '';
        }}
        let val = raw;
        if (typeof rule.extract === 'string') val = extractValue(val, rule.extract);
        out[col] = rule.parse_date ? mapDate(val, inFmt, outFmt) : val;
      }} else out[col] = '';
    }} else out[col] = '';
  }}
  return out;
}}

function toAmazonFormatTSV(columns, records, headerRows){{
  const TOTAL_COLUMNS = 256;
  const esc = (v)=>{{
    const s = v==null? '' : String(v);
    return s.replace(/\\t/g, ' ').replace(/\\r|\\n/g, ' ');
  }};
  const lines = [];
  if (Array.isArray(headerRows)){{
    for (const hr of headerRows){{
      if (Array.isArray(hr)) {{
        const line = hr.map(esc);
        while (line.length < TOTAL_COLUMNS) line.push('');
        lines.push(line.join('\\t'));
      }}
    }}
  }}
  const headerLine = columns.map(esc);
  while (headerLine.length < TOTAL_COLUMNS) headerLine.push('');
  lines.push(headerLine.join('\\t'));
  for (const r of records) {{
    const line = columns.map(c=>esc(r[c]));
    while (line.length < TOTAL_COLUMNS) line.push('');
    lines.push(line.join('\\t'));
  }}
  lines.push(''); // final empty line to match sample
  return lines.join('\\r\\n');
}}

async function readAsArrayBuffer(file){{
  return new Promise((res, rej)=>{{ const fr=new FileReader(); fr.onerror = ()=>rej(fr.error); fr.onload=()=>res(fr.result); fr.readAsArrayBuffer(file); }});
}}

function decodeCSV(ab){{
  const bytes = new Uint8Array(ab);
  
  // Try encoding.js first for Shift_JIS → Unicode
  if (typeof Encoding !== 'undefined') {{
    try {{
      const unicodeArray = Encoding.convert(bytes, 'UNICODE', 'SJIS');
      return Encoding.codeToString(unicodeArray);
    }} catch (_) {{}}
  }}
  
  // Try browser's TextDecoder with various encodings
  const encodings = ['shift_jis', 'shift-jis', 'sjis', 'cp932', 'windows-31j', 'utf-8', 'utf-16'];
  
  for (const encoding of encodings) {{
    try {{
      const text = new TextDecoder(encoding).decode(bytes);
      // Basic validation: check if the decoded text contains reasonable characters
      if (text && text.length > 0 && !/[\\uFFFD\\u0000-\\u0008\\u000E-\\u001F]/.test(text.slice(0, 100))) {{
        return text;
      }}
    }} catch (_) {{}}
  }}
  
  // Fallback to UTF-8
  try {{
    return new TextDecoder('utf-8').decode(bytes);
  }} catch (_) {{
    return '';
  }}
}}

function encodeANSI(str){{
  // 必ずShift_JIS（CP932）で出力する
  if (typeof Encoding !== 'undefined') {{
    try {{
      const unicodeCodes = Encoding.stringToCode(str);
      const sjisCodes = Encoding.convert(unicodeCodes, 'SJIS', 'UNICODE');
      console.log('Shift_JIS encoding successful:', sjisCodes.length, 'bytes');
      return {{ bytes: new Uint8Array(sjisCodes), exact: true }};
    }} catch (err) {{
      console.error('Encoding.js failed:', err);
      throw new Error('Shift_JISエンコーディングに失敗しました: ' + err.message);
    }}
  }}
  
  // encoding.jsが利用できない場合はエラー
  throw new Error('encoding.jsライブラリが読み込まれていません。Shift_JISエンコーディングができません。');
}}

(function(){{
  const drop = document.getElementById('drop');
  const msg = document.getElementById('msg');
  const fileInput = document.getElementById('file');
  function setMsg(t, isErr){{ msg.textContent = t; msg.className = 'row small' + (isErr? ' error':'' ); }}

  // ライブラリの読み込み状況をチェック（少し待ってから）
  setTimeout(function() {{
    console.log('Main script - Encoding library check:', typeof Encoding !== 'undefined' ? 'AVAILABLE' : 'NOT AVAILABLE');
    
    if (typeof Encoding === 'undefined') {{
      console.error('encoding.js library is not loaded. Shift_JIS encoding will not work.');
      setMsg('エラー: encoding.jsライブラリが読み込まれていません。ブラウザのコンソールを確認してください。', true);
    }} else {{
      console.log('encoding.js library loaded successfully');
      console.log('Encoding.convert function:', typeof Encoding.convert);
      console.log('Encoding.stringToCode function:', typeof Encoding.stringToCode);
      setMsg('encoding.jsライブラリが正常に読み込まれました。');
      
      // テスト変換を実行
      try {{
        const testStr = 'テスト';
        const unicodeCodes = Encoding.stringToCode(testStr);
        const sjisCodes = Encoding.convert(unicodeCodes, 'SJIS', 'UNICODE');
        console.log('Encoding test successful - SJIS bytes:', sjisCodes.length);
      }} catch (err) {{
        console.error('Encoding test failed:', err);
        setMsg('エラー: encoding.jsライブラリの動作テストに失敗しました。', true);
      }}
    }}
  }}, 100);

  // Prevent default drag behaviors on window to allow drop zone functionality
  window.addEventListener('dragover', (e) => {{ e.preventDefault(); }});
  window.addEventListener('drop', (e) => {{ e.preventDefault(); }});

  async function handleFile(file){{
    try {{
      if (!file) {{ setMsg('ファイルが選択されていません', true); return; }}
      
      // ファイル形式のチェック
      const fileName = file.name.toLowerCase();
      const fileType = file.type.toLowerCase();
      if (!fileName.endsWith('.csv') && !fileType.includes('csv') && !fileType.includes('text')) {{
        setMsg('CSVファイルを選択してください。', true);
        return;
      }}
      
      setMsg('読み込み中: ' + file.name);
      const ab = await readAsArrayBuffer(file);
      const text = decodeCSV(ab);
      const data = parseCSV(text);
      if (data.length === 0) {{ setMsg('CSVデータが見つかりませんでした。ファイル内容を確認してください。', true); return; }}
      const transformed = data.map(r => transformRow(r, MAPCFG || {{}}));
      const amazonTsv = toAmazonFormatTSV(TEMPLATE_COLUMNS, transformed, HEADER_ROWS);
      
      // Shift_JISエンコーディングを強制実行
      const enc = encodeANSI(amazonTsv);

      // ファイル名は Python 版と同じタイムスタンプ形式
      const now = new Date();
      const ts = now.getFullYear()
        + String(now.getMonth() + 1).padStart(2, '0')
        + String(now.getDate()).padStart(2, '0') + '_' +
        String(now.getHours()).padStart(2, '0') +
        String(now.getMinutes()).padStart(2, '0') +
        String(now.getSeconds()).padStart(2, '0');
      const baseName = (CONFIG && CONFIG.output && CONFIG.output.txt_name) || 'shipping_confirmation.txt';
      const nameParts = baseName.split('.');
      const filename = nameParts.length === 2 ? `${{nameParts[0]}}_${{ts}}.${{nameParts[1]}}` : `${{baseName}}_${{ts}}`;

      // Shift_JISエンコードされたバイト配列でBlobを作成
      console.log('Creating Shift_JIS file with', enc.bytes.length, 'bytes');
      const blob = new Blob([enc.bytes], {{ 
        type: 'application/octet-stream'  // バイナリデータとして扱う
      }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url; 
      a.download = filename;
      a.style.display = 'none';
      document.body.appendChild(a); 
      a.click();
      setTimeout(()=>{{ 
        URL.revokeObjectURL(url); 
        document.body.removeChild(a); 
      }}, 100);
      setMsg(`変換完了（Shift_JIS・${{enc.bytes.length}}バイト）: ${{filename}}`);
    }} catch (err){{ console.error(err); setMsg('エラー: ' + (err && err.message ? err.message : String(err)), true); }}
  }}

  drop.addEventListener('dragenter', (e) => {{ 
    e.preventDefault(); 
    e.stopPropagation(); 
    drop.classList.add('ok'); 
  }});
  drop.addEventListener('dragover', (e) => {{ 
    e.preventDefault(); 
    e.stopPropagation(); 
    e.dataTransfer.dropEffect = 'copy'; 
  }});
  drop.addEventListener('dragleave', (e) => {{ 
    e.preventDefault(); 
    e.stopPropagation(); 
    // Only remove 'ok' class if we're leaving the drop zone itself, not child elements
    if (!drop.contains(e.relatedTarget)) {{
      drop.classList.remove('ok'); 
    }}
  }});
  drop.addEventListener('drop', (e) => {{ 
    e.preventDefault(); 
    e.stopPropagation(); 
    drop.classList.remove('ok'); 
    const files = e.dataTransfer && e.dataTransfer.files; 
    if (files && files.length > 0) {{
      handleFile(files[0]);
    }}
  }});
  drop.addEventListener('click', () => fileInput.click());
  fileInput.addEventListener('change', () => handleFile(fileInput.files && fileInput.files[0]));
}})();
"""

    html = f'''<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Amazon 出荷通知 変換ツール (ブラウザ版)</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif; margin: 24px; }}
    .drop {{ border: 2px dashed #888; padding: 32px; text-align: center; border-radius: 8px; color: #555; transition: all 0.3s ease; cursor: pointer; }}
    .drop:hover {{ border-color: #007cba; background-color: #f8f9fa; }}
    .ok {{ border-color: #2c7; color: #2c7; }}
    .row {{ margin: 16px 0; }}
    .small {{ color: #666; font-size: 12px; }}
    .error {{ color: #c22; }}
    input[type=file] {{ display: none; }}
    .btn {{ display: inline-block; padding: 8px 14px; background: #0366d6; color: #fff; border-radius: 6px; cursor: pointer; text-decoration: none; }}
  </style>
  <script>
  const TEMPLATE_COLUMNS = {json.dumps(columns, ensure_ascii=False)};
  const HEADER_ROWS = {json.dumps(header_rows, ensure_ascii=False)};
  const MAPCFG = {json.dumps(mapping, ensure_ascii=False)};
  const CONFIG = {json.dumps(config, ensure_ascii=False)};
  </script>
  <!-- Load encoding.js library -->
  <script src="vendor/encoding.min.js" onerror="console.error('Failed to load vendor/encoding.min.js')"></script>
  <!-- Inline fallback (works when opened via file://) -->
  <script>{encoding_js}</script>
  <!-- Check if Encoding is available after all scripts loaded -->
  <script>
  // 初期チェック
  console.log('Initial Encoding library check:', typeof Encoding !== 'undefined' ? 'LOADED' : 'NOT LOADED');
  if (typeof Encoding !== 'undefined') {{
    console.log('Encoding object methods:', Object.keys(Encoding));
  }}
  
  // DOMContentLoaded後にも再チェック
  document.addEventListener('DOMContentLoaded', function() {{
    console.log('DOMContentLoaded - Encoding library check:', typeof Encoding !== 'undefined' ? 'LOADED' : 'NOT LOADED');
    if (typeof Encoding !== 'undefined') {{
      console.log('Encoding available methods:', Object.keys(Encoding));
      console.log('Test encoding conversion available:', typeof Encoding.convert === 'function');
    }} else {{
      console.error('Encoding library failed to load. Check console for errors.');
    }}
  }});
  </script>
</head>
<body>
  <h1>Amazon 出荷通知 変換ツール (ブラウザ版)</h1>
  <p>CSV をドロップまたは選択すると、Amazon 形式 (CP932/Shift_JIS・256列固定・タブ区切り・CRLF) の TXT をダウンロードします。</p>

  <div id="drop" class="drop">ここに CSV をドロップ、またはクリックして選択</div>
  <div class="row"><label class="btn" for="file">ファイルを選択</label> <input id="file" type="file" accept=".csv,text/csv"></div>
  <div id="msg" class="row small"></div>

<script>{js_code}</script>
</body>
</html>
'''

    Path("index.html").write_text(html, encoding="utf-8")
    print("[ok] 生成完了: index.html")
    print(f"[ok] 列数: {len(columns)} / ヘッダ行: {len(header_rows)}")


if __name__ == "__main__":
    main()
