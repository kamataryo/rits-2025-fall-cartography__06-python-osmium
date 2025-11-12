"""
例2: 特定のタグを持つ地物を抽出する

このスクリプトは、指定されたタグを持つノードやウェイを抽出し、
結果を表示します。

使い方:
    uv run 02_tag_filter.py
"""

import os, json

from src.handlers import TagFilterHandler

# ========== 設定 ==========
# 処理するOSMファイルのパス
OSM_FILE = "data/shikoku.osm.pbf"
# ==========================

def main():
    """メイン処理"""
    # ハンドラーをインスタンス化
    restaurantHandler = TagFilterHandler("amenity", "restaurant")

    # OSMファイルを処理
    restaurantHandler.apply_file(OSM_FILE)

    # 結果を表示
    restaurantHandler.print_summary()
    print(restaurantHandler.nodes[0])  # 最初のノードを表示

if __name__ == "__main__":
    main()
