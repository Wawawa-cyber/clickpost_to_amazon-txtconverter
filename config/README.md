# 險ｭ螳壹ヵ繧｡繧､繝ｫ隱ｬ譏・
縺薙・繝・ぅ繝ｬ繧ｯ繝医Μ縺ｫ縺ｯ縲√ヤ繝ｼ繝ｫ縺ｮ蜍穂ｽ懊ｒ蛻ｶ蠕｡縺吶ｋ險ｭ螳壹ヵ繧｡繧､繝ｫ縺悟性縺ｾ繧後※縺・∪縺吶・
## 刀 繝輔ぃ繧､繝ｫ荳隕ｧ

| 繝輔ぃ繧､繝ｫ | 隱ｬ譏・| 蠖｢蠑・| 蠢・・|
|---------|------|------|------|
| `config.json` | 蜈ｱ騾夊ｨｭ螳・| UTF-8 | 笨・|
| `mapping.json` | 蛻励・繝・ヴ繝ｳ繧ｰ險ｭ螳・| UTF-8 | 笨・|
| `template_columns.json` | Amazon繝・Φ繝励Ξ繝ｼ繝域ュ蝣ｱ | UTF-8 | 笨・|

---

## 笞呻ｸ・config.json

繝・・繝ｫ蜈ｨ菴薙・蜈ｱ騾夊ｨｭ螳壹ｒ邂｡逅・＠縺ｾ縺吶・
### 搭 險ｭ螳夐・岼

