# Python-Osmium 演習

このリポジトリは、データベース演習;コンピューターグラフィクス演習II で使用する教材です。Python と pyosmium ライブラリを使用して、OpenStreetMap（OSM）データの処理方法を学習します。

## 📚 学習内容

このチュートリアルでは、以下のスキルを習得します：

1. **Python の基礎**: 初歩的な Python プログラミング
2. **OSM データの理解**: OpenStreetMap のデータ構造（ノード、ウェイ、リレーション）
3. **データ抽出**: pyosmium を使用した地理データの抽出
4. **データ加工**: Python を使用した地図データの処理と変換

## 🔧 必要な環境

- **開発環境**: GitHub Codespaces（推奨）またはローカル環境
- **Python**: 3.8 以上
- **パッケージマネージャー**: [uv](https://github.com/astral-sh/uv)

##  Codespace 環境でのセットアップ

```shell
$ pip install uv
```

## 🚀 ローカル環境でのセットアップ手順

### 1. リポジトリのクローン

```bash
git clone <このリポジトリのURL>
cd rits-2025-fall-cartography__06-python-osmium
```

### 2. uv のインストール（まだの場合）

#### macOS / Linux
```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. 依存関係のインストール

```bash
# 仮想環境を作成
uv venv

# pyosmium 等のインストール
uv sync
```

## 📖 使い方

### 基本的な実行方法

```bash
# スクリプトの実行（例）
uv run scripts/example.py
```

### OSM データの準備

1. [Geofabrik](https://download.geofabrik.de/) や [OpenStreetMap](https://planet.openstreetmap.org/) から `.osm.pbf` ファイルをダウンロード
2. `data/` ディレクトリに配置（ディレクトリは必要に応じて作成）

```bash
mkdir -p data
# ダウンロード例（四国のデータ）
# https://download.geofabrik.de/asia/japan.html
$ curl -L https://download.geofabrik.de/asia/japan/shikoku-latest.osm.pbf -o data/shikoku.osm.pbf
```

## 🗂️ プロジェクト構造（予定）

```
rits-2025-fall-cartography__06-python-osmium/
├── .venv/              # 仮想環境（自動生成、git管理外）
├── data/               # OSMデータファイル（.osm.pbf など）
├── src/                # ソースコード
│   ├── handlers/       # カスタムosmiumハンドラー
│   ├── filters/        # データフィルタリング
│   └── utils/          # ユーティリティ関数
├── scripts/            # 実行用スクリプト
├── examples/           # サンプルコード
├── results/            # 出力結果（git管理外）
├── tests/              # テストコード
├── CLAUDE.md           # AI アシスタント向けガイド
├── README.md           # このファイル
└── requirements.txt    # 依存関係リスト
```

## 🎓 チュートリアルの流れ

### Step 1: Python の基礎
- 変数とデータ型
- 制御構文（if文、for文）
- 関数の定義と使用
- ファイルの読み書き

### Step 2: OpenStreetMap データの理解
- OSM データ構造の基礎
  - **ノード（Node）**: 地点（座標を持つ点）
  - **ウェイ（Way）**: 線や領域（ノードの集合）
  - **リレーション（Relation）**: 複雑な地物（ウェイやノードの関係）
- タグの仕組み（key=value）

### Step 3: pyosmium による データ抽出
- `osmium.SimpleHandler` の使い方
- ノード、ウェイ、リレーションの処理
- タグのフィルタリング
- 地理的範囲でのフィルタリング

### Step 4: データの加工と出力
- 抽出したデータの整形
- JSON / GeoJSON 形式での出力
- CSV 形式での統計データ出力
- 結果の可視化

## 💡 サンプルコード

### 基本的なハンドラーの例

```python
import osmium

class CountHandler(osmium.SimpleHandler):
    """OSMデータ内の地物をカウントするハンドラー"""

    def __init__(self):
        super().__init__()
        self.nodes = 0
        self.ways = 0
        self.relations = 0

    def node(self, n):
        """ノード（点）を処理"""
        self.nodes += 1

    def way(self, w):
        """ウェイ（線・面）を処理"""
        self.ways += 1

    def relation(self, r):
        """リレーション（複雑な地物）を処理"""
        self.relations += 1

# 使用例
handler = CountHandler()
handler.apply_file("data/shikoku.osm.pbf")
print(f"ノード数: {handler.nodes}")
print(f"ウェイ数: {handler.ways}")
print(f"リレーション数: {handler.relations}")
```

## 🔍 トラブルシューティング

### メモリ不足エラー

大きな OSM ファイル（数GB）を処理する場合：
- より小さな地域のデータから始める
- ストリーミング処理を活用（データ全体をメモリに読み込まない）
- 必要なデータのみをフィルタリング

### ファイルが見つからない

```bash
# ファイルパスを確認
ls -la data/

# 絶対パスで指定
handler.apply_file("/full/path/to/data/file.osm.pbf")
```

## 📚 参考資料

- [OpenStreetMap Wiki](https://wiki.openstreetmap.org/)
- [pyosmium ドキュメント](https://osmcode.org/pyosmium/)
- [OSM データ構造](https://wiki.openstreetmap.org/wiki/Elements)
- [Geofabrik ダウンロード](https://download.geofabrik.de/)
