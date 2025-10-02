# クリックポスト → Amazon 出荷通知 変換ツール

クリックポストの出荷通知CSVファイルを、Amazonの「出荷通知アップロード」用フォーマット（CP932、タブ区切り、256列固定）に変換するツールです。
Excel繝・Φ繝励Ξ繝ｼ繝医・菴ｿ繧上★縲√ユ繝ｳ繝励Ξ繝ｼ繝医・1陦檎岼・域ｳｨ諢乗枚・峨→2陦檎岼・医・繝・ム繝ｼ・峨ｒJSON縺ｫ菫晄戟縺励※蜃ｺ蜉帙∈蜿肴丐縺励∪縺吶・
## 搭 逶ｮ谺｡

- [蠢・ｦ√↑繝輔ぃ繧､繝ｫ](#-蠢・ｦ√↑繝輔ぃ繧､繝ｫ)
- [Python迚茨ｼ域耳螂ｨ・云(#-python迚域耳螂ｨ)
- [繝悶Λ繧ｦ繧ｶ迚茨ｼ育ｰ｡譏難ｼ云(#-繝悶Λ繧ｦ繧ｶ迚育ｰ｡譏・
- [險ｭ螳壹ヵ繧｡繧､繝ｫ](#・・險ｭ螳壹ヵ繧｡繧､繝ｫ)
- [繝医Λ繝悶Ν繧ｷ繝･繝ｼ繝・ぅ繝ｳ繧ｰ](#-繝医Λ繝悶Ν繧ｷ繝･繝ｼ繝・ぅ繝ｳ繧ｰ)

## 刀 蠢・ｦ√↑繝輔ぃ繧､繝ｫ

| 繝輔ぃ繧､繝ｫ | 隱ｬ譏・|
|---------|------|
| `input/*.csv` | 繧・≧繝励ΜR縺ｮ蜃ｺ蜉帙ヵ繧｡繧､繝ｫ・井ｻｻ諢上・蜷榊燕縲√お繝ｳ繧ｳ繝ｼ繝芽・蜍墓､懷・・・|
| `config/template_columns.json` | Amazon繝・Φ繝励Ξ繝ｼ繝医・繝倥ャ繝繝ｼ諠・ｱ・・SON蠖｢蠑擾ｼ・|
| `config/mapping.json` | 蛻励・繝槭ャ繝斐Φ繧ｰ險ｭ螳夲ｼ・TF-8縲～sample/mapping_prompt.txt`繧貞盾閠・ｼ・|
| `config/config.json` | 蜈･蜃ｺ蜉帙・蠖｢蠑上・蜃ｺ蜉帙・蜷・ｨｭ螳・|

## 錐 Python迚茨ｼ域耳螂ｨ・・
### 肌 蠢・ｦ√↑迺ｰ蠅・- Python 3.6 莉･荳・- 蠢・ｦ√↑繝ｩ繧､繝悶Λ繝ｪ・壽ｨ呎ｺ悶Λ繧､繝悶Λ繝ｪ縺ｮ縺ｿ・郁ｿｽ蜉繧､繝ｳ繧ｹ繝医・繝ｫ荳崎ｦ・ｼ・
### 噫 螳溯｡梧婿豕・
1. **險ｭ螳壹ヵ繧｡繧､繝ｫ縺ｮ貅門ｙ**
   ```bash
   # config/config.json 縺ｫ蜈ｱ騾夊ｨｭ螳壹ｒ險倩ｼ・   # config/mapping.json 縺ｫ繝槭ャ繝斐Φ繧ｰ險ｭ螳壹ｒ險倩ｼ・   ```

2. **CSV繝輔ぃ繧､繝ｫ縺ｮ驟咲ｽｮ**
   ```bash
   # input繝輔か繝ｫ繝縺ｫ莉ｻ諢上・蜷榊燕縺ｮCSV繝輔ぃ繧､繝ｫ繧帝・鄂ｮ
   # 繧ｨ繝ｳ繧ｳ繝ｼ繝峨・閾ｪ蜍墓､懷・・・TF-8縲ヾhift_JIS縲，P932蟇ｾ蠢懶ｼ・   input/amazon逕ｨ蜃ｺ闕ｷ騾夂衍.csv  # 萓・   ```

3. **螟画鋤縺ｮ螳溯｡・*・井ｻ･荳九・縺・★繧後°・・   ```bash
   # Python逶ｴ謗･螳溯｡鯉ｼ郁・蜍慕噪縺ｫinput繝輔か繝ｫ繝縺ｮCSV繧呈､懷・・・   python tools/clickpost_to_amazon.py
   
   # 繝舌ャ繝√ヵ繧｡繧､繝ｫ螳溯｡・   run-clickpost-to-amazon.bat
   
   # 迚ｹ螳壹ヵ繧｡繧､繝ｫ繧呈欠螳壹☆繧句ｴ蜷・   python tools/clickpost_to_amazon.py --input input/my_file.csv
   ```

### 豆 蜈･蜃ｺ蜉帙ヵ繧｡繧､繝ｫ

| 遞ｮ鬘・| 繝代せ | 蠖｢蠑・| 隱ｬ譏・|
|------|------|------|------|
| 蜈･蜉・| `input/*.csv` | 繧ｨ繝ｳ繧ｳ繝ｼ繝芽・蜍墓､懷・ | 繧・≧繝励ΜR縺ｮ蜃ｺ蜉帙ヵ繧｡繧､繝ｫ・井ｻｻ諢上・蜷榊燕・・|
| 蜃ｺ蜉・| `output/shipping_confirmation_YYYYMMDD_HHMMSS.txt` | CP932縲√ち繝門玄蛻・ｊ縲・56蛻怜崋螳壼ｹ・| Amazon逕ｨ蜃ｺ闕ｷ騾夂衍繝輔ぃ繧､繝ｫ |
| 蜃ｺ蜉幢ｼ医が繝励す繝ｧ繝ｳ・・| `output/shipping_confirmation_YYYYMMDD_HHMMSS.csv` | UTF-8縲，SV | 繝・ヰ繝・げ逕ｨ・域里螳壹〒辟｡蜉ｹ・・|

> **豕ｨ諢・*: CSV蜃ｺ蜉帙ｒ譛牙柑縺ｫ縺吶ｋ縺ｫ縺ｯ `config/config.json` 縺ｮ `output.write_csv` 繧・`true` 縺ｫ險ｭ螳壹＠縺ｦ縺上□縺輔＞縲・
## 倹 繝悶Λ繧ｦ繧ｶ迚茨ｼ育ｰ｡譏難ｼ・
### 畑 繝薙Ν繝画焔鬆・
1. **HTML繝輔ぃ繧､繝ｫ縺ｮ逕滓・**
   ```bash
   # Python螳溯｡・   python tools/build_web_index.py
   
   # 縺ｾ縺溘・繝舌ャ繝√ヵ繧｡繧､繝ｫ螳溯｡・   build-web-index.bat
   ```
   竊・繝ｫ繝ｼ繝医ョ繧｣繝ｬ繧ｯ繝医Μ縺ｫ `index.html` 縺檎函謌舌＆繧後∪縺・
2. **險ｭ螳壹・蝓九ａ霎ｼ縺ｿ**
   - `config/template_columns.json` 竊・`TEMPLATE_COLUMNS`縺ｨ縺励※蝓九ａ霎ｼ縺ｿ
   - `config/mapping.json` 竊・`MAPCFG`縺ｨ縺励※蝓九ａ霎ｼ縺ｿ

### 捗 菴ｿ逕ｨ譁ｹ豕・
1. 逕滓・縺輔ｌ縺・`index.html` 繧偵ヶ繝ｩ繧ｦ繧ｶ縺ｧ髢九￥
2. CSV繝輔ぃ繧､繝ｫ・井ｻｻ諢上・繧ｨ繝ｳ繧ｳ繝ｼ繝会ｼ峨ｒ繧｢繝・・繝ｭ繝ｼ繝・   - 繝峨Λ繝・げ・・ラ繝ｭ繝・・
   - 縲後ヵ繧｡繧､繝ｫ繧帝∈謚槭阪・繧ｿ繝ｳ
3. `shipping_confirmation_YYYYMMDD_HHMMSS.txt`・・P932縲・56蛻怜崋螳壼ｹ・ｼ峨′閾ｪ蜍輔ム繧ｦ繝ｳ繝ｭ繝ｼ繝蛾幕蟋・
### 笞呻ｸ・繧ｨ繝ｳ繧ｳ繝ｼ繝芽ｨｭ螳・
**櫨 驥崎ｦ・*: 豁｣遒ｺ縺ｪCP932蜈･蜃ｺ蜉帙・縺溘ａ縲∽ｻ･荳九・繝ｩ繧､繝悶Λ繝ｪ縺悟ｿ・ｦ√〒縺呻ｼ・
```
vendor/
笏披楳笏 encoding.min.js  # 蠢・茨ｼ育ｴ・27KB・・```

**繝ｩ繧､繝悶Λ繝ｪ**: [encoding-japanese](https://github.com/polygonplanet/encoding.js)

**笞・・豕ｨ諢・*: 
- 繝輔ぃ繧､繝ｫ繧ｵ繧､繧ｺ縺檎ｴ・9KB縺ｮ蝣ｴ蜷医・荳榊ｮ悟・迚医〒縺・- 荳榊ｮ悟・迚医〒縺ｯ`Uncaught SyntaxError`繧ｨ繝ｩ繝ｼ縺檎匱逕溘＠縺ｾ縺・- 蠢・★蜈ｬ蠑上Μ繝昴ず繝医Μ縺九ｉ螳悟・迚茨ｼ育ｴ・27KB・峨ｒ繝繧ｦ繝ｳ繝ｭ繝ｼ繝峨＠縺ｦ縺上□縺輔＞

**遒ｺ隱肴婿豕・*:
```bash
ls -la vendor/encoding.min.js
# 譛溷ｾ・､: 邏・27,869 bytes
# 逡ｰ蟶ｸ蛟､: 邏・9,519 bytes・医％縺ｮ蝣ｴ蜷医・蜀阪ム繧ｦ繝ｳ繝ｭ繝ｼ繝牙ｿ・ｦ・ｼ・```

> **繝輔か繝ｼ繝ｫ繝舌ャ繧ｯ**: 繝ｩ繧､繝悶Λ繝ｪ縺梧悴驟咲ｽｮ縺ｮ蝣ｴ蜷医～TextDecoder`/`TextEncoder`縺ｫ繧医ｋ蜃ｦ逅・→縺ｪ繧翫∫腸蠅・↓繧医▲縺ｦ縺ｯUTF-8蜃ｺ蜉帙→縺ｪ繧翫∪縺吶ょ宍蟇・↓CP932縺悟ｿ・ｦ√↑蝣ｴ蜷医・Python迚医ｒ縺泌茜逕ｨ縺上□縺輔＞縲・
## 笞呻ｸ・險ｭ螳壹ヵ繧｡繧､繝ｫ

### 統 繝槭ャ繝斐Φ繧ｰ險ｭ螳壹・菴懈・

1. **蜿り・ヵ繧｡繧､繝ｫ**: `sample/mapping_prompt.txt`縺ｫJSON繧ｹ繧ｱ繝ｫ繝医Φ縺ｨ豕ｨ諢丈ｺ矩・ｒ險倩ｼ・2. **菴懈・謇矩・*: 
   - UTF-8縺ｧ`config/mapping.json`繧剃ｽ懈・
   - 繧・≧繝励ΜR縺ｮCSV蛻怜錐縺ｫ蜷医ｏ縺帙※繝槭ャ繝斐Φ繧ｰ繧定ｨｭ螳・
**笞・・驥崎ｦ・*: 繝倥ャ繝繝ｼ蜷阪・`config/template_columns.json`縺ｮ`columns`縺ｨ螳悟・荳閾ｴ縺輔○繧句ｿ・ｦ√′縺ゅｊ縺ｾ縺吶・
### 売 險ｭ螳壹・蜆ｪ蜈磯・ｽ・
| 蜆ｪ蜈亥ｺｦ | 險ｭ螳壹ヵ繧｡繧､繝ｫ | 蜀・ｮｹ |
|--------|-------------|------|
| 1・磯ｫ假ｼ・| `config/mapping.json` | 繧ｨ繝ｳ繧ｳ繝ｼ繝・ぅ繝ｳ繧ｰ縲∵律莉倥ヵ繧ｩ繝ｼ繝槭ャ繝育ｭ峨・蛟句挨險ｭ螳・|
| 2・井ｸｭ・・| `config/config.json` | 蜈ｱ騾夊ｨｭ螳・|
| 3・井ｽ趣ｼ・| 繧ｹ繧ｯ繝ｪ繝励ヨ蜀・ョ繝輔か繝ｫ繝亥､ | 譛ｪ謖・ｮ夐・岼縺ｮ繝輔か繝ｼ繝ｫ繝舌ャ繧ｯ蛟､ |

### 搭 險ｭ螳壻ｾ・
**config/config.json**:
```json
{
  "io": {
    "encoding": "auto",
    "columns_path": "config/template_columns.json"
  },
  "format": {
    "input_date_format": "yyyyMMdd",
    "output_date_format": "yyyy-MM-dd"  
  },
  "output": {
    "write_txt": true,
    "write_csv": false,
    "txt_name": "shipping_confirmation.txt"
  }
}
```

## 肌 繝医Λ繝悶Ν繧ｷ繝･繝ｼ繝・ぅ繝ｳ繧ｰ

### 笶・驥崎ｦ・ encoding.js 繝ｩ繧､繝悶Λ繝ｪ繧ｨ繝ｩ繝ｼ

**逞・憾**: 繝悶Λ繧ｦ繧ｶ迚医〒縲憩ncoding.js繝ｩ繧､繝悶Λ繝ｪ縺瑚ｪｭ縺ｿ霎ｼ縺ｾ繧後※縺・∪縺帙ｓ縲阪お繝ｩ繝ｼ縺檎匱逕・```
Uncaught SyntaxError: Unexpected token ':'
encoding.js library is not loaded. Shift_JIS encoding will not work.
```

**蜴溷屏**: `vendor/encoding.min.js`繝輔ぃ繧､繝ｫ縺御ｸ榊ｮ悟・・育ｴ・9KB・・
**隗｣豎ｺ譁ｹ豕・*:
1. 螳悟・迚医Λ繧､繝悶Λ繝ｪ繧偵ム繧ｦ繝ｳ繝ｭ繝ｼ繝・
   ```bash
   cd vendor/
   curl -L "https://raw.githubusercontent.com/polygonplanet/encoding.js/master/encoding.min.js" -o encoding.min.js
   ```
2. 繝輔ぃ繧､繝ｫ繧ｵ繧､繧ｺ繧堤｢ｺ隱搾ｼ育ｴ・27KB縺梧ｭ｣蟶ｸ・・
   ```bash
   ls -la vendor/encoding.min.js
   ```
3. HTML繧貞・繝薙Ν繝・
   ```bash
   python tools/build_web_index.py
   ```

> **隧ｳ邏ｰ**: `sample/encoding-js-error-fix/`繝輔か繝ｫ繝縺ｫ螳悟・縺ｪ隗｣豎ｺ謇矩・ｒ險倬鹸

### 繧医￥縺ゅｋ蝠城｡後→隗｣豎ｺ遲・
| 蝠城｡・| 蜴溷屏 | 隗｣豎ｺ遲・|
|------|------|--------|
| **encoding.js繧ｨ繝ｩ繝ｼ** | **荳榊ｮ悟・縺ｪ繝ｩ繧､繝悶Λ繝ｪ繝輔ぃ繧､繝ｫ・・9KB・・* | **螳悟・迚茨ｼ・27KB・峨ｒ繝繧ｦ繝ｳ繝ｭ繝ｼ繝牙ｾ後∝・繝薙Ν繝・* |
| 繧ｨ繝ｳ繧ｳ繝ｼ繝峨お繝ｩ繝ｼ | 繧ｨ繝ｳ繧ｳ繝ｼ繝画､懷・螟ｱ謨・| `config/config.json`縺ｮ`encoding`繧蛋"auto"`縺ｾ縺溘・蜈ｷ菴鍋噪縺ｪ蛟､縺ｫ險ｭ螳・|
| 繝槭ャ繝斐Φ繧ｰ繧ｨ繝ｩ繝ｼ | 蛻怜錐縺ｮ荳堺ｸ閾ｴ | `config/template_columns.json`縺ｨ`mapping.json`縺ｮ蛻怜錐繧堤｢ｺ隱・|
| 譌･莉倥ヵ繧ｩ繝ｼ繝槭ャ繝医お繝ｩ繝ｼ | 譌･莉伜ｽ｢蠑上・荳堺ｸ閾ｴ | `input_date_format`縺ｨ`output_date_format`繧堤｢ｺ隱・|
| CSV繝輔ぃ繧､繝ｫ縺瑚ｦ九▽縺九ｉ縺ｪ縺・| input繝輔か繝ｫ繝縺ｫCSV繝輔ぃ繧､繝ｫ縺後↑縺・| `input/`繝輔か繝ｫ繝縺ｫCSV繝輔ぃ繧､繝ｫ繧帝・鄂ｮ |
| Amazon縺ｧ繧ｨ繝ｩ繝ｼ | 繝輔か繝ｼ繝槭ャ繝井ｸ堺ｸ閾ｴ | 蜃ｺ蜉帙ヵ繧｡繧､繝ｫ縺靴P932縲・56蛻怜崋螳壼ｹ・↓縺ｪ縺｣縺ｦ縺・ｋ縺九ｒ遒ｺ隱・|

### 繝・ヰ繝・げ縺ｮ繝偵Φ繝・
1. **CSV蜃ｺ蜉帙ｒ譛牙柑蛹・*: `output.write_csv: true`縺ｧ荳ｭ髢鍋ｵ先棡繧堤｢ｺ隱・2. **Python螳溯｡・*: 繝舌ャ繝√ヵ繧｡繧､繝ｫ縺ｧ縺ｪ縺襲ython逶ｴ謗･螳溯｡後〒繧ｨ繝ｩ繝ｼ隧ｳ邏ｰ繧堤｢ｺ隱・3. **繧ｨ繝ｳ繧ｳ繝ｼ繝臥｢ｺ隱・*: 繧ｨ繝ｳ繧ｳ繝ｼ繝芽・蜍墓､懷・縺ｮ邨先棡繧偵さ繝ｳ繧ｽ繝ｼ繝ｫ蜃ｺ蜉帙〒遒ｺ隱・4. **繝輔か繝ｼ繝槭ャ繝育｢ｺ隱・*: 蜃ｺ蜉帙ヵ繧｡繧､繝ｫ縺・56蛻励・蝗ｺ螳壼ｹ・↓縺ｪ縺｣縺ｦ縺・ｋ縺九ｒ遒ｺ隱・
### ・ 繧ｵ繝昴・繝・
- **險ｭ螳壻ｾ・*: `sample/`繝・ぅ繝ｬ繧ｯ繝医Μ蜀・・繝輔ぃ繧､繝ｫ繧貞盾辣ｧ
- **繝槭ャ繝斐Φ繧ｰ菴懈・**: `sample/mapping_prompt.txt`縺ｮ謇矩・↓蠕薙≧

---

## 唐 繝励Ο繧ｸ繧ｧ繧ｯ繝域ｧ区・

```
.
笏懌楳笏 config/
笏・  笏懌楳笏 config.json              # 蜈ｱ騾夊ｨｭ螳・笏・  笏懌楳笏 mapping.json             # 蛻励・繝・ヴ繝ｳ繧ｰ險ｭ螳・笏・  笏披楳笏 template_columns.json    # Amazon繝・Φ繝励Ξ繝ｼ繝域ュ蝣ｱ
笏懌楳笏 input/
笏・  笏披楳笏 *.csv                    # 蜈･蜉帙ヵ繧｡繧､繝ｫ・井ｻｻ諢上・蜷榊燕縲√お繝ｳ繧ｳ繝ｼ繝芽・蜍墓､懷・・・笏懌楳笏 output/
笏・  笏披楳笏 shipping_confirmation_YYYYMMDD_HHMMSS.txt # 蜃ｺ蜉帙ヵ繧｡繧､繝ｫ・・mazon蠖｢蠑上，P932・・笏・笏懌楳笏 tools/
笏・  笏懌楳笏 clickpost_to_amazon.py     # 繝｡繧､繝ｳ螟画鋤繧ｹ繧ｯ繝ｪ繝励ヨ
笏・  笏披楳笏 build_web_index.py       # 繝悶Λ繧ｦ繧ｶ迚医ン繝ｫ繝峨せ繧ｯ繝ｪ繝励ヨ
笏懌楳笏 vendor/
笏・  笏披楳笏 encoding.min.js          # 繧ｨ繝ｳ繧ｳ繝ｼ繝・ぅ繝ｳ繧ｰ繝ｩ繧､繝悶Λ繝ｪ
笏懌楳笏 run-clickpost-to-amazon.bat    # Python迚亥ｮ溯｡檎畑
笏懌楳笏 build-web-index.bat          # 繝悶Λ繧ｦ繧ｶ迚医ン繝ｫ繝臥畑
笏披楳笏 README.md
```
# クリックポスト → Amazon 出荷通知 変換ツール

クリックポストの出荷通知CSVファイルを、Amazonの「出荷通知アップロード」用フォーマット（CP932、タブ区切り、256列固定）に変換するツールです。Excelテンプレートは使わず、テンプレート1行目の注意文と2行目の日本語ヘッダー、英語の列名をJSONに保持して出力へ反映します。

## 📋 目次

- 必要なファイル
- Python版（推奨）
- ブラウザ版（簡易）
- 設定ファイル
- トラブルシューティング
- プロジェクト構成

## 📁 必要なファイル

- `input/*.csv`: クリックポストの出力ファイル（任意の名前、エンコードは自動検出に対応）
- `config/template_columns.json`: Amazonテンプレートのヘッダーと列名（JSON）
- `config/mapping.json`: 列のマッピング設定（UTF-8）
- `config/config.json`: 入出力形式・出力ファイル名などの共通設定（UTF-8）

## 🐍 Python版（推奨）

### 事前準備
- Python 3.6 以上（追加ライブラリ不要、標準ライブラリのみ）

### 使い方
1) 設定ファイルを用意
   - `config/config.json`（共通設定）
   - `config/mapping.json`（マッピング設定）
2) `input/` フォルダにCSVを配置（エンコードは自動検出: UTF-8, Shift_JIS, CP932 等）
3) 実行（どちらか）
   - `python tools/clickpost_to_amazon.py`
   - `run-clickpost-to-amazon.bat`
4) 出力
   - `output/shipping_confirmation_YYYYMMDD_HHMMSS.txt`（CP932、タブ区切り、256列固定）
   - 必要に応じてCSV出力も可（`config/config.json` の `output.write_csv` を `true`）

## 🌐 ブラウザ版（簡易）

### ビルド
1) HTML生成
   - `python tools/build_web_index.py`
   - または `build-web-index.bat`
   - ルートに `index.html` が生成されます
2) 設定の埋め込み
   - `config/template_columns.json` → `TEMPLATE_COLUMNS`/`HEADER_ROWS`
   - `config/mapping.json` → `MAPCFG`
   - `config/config.json` → `CONFIG`

### 使い方
1) 生成された `index.html` をブラウザで開く
2) CSVファイルをドロップまたは「ファイルを選択」で指定
3) `shipping_confirmation_YYYYMMDD_HHMMSS.txt` が自動ダウンロード（CP932、タブ区切り、256列）

