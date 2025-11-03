"""
例2: 特定のタグを持つ地物を抽出する

このスクリプトは、指定されたタグを持つノードやウェイを抽出し、
結果をJSON形式で保存します。

使い方:
    uv run 02_tag_filter.py
"""

import os, json

from src.handlers import TagFilterHandler

# ========== 設定 ==========
# 処理するOSMファイルのパス
OSM_FILE = "data/shikoku.osm.pbf"

# 検索するタグのキー（例: "amenity", "highway", "shop" など）
TARGET_KEY = "amenity"

# 検索するタグの値（例: "restaurant", "cafe", "school" など）
# Noneに設定すると、キーの存在のみをチェックします
TARGET_VALUE = "restaurant"
# ==========================

def main():
    """メイン処理"""
    # ハンドラーを作成
    handler = TagFilterHandler(TARGET_KEY, TARGET_VALUE)

    # OSMファイルを処理
    handler.apply_file(OSM_FILE)

    # 結果を表示
    handler.print_summary()

    # 結果をJSON形式で保存
    results = handler.get_results()

    # resultsディレクトリを作成
    if not os.path.exists("results"):
      os.makedirs("results")

    # ファイル名を生成
    geojson_filename = f"results/{TARGET_KEY}_{TARGET_VALUE}.geojson"

    # ノードをGeoJSON形式で保存
    if results['nodes']:
        geojson = nodes_to_geojson(results['nodes'])

        # ファイル保存
        with open(geojson_filename, 'w', encoding='utf-8') as f:
          json.dump(geojson, f, indent=4, ensure_ascii=False)

        print(f"GeoJSONファイルを保存しました: {geojson_filename}")


def nodes_to_geojson(nodes):
    """
    ノードのリストをGeoJSONのFeatureリストに変換

    引数:
        nodes (List[Dict]): ノードのリスト
                           各ノードは 'id', 'lat', 'lon', 'tags' を含む辞書

    戻り値:
        List[Dict]: GeoJSONのFeatureリスト

    例:
        >>> nodes = [
        ...     {'id': 1, 'lat': 35.6812, 'lon': 139.7671, 'tags': {'name': '東京駅'}}
        ... ]
        >>> features = nodes_to_geojson_features(nodes)
    """
    features = []

    for node in nodes:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [node['lon'], node['lat']],
            },
            'id': node['id'],
            'properties': {},
        }

        # タグをプロパティに追加
        tags = node.get('tags', {})
        for key, value in tags.items():
            feature['properties'][key] = value
        features.append(feature)

    return {
        'type': 'FeatureCollection',
        'features': features,
    }


if __name__ == "__main__":
    main()
