# mint project 設定ファイルなど

## network設定
mint.cfg がNNの設定ファイルです。

元となるファイルはここを参照してください。<br>
https://github.com/pjreddie/darknet/blob/master/cfg/yolov2-voc.cfg

mint.cfgとyolov2-voc.cfgのdiffを取ると修正箇所が分かります。

## 設定ファイル
- datasets.data 
- train.txt
- val.txt
- test.txt

test.txtは使わなかったような・・・

## スクリプト

- gen_data.py データオーギュメンテーション
- gen_test.py train.txt等の生成スクリプト

gen_test.pyはglob等の使い方のサンプルとして見てください。

## 学習ログ
- train.log darknetの学習ログ
- loss.txt train.logからlossの部分だけを抜き出し。

## 学習注意点
デフォルトで、weightファイルの保存が、100, 200, ... 900, 10000 epocと、900から10000まで非常に間がある。使いにくいので、ソースファイルの修正を推奨します。

https://github.com/pjreddie/darknet/blob/61c9d02ec461e30d55762ec7669d6a1d3c356fb2/examples/detector.c#L138

```c
if(i%10000==0 || (i < 1000 && i%100 == 0)){
```

i%10000==0をi%1000==0 に修正すると、1000 epoc毎にファイルを保存します。