```json
{
  "io": {
    "encoding": "cp932",
    "columns_path": "config/template_columns.json"
  },
  "format": {
    "input_date_format": "yyyyMMdd",
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

### 肌 險ｭ螳夊ｩｳ邏ｰ

#### `io` 繧ｻ繧ｯ繧ｷ繝ｧ繝ｳ
- **`encoding`**: 蜈･蜉帙ヵ繧｡繧､繝ｫ縺ｮ譁・ｭ励お繝ｳ繧ｳ繝ｼ繝・ぅ繝ｳ繧ｰ
  - `"cp932"` - Shift_JIS・医ｆ縺・・繝ｪR縺ｮ讓呎ｺ門ｽ｢蠑擾ｼ・  - `"utf-8"` - UTF-8蠖｢蠑・- **`columns_path`**: 繝・Φ繝励Ξ繝ｼ繝亥・螳夂ｾｩ繝輔ぃ繧､繝ｫ縺ｮ繝代せ

#### `format` 繧ｻ繧ｯ繧ｷ繝ｧ繝ｳ
- **`input_date_format`**: 蜈･蜉帙ヵ繧｡繧､繝ｫ縺ｮ譌･莉伜ｽ｢蠑・  - `"yyyyMMdd"` - 萓・ 20240315
  - `"yyyy-MM-dd"` - 萓・ 2024-03-15
- **`output_date_format`**: 蜃ｺ蜉帙ヵ繧｡繧､繝ｫ縺ｮ譌･莉伜ｽ｢蠑・
#### `output` 繧ｻ繧ｯ繧ｷ繝ｧ繝ｳ
- **`write_txt`**: 繧ｿ繝門玄蛻・ｊTXT繝輔ぃ繧､繝ｫ蜃ｺ蜉帙・譛牙柑/辟｡蜉ｹ
- **`write_csv`**: CSV繝輔ぃ繧､繝ｫ蜃ｺ蜉帙・譛牙柑/辟｡蜉ｹ・医ョ繝舌ャ繧ｰ逕ｨ・・- **`write_xlsx`**: Excel繝輔ぃ繧､繝ｫ蜃ｺ蜉帙・譛牙柑/辟｡蜉ｹ・磯撼謗ｨ螂ｨ・・- **`txt_name`**: 蜃ｺ蜉婬XT繝輔ぃ繧､繝ｫ蜷・- **`csv_name`**: 蜃ｺ蜉佞SV繝輔ぃ繧､繝ｫ蜷・- **`xlsx_name`**: 蜃ｺ蜉妣xcel繝輔ぃ繧､繝ｫ蜷・
---

## 亮・・mapping.json

蜈･蜉佞SV縺ｮ蛻励ｒAmazon繝・Φ繝励Ξ繝ｼ繝医・蛻励↓繝槭ャ繝斐Φ繧ｰ縺吶ｋ險ｭ螳壹〒縺吶・
### 搭 蝓ｺ譛ｬ讒矩

```json
{
  "encoding": "cp932",
  "input_date_format": "yyyyMMdd", 
  "output_date_format": "yyyy-MM-dd",
  "mappings": {
    "Amazon蛻怜錐": {
      "source": "蜈･蜉佞SV蛻怜錐"
    }
  }
}
```

### 識 繝槭ャ繝斐Φ繧ｰ譁ｹ豕・
#### 1. 蜈･蜉佞SV蛻怜錐縺ｫ繧医ｋ謖・ｮ・```json
"order-id": {
  "source": "豕ｨ譁・分蜿ｷ"
}
```

#### 2. 蛻励う繝ｳ繝・ャ繧ｯ繧ｹ縺ｫ繧医ｋ謖・ｮ・```json
"order-id": {
  "index": 0
}
```

#### 3. 蝗ｺ螳壼､縺ｮ險ｭ螳・```json
"carrier-name": {
  "value": "譌･譛ｬ驛ｵ萓ｿ"
}
```

#### 4. 譌･莉伜､画鋤莉倥″繝槭ャ繝斐Φ繧ｰ
```json
"ship-date": {
  "source": "蜃ｺ闕ｷ譌･",
  "parse_date": true
}
```

### 統 險ｭ螳壻ｾ・
```json
{
  "mappings": {
    "order-id": { "source": "豕ｨ譁・分蜿ｷ" },
    "order-item-id": { "source": "繝輔Ν繝輔ぅ繝ｫ繝｡繝ｳ繝茨ｼｯ・ｳ" },
    "quantity": { "value": 1 },
    "ship-date": { "source": "蜃ｺ闕ｷ譌･", "parse_date": true },
    "carrier-code": { "value": "Japan Post" },
    "carrier-name": { "value": "譌･譛ｬ驛ｵ萓ｿ" },
    "tracking-number": { "source": "縺雁撫縺・粋繧上○逡ｪ蜿ｷ" },
    "ship-method": { "source": "豕ｨ譁・分蜿ｷ 縺昴・・・ },
    "ship_from_address_name": { "value": "ABCOSME" },
    "ship_from_address_county": { "value": "JP" }
  }
}
```

### 笞・・豕ｨ諢丈ｺ矩・
1. **蛻怜錐縺ｮ螳悟・荳閾ｴ**: 繝槭ャ繝斐Φ繧ｰ蟇ｾ雎｡縺ｮ蛻怜錐縺ｯ`template_columns.json`縺ｮ`columns`驟榊・縺ｨ螳悟・縺ｫ荳閾ｴ縺吶ｋ蠢・ｦ√′縺ゅｊ縺ｾ縺・2. **譁・ｭ励お繝ｳ繧ｳ繝ｼ繝・ぅ繝ｳ繧ｰ**: UTF-8縺ｧ菫晏ｭ倥＠縺ｦ縺上□縺輔＞
3. **險ｭ螳壹・蜆ｪ蜈磯・ｽ・*: `mapping.json`縺ｮ險ｭ螳壹・`config.json`繧医ｊ蜆ｪ蜈医＆繧後∪縺・
---

## 塘 template_columns.json

Amazon繝・Φ繝励Ξ繝ｼ繝医・蛻玲ュ蝣ｱ縺ｨ繝倥ャ繝繝ｼ陦後ｒ螳夂ｾｩ縺励∪縺吶・
### 搭 讒矩

```json
{
  "header_rows": [
    ["TemplateType=OrderFulfillment", "Version=2011.1102", "豕ｨ諢乗枚..."],
    ["豕ｨ譁・分蜿ｷ", "豕ｨ譁・膚蜩∫分蜿ｷ", "蜃ｺ闕ｷ謨ｰ", "..."]
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

### 肌 險ｭ螳夊ｩｳ邏ｰ

#### `header_rows` 驟榊・
- Amazon繝・Φ繝励Ξ繝ｼ繝医・1陦檎岼・域ｳｨ諢乗枚・峨→2陦檎岼・域律譛ｬ隱槭・繝・ム繝ｼ・・- 蜃ｺ蜉帙ヵ繧｡繧､繝ｫ縺ｮ蜈磯ｭ縺ｫ謖ｿ蜈･縺輔ｌ縺ｾ縺・
#### `columns` 驟榊・  
- Amazon API逕ｨ縺ｮ闍ｱ隱槫・蜷・- 繝・・繧ｿ陦後・蛻鈴・ｺ上ｒ豎ｺ螳・- `mapping.json`縺ｮ繝槭ャ繝斐Φ繧ｰ蟇ｾ雎｡

### 統 繧ｫ繧ｹ繧ｿ繝槭う繧ｺ譁ｹ豕・
1. **譁ｰ縺励＞蛻励・霑ｽ蜉**:
   ```json
   {
     "columns": [
       "order-id",
       "譁ｰ縺励＞蛻怜錐",
       "..."
     ]
   }
   ```

2. **繝倥ャ繝繝ｼ陦後・譖ｴ譁ｰ**:
   ```json
   {
     "header_rows": [
       ["譖ｴ譁ｰ縺輔ｌ縺滓ｳｨ諢乗枚"],
       ["譌･譛ｬ隱槭・繝・ム繝ｼ1", "譌･譛ｬ隱槭・繝・ム繝ｼ2", "..."]
     ]
   }
   ```

---

## 売 險ｭ螳壹・蜆ｪ蜈磯・ｽ・
險ｭ螳壹・驕ｩ逕ｨ鬆・ｺ擾ｼ磯ｫ倥＞鬆・ｼ・

| 蜆ｪ蜈亥ｺｦ | 繝輔ぃ繧､繝ｫ | 隱ｬ譏・|
|-------|---------|------|
| 1・域怙鬮假ｼ・| `mapping.json` | 蛟句挨縺ｮ繝槭ャ繝斐Φ繧ｰ險ｭ螳・|
| 2・井ｸｭ・・| `config.json` | 蜈ｱ騾夊ｨｭ螳・|
| 3・域怙菴趣ｼ・| 繧ｹ繧ｯ繝ｪ繝励ヨ蜀・ョ繝輔か繝ｫ繝・| 譛ｪ謖・ｮ夐・岼縺ｮ繝輔か繝ｼ繝ｫ繝舌ャ繧ｯ |

### 庁 菴ｿ縺・・縺・
- **`config.json`**: 蜈ｨ闊ｬ逧・↑險ｭ螳夲ｼ医お繝ｳ繧ｳ繝ｼ繝・ぅ繝ｳ繧ｰ縲∝・蜉帛ｽ｢蠑上↑縺ｩ・・- **`mapping.json`**: 迚ｹ螳壹・螟画鋤繝ｫ繝ｼ繝ｫ縲∝句挨險ｭ螳壹・荳頑嶌縺・
---

## 屏・・繝医Λ繝悶Ν繧ｷ繝･繝ｼ繝・ぅ繝ｳ繧ｰ

### 繧医￥縺ゅｋ險ｭ螳壹お繝ｩ繝ｼ

| 繧ｨ繝ｩ繝ｼ | 蜴溷屏 | 隗｣豎ｺ遲・|
|--------|------|--------|
| JSON蠖｢蠑上お繝ｩ繝ｼ | 讒区枚髢馴＆縺・| JSON繝舌Μ繝・・繧ｿ繝ｼ縺ｧ遒ｺ隱・|
| 蛻怜錐荳堺ｸ閾ｴ繧ｨ繝ｩ繝ｼ | `mapping.json`縺ｮ蛻怜錐縺形template_columns.json`縺ｫ縺ｪ縺・| 蛻怜錐繧偵メ繧ｧ繝・け繝ｻ菫ｮ豁｣ |
| 繧ｨ繝ｳ繧ｳ繝ｼ繝・ぅ繝ｳ繧ｰ繧ｨ繝ｩ繝ｼ | 蜈･蜉帙ヵ繧｡繧､繝ｫ縺ｨ縺ｮ譁・ｭ励さ繝ｼ繝我ｸ堺ｸ閾ｴ | `encoding`險ｭ螳壹ｒ遒ｺ隱・|
| 譌･莉伜､画鋤繧ｨ繝ｩ繝ｼ | 譌･莉伜ｽ｢蠑上・荳堺ｸ閾ｴ | `input_date_format`縺ｨ`output_date_format`繧堤｢ｺ隱・|

### 剥 險ｭ螳夂｢ｺ隱肴婿豕・
1. **JSON蠖｢蠑上メ繧ｧ繝・け**:
   ```bash
   python -m json.tool config.json
   ```

2. **險ｭ螳壼・螳ｹ縺ｮ遒ｺ隱・*:
   ```bash
   python tools/clickpost_to_amazon.py --dry-run
   ```

3. **繝・ヰ繝・げ逕ｨCSV蜃ｺ蜉・*:
   ```json
   {
     "output": {
       "write_csv": true
     }
   }
   ```

---

## 答 蜿り・ュ蝣ｱ

- **繧ｵ繝ｳ繝励Ν險ｭ螳・*: `sample/mapping_prompt.txt`縺ｫ隧ｳ邏ｰ縺ｪ菴懈・謇矩・′縺ゅｊ縺ｾ縺・- **Amazon繝・Φ繝励Ξ繝ｼ繝・*: `sample/`繝・ぅ繝ｬ繧ｯ繝医Μ蜀・・Excel繝輔ぃ繧､繝ｫ繧貞盾辣ｧ
- **繧ｨ繝ｩ繝ｼ蟇ｾ蠢・*: 繝｡繧､繝ｳ縺ｮ`README.md`縺ｮ繝医Λ繝悶Ν繧ｷ繝･繝ｼ繝・ぅ繝ｳ繧ｰ繧ｻ繧ｯ繧ｷ繝ｧ繝ｳ繧貞盾辣ｧ