### エンコード（重要）
- 正確なCP932出力のため `vendor/encoding.min.js` が必要です（約27KB）
- 不完全版（約9KB）だとエラーになります。公式から正しいファイルを取得してください

## ⚙ 設定ファイル

### config/config.json（例）
```
{
  "io": { "encoding": "auto", "columns_path": "config/template_columns.json" },
  "format": { "input_date_format": "yyyy/MM/dd", "output_date_format": "yyyy-MM-dd" },
  "output": {
    "write_txt": true, "write_csv": false, "write_xlsx": false,
    "txt_name": "shipping_confirmation.txt", "csv_name": "shipping_confirmation.csv",
    "xlsx_name": "AmazonShippingConfirmation_output.xlsx"
  }
}
```

### config/mapping.json（抜粋・クリックポスト向け）
- 列例（想定）: 0=GoQ管理番号, 1=お問い合わせ番号, 2=出荷日, 4=商品名×数量
- 主要設定:
  - `order-id`: GoQ管理番号の括弧内（`paren_inner`）
  - `order-item-id`: GoQ管理番号の括弧前（`paren_before`）
  - `ship-date`: 出荷日（`parse_date: true`）
  - `tracking-number`: お問い合わせ番号
  - `quantity`: 商品名から×の後ろの数字を抽出（`after_multiply`）
  - `ship-method`: クリックポスト（固定）
  - `carrier-code`: Japan Post（固定）
  - `carrier-name`: 日本郵便（固定）

