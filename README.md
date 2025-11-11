# Python-Osmium 演習

このリポジトリは、データベース演習;コンピューターグラフィクス演習II で使用する教材です。Python と pyosmium ライブラリを使用して、OpenStreetMap（OSM）データの処理方法を学習します。

## 学習内容

このチュートリアルでは、以下のスキルを習得します：

1. **Python の基礎**: 初歩的な Python プログラミング
2. **OSM データの理解**: OpenStreetMap のデータ構造（ノード、ウェイ、リレーション）
3. **データ抽出**: pyosmium を使用した地理データの抽出
4. **データ加工**: Python を使用した地図データの処理と変換

## 🔧 必要な環境

- **開発環境**: GitHub Codespaces（推奨）またはローカル環境
- **Python**: 3.8 以上
- **パッケージマネージャー**: [uv](https://github.com/astral-sh/uv)

## Codespace 環境でのセットアップ

```shell
$ pip install uv
```

## ローカル環境でのセットアップ

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

## 🎓 チュートリアルの流れ

### Step 1: Python の基礎
- クラス構文
- オブジェクト指向プログラミング

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

## 課題

### 出題

1. 興味のあるテーマ（例：カフェ、寺社、登山道など）を選び、02_tag_filter.py を改造して該当するタグを抽出してください。見つかったタグの種類や表記の揺れなど、気づいた点・面白い点をまとめてください。
2. 授業では四国のデータを扱いました。他の地域のデータ（例: 近畿など）をダウンロードして、同様の処理を行なってみてください。その時、1 でまとめたタグのデータとはどのような違いがありましたか？気づいた点などをまとめてください。
3. 1と2で取得したタグのデータについて、
   - 3-1. どのような分析ができると思いますか？ご自身の興味などに基づいてまとめてください。
   - 3-2. 統計的な解析を行いたい場合、どのような点に注意したら良いと思いますか？
   
### 提出方法

- PDF で提出。A4サイズ相当で1枚以上(多い分には問題ありません)
- 図や表を添えても良い
- manaba+R 経由で提出(次回授業(11/11(火))開始前まで)


## 📚 参考資料

- [OpenStreetMap Wiki](https://wiki.openstreetmap.org/)
- [pyosmium ドキュメント](https://osmcode.org/pyosmium/)
- [OSM データ構造](https://wiki.openstreetmap.org/wiki/Elements)
- [Geofabrik ダウンロード](https://download.geofabrik.de/)
