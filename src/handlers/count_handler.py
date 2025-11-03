"""
OSMデータの要素数をカウントするハンドラー

このモジュールは、OpenStreetMapデータに含まれる
ノード、ウェイ、リレーションの数を集計します。
"""

import osmium


class CountHandler(osmium.SimpleHandler):
    """
    OSMデータ内の地物をカウントするハンドラー(= 処理機構、ハンドラーと呼び表されることが多い)

    このクラスは、OSMファイルを読み込んで、
    含まれる各要素タイプ（ノード、ウェイ、リレーション）の
    数を集計します。
    CountHandler は osmium.SimpleHandler を継承しています。

    属性:
        nodes (int): ノードの総数
        ways (int): ウェイの総数
        relations (int): リレーションの総数
    """

    def __init__(self):
        """
        コンストラクタと呼ばれる初期化メソッド。
        クラスのインスタンスが生成されるときに呼び出されます。
        一般的に、コンストラクタにおいては、データの初期値を設定するなどの処理が行われます。

        ハンドラーを初期化し、カウンターを0に設定
        """
        # 親クラスのコンストラクタを呼び出し。
        super().__init__()
        self.nodes = 0
        self.ways = 0
        self.relations = 0

    def node(self, n):
        """
        ノード（点）を処理

        ノードは、緯度・経度を持つ地点を表します。
        例：建物の入口、木、街灯など

        引数:
            n: osmium.osm.Node オブジェクト
        """
        self.nodes += 1

    def way(self, w):
        """
        ウェイ（線・面）を処理

        ウェイは、複数のノードを結んだ線や領域を表します。
        例：道路、建物の輪郭、河川など

        引数:
            w: osmium.osm.Way オブジェクト
        """
        self.ways += 1

    def relation(self, r):
        """
        リレーション（複雑な地物）を処理

        リレーションは、複数の要素（ノード、ウェイ、他のリレーション）
        の関係を表します。
        例：バス路線、境界線、複雑な建物など

        引数:
            r: osmium.osm.Relation オブジェクト
        """
        self.relations += 1

    def print_summary(self):
        """集計結果をコンソールに表示"""
        print("=" * 50)
        print("OSMデータ集計結果")
        print("=" * 50)
        print(f"ノード数（点）:       {self.nodes:,}")
        print(f"ウェイ数（線・面）:   {self.ways:,}")
        print(f"リレーション数:       {self.relations:,}")
        print("-" * 50)
        print(f"合計:                 {self.nodes + self.ways + self.relations:,}")
        print("=" * 50)


    def get_counts(self):
        """
        実習: 以下の戻り値を持つメソッドを実装してください

        戻り値:
            dict: 各要素タイプの数を含む辞書
                {
                    'nodes': int,
                    'ways': int,
                    'relations': int,
                    'total': int
                }
        """
        raise NotImplementedError('このメソッドは未実装です')
