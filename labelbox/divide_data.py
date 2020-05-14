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
    a = 0
    for col in f:
        print(col)
        a = a + 1
        if a == 10:
            break


'''
デバッグ中
'''