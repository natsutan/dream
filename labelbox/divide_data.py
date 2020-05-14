#!python3
import csv

# イメージパス
img_path = "dummy/image/"

# 読み込むファイルのパス
path = "csv/export.csv"

with open(path) as file:
    # リスト形式
    f = csv.reader(file, delimiter=",", doublequote=True, lineterminator="\n", quotechar='"', skipinitialspace=True)
    header = next(f)
    a = 0
    for col in f:
        print(f)
        a = a + 1
        if a == 10:
            break


'''
１０行だけデバッグしてみたが、結果は以下
<_csv.reader object at 0x100c0a978>
<_csv.reader object at 0x100c0a978>
<_csv.reader object at 0x100c0a978>
<_csv.reader object at 0x100c0a978>
<_csv.reader object at 0x100c0a978>
<_csv.reader object at 0x100c0a978>
<_csv.reader object at 0x100c0a978>
<_csv.reader object at 0x100c0a978>
<_csv.reader object at 0x100c0a978>
<_csv.reader object at 0x100c0a978>
想定は、カンマ区切りのデータ
'''