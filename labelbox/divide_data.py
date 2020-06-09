#!python3
import csv
import json

# ファイル書き込み
def file_w(p, l):
    with open(p, 'w') as f:
        f.write('\n'.join(l))

def main():
    # イメージパス
    img_path = "dummy/image/"

    # 読み込みファイルのパス
    path = "csv/export.csv"

    # テストファイルのパス
    test_path = "test.txt"
    # 検証ファイルのパス
    valid_path = "validation.txt"
    # 訓練ファイルのパス
    train_path = "train.txt"

    with open(path, 'r') as f:
        # リスト形式に読み込む
        l = csv.reader(f, delimiter=',', quotechar='"')

        # ヘッダーはスキップ
        next(l)

        test_list = []
        valid_list = []
        train_list = []
        for i, col in enumerate(l):
            # オブジェクトの情報が空の場合はスキップ
            json_data = json.loads(col[3])
            if not json_data:
                continue

            fp = img_path + col[9]
            c = i % 3
            if  c == 1 and len(test_list) < 100:
                test_list.append(fp)
            elif c == 2 and len(valid_list) < 100:
                valid_list.append(fp)
            else:
                train_list.append(fp)

    # テストファイル書き込み
    file_w(test_path, test_list)

    # 検証ファイル書き込み
    file_w(valid_path, valid_list)

    # 訓練ファイル書き込み
    file_w(train_path, train_list)

if __name__ == "__main__":
    main()
