"""
特定のタグを持つOSMデータを抽出するハンドラー

このモジュールは、指定されたタグ（key=value）を持つ
ノードやウェイを抽出します。
"""

from src.handlers import TagFilterHandler


class TagFilterAndTransformToGeojsonHandler(TagFilterHandler):
    """
    GeoJSON形式に変換可能なタグフィルタハンドラー

    属性:
        target_key (str): 検索するタグのキー（例: "amenity", "highway"）
        target_value (st): 検索するタグの値（例: "restaurant", "primary"）
        nodes (list): 条件に一致したノードのリスト
        ways (list): 条件に一致したウェイのリスト
    """

    """Node のみを抽出して GeoJSON で出力するメソッド"""
    def to_geojson(self):

      # 最初に、Way に登場する Node を除外するためのセットを作成
      node_ids_in_way = set()
      for way in self.ways:
        for node_id in way['nodes']:
          node_ids_in_way.add(node_id)

      # 次に、Node のみを抽出
      filtered_nodes = [node for node in self.nodes if node['id'] not in node_ids_in_way]

      # GeoJSON 形式に変換
      features = []
      for node in filtered_nodes:
        feature = {
          "type": "Feature",
          "id": node['id'],
          "geometry": {
            "type": "Point",
            "coordinates": [node['lon'], node['lat']]
          },
          "properties": dict(node['tags'])
        }
        features.append(feature)

      geojson = {
        "type": "FeatureCollection",
        "features": features
      }
      return geojson

