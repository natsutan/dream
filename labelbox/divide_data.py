#!python3
import csv

# イメージパス
img_path = "dummy/image/"

# 読み込むファイルのパス
path = "csv/export.csv"

with open(path, 'r') as file:
    # リスト形式
    f = csv.reader(file, delimiter=',', quotechar='"')

    # ヘッダーはスキップ
    next(f)

    name = []
    for col in f:
        name.append(img_path + col[9])

print(name)

'''
デバッグ中
'''