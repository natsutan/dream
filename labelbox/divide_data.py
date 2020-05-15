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

    test_list = []
    valid_list = []
    train_list = []
    for i, col in enumerate(f):
        fp = img_path + col[9]
        c = i % 3
        if  c == 1 and len(test_list) < 100:
            test_list.append(fp)
        elif c == 2 and len(valid_list) < 100:
            valid_list.append(fp)
        else:
            train_list.append(fp)

print(test_list)
print(valid_list)
print(train_list)

'''
デバッグ中
'''