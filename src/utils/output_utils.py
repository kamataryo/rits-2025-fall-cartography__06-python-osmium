"""
データ出力に関するユーティリティ関数

このモジュールは、抽出したOSMデータをJSON、CSV、GeoJSONなどの
形式で出力するための関数を提供します。
"""

import csv


def write_csv(data, output_path, fieldnames=None):
    """
    データをCSV形式でファイルに書き込む

    引数:
        data (List[Dict]): CSV形式で書き込むデータのリスト
                          各要素は辞書形式
        output_path (str): 出力ファイルのパス
        fieldnames (List[str], optional): CSVのヘッダー（列名）
                                         指定しない場合、最初のデータから自動抽出

    戻り値:
        bool: 書き込みが成功した場合True

    例:
        >>> data = [
        ...     {'id': 1, 'name': '東京駅', 'type': 'station'},
        ...     {'id': 2, 'name': '新宿駅', 'type': 'station'}
        ... ]
        >>> write_csv(data, "results/stations.csv")
        True
    """
    if not data:
        print("警告: 書き込むデータが空です")
        return False

    try:
        # fieldnamesが指定されていない場合、最初のデータから取得
        if fieldnames is None:
            fieldnames = list(data[0].keys())

        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"CSVファイルを保存しました: {output_path}")
        return True
    except Exception as e:
        print(f"CSVファイルの書き込みに失敗しました: {e}")
        return False


def write_geojson(features, output_path):
    """
    データをGeoJSON形式でファイルに書き込む

    引数:
        features (List[Dict]): GeoJSONのfeatureリスト
                              各featureは座標情報とプロパティを含む
        output_path (str): 出力ファイルのパス

    戻り値:
        bool: 書き込みが成功した場合True

    例:
        >>> features = [
        ...     {
        ...         'type': 'Feature',
        ...         'geometry': {
        ...             'type': 'Point',
        ...             'coordinates': [139.7671, 35.6812]
        ...         },
        ...         'properties': {'name': '東京駅'}
        ...     }
        ... ]
        >>> write_geojson(features, "results/points.geojson")
        True
    """
    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }

    return write_json(geojson, output_path, indent=2, ensure_ascii=False)