## 🔧 トラブルシューティング

- 文字化けする/エラーになる
  - 入力CSVのエンコードが不明な場合でも `encoding: auto` で自動判定します
  - ブラウザ版は `encoding.min.js` が正しく配置されているか確認
- マッピングエラー
  - `template_columns.json` の `columns` と `mapping.json` のキー名が一致しているか確認
- 日付が `yyyy/MM/dd` のまま
  - `config/config.json` の `format.output_date_format` を `yyyy-MM-dd` に設定
  - ブラウザ版は再ビルドして `index.html` を生成し直してください

## 📂 プロジェクト構成

```
.
├── config/
│  ├── config.json              # 共通設定
│  ├── mapping.json             # 列マッピング設定
│  └── template_columns.json    # Amazonテンプレート情報
├── input/
│  └── *.csv                    # 入力ファイル（エンコード自動検出）
├── output/
│  └── shipping_confirmation_YYYYMMDD_HHMMSS.txt # 出力ファイル（CP932/タブ/256列）
├── tools/
│  ├── clickpost_to_amazon.py   # メイン変換スクリプト
│  └── build_web_index.py       # ブラウザ版ビルドスクリプト
├── vendor/
│  └── encoding.min.js          # エンコードライブラリ（約27KB）
├── run-clickpost-to-amazon.bat # Python版実行用
├── build-web-index.bat         # ブラウザ版ビルド用
└── index.html                  # 生成されるブラウザ版
```
