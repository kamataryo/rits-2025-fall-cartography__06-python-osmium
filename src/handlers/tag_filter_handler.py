"""
特定のタグを持つOSMデータを抽出するハンドラー

このモジュールは、指定されたタグ（key=value）を持つ
ノードやウェイを抽出します。
"""

import osmium


class TagFilterHandler(osmium.SimpleHandler):
    """
    特定のタグを持つ地物を抽出するハンドラー

    このクラスは、指定されたタグのキーと値に一致する
    OSMの要素を抽出します。

    属性:
        target_key (str): 検索するタグのキー（例: "amenity", "highway"）
        target_value (st): 検索するタグの値（例: "restaurant", "primary"）
        nodes (list): 条件に一致したノードのリスト
        ways (list): 条件に一致したウェイのリスト
    """

    def __init__(self, target_key, target_value):
        """
        ハンドラーを初期化

        引数:
            target_key (str): 検索するタグのキー
            target_value (str): 検索するタグの値。
        """
        super().__init__()
        self.target_key = target_key
        self.target_value = target_value
        self.nodes = []
        self.ways = []

    def _matches_filter(self, tags):
        """
        タグがフィルター条件に一致するかチェック。

        アンダースコア(_)で始まるメソッドは、プライベートメソッドとして扱われます。
        プライベートメソッドとは、クラスの内部でのみ使用されることを意図したメソッドです。
        言語によっては、アクセス制御の仕組みがあり、外部からのアクセスを制限できますが、
        Pythonには存在しないため、慣習的にアンダースコアを用いてプライベートメソッドを示します。

        引数:
            tags: osmium.osm.TagList オブジェクト

        戻り値:
            bool: 条件に一致する場合True
        """
        # タグのキーが存在するかチェック
        if self.target_key not in tags:
            return False

        # target_valueが指定されていない場合、キーの存在のみで判定
        if self.target_value is None:
            return True

        # キーと値の両方が一致するかチェック
        return tags[self.target_key] == self.target_value

    def node(self, n):
        """
        ノードを処理し、条件に一致すれば保存

        引数:
            n: osmium.osm.Node オブジェクト
        """
        if self._matches_filter(n.tags):
            # 必要な情報を辞書形式で保存
            node_data = {
                'id': n.id,
                'lat': n.location.lat,
                'lon': n.location.lon,
                'tags': dict(n.tags)
            }
            self.nodes.append(node_data)

    def way(self, w):
        """
        ウェイを処理し、条件に一致すれば保存

        引数:
            w: osmium.osm.Way オブジェクト
        """
        if self._matches_filter(w.tags):
            # ウェイを構成するノードのIDリストを取得
            node_ids = [node.ref for node in w.nodes]

            # 必要な情報を辞書形式で保存
            way_data = {
                'id': w.id,
                'nodes': node_ids,
                'tags': dict(w.tags),
            }
            self.ways.append(way_data)

    def get_results(self):
        """
        抽出結果を辞書形式で返す

        戻り値:
            dict: 抽出されたノードとウェイを含む辞書
                {
                    'filter': {'key': str, 'value': str},
                    'nodes': list,
                    'ways': list,
                    'counts': {'nodes': int, 'ways': int, 'total': int}
                }
        """
        return {
            'filter': {
                'key': self.target_key,
                'value': self.target_value
            },
            'nodes': self.nodes,
            'ways': self.ways,
            'counts': {
                'nodes': len(self.nodes),
                'ways': len(self.ways),
                'total': len(self.nodes) + len(self.ways),
            }
        }

    def print_summary(self):
        """抽出結果のサマリーをコンソールに表示"""
        print("=" * 50)
        print("タグフィルタリング結果")
        print("=" * 50)
        print(f"検索条件: {self.target_key}", end="")
        if self.target_value:
            print(f"={self.target_value}")
        else:
            print(" (値は任意)")
        print("-" * 50)
        print(f"一致したノード数:     {len(self.nodes):,}")
        print(f"一致したウェイ数:     {len(self.ways):,}")
        print("-" * 50)
        print(f"合計:                 {len(self.nodes) + len(self.ways):,}")
        print("=" * 50)
