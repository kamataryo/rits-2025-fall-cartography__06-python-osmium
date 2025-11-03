"""
例1: OSMデータの要素数をカウントする

このスクリプトは、OSMファイルに含まれる
ノード、ウェイ、リレーションの数を集計します。

使い方:
    uv run 01_count_handler.py
"""

from src.handlers import CountHandler

# ========== 設定 ==========
# 処理するOSMファイルのパス
OSM_FILE = "data/shikoku.osm.pbf"
# ==========================


def main():
    """メイン処理"""

    # ハンドラーを作成
    # CountHandler クラスのインスタンスを生成
    handler = CountHandler()

    # OSMファイルを処理
    handler.apply_file(OSM_FILE)

    # 結果を表示
    handler.print_summary()


if __name__ == "__main__":
    main()
