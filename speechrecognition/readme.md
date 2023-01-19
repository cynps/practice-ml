# readme

## what is this
* conv.py
    * 動画を音声ファイルに変換
    * SpeechRecognition にロードするために ３分以内に分割
* voice_test.py
    * 分割済み音声ファイルを読み込み、テキストを抽出
    * 抽出したテキスト文字列を result.txt に追記

## 環境
* apt
    * python3
    * python3-pip
    * ffmpeg
* pip
    * SpeechRecogntion 
    * ffmpeg-python

## 使い方
1. 環境構築
2. conv.py の変数を調整して実行
    * 実行コマンド（参考）  
        ```
        # python3 conv.py
        ```
    * srcfilepath, rangeparam の値を設定する
    * サンプルコードでは、 dist/src/ 配下に音声ファイルへの変換元動画ファイルを格納する想定
3. voice_test.py の変数を調整して実行
    * 実行コマンド（参考）  
        ```
        # python3 voice_test.py
        ```
    * rangeparam の値を設定する（conv.py の値と合わせる）
    * サンプルコードでは、 dist/output/ 配下にテキストファイルへの変換元音声ファイルを格納する想定
4. 結果の確認
    * dist/output/result.txt に追記される
    * 過去分が不要な場合は、手動で削除する
    * ファイル自体を削除するとエラーになるので、最低限、空ファイルは残す。

## 諸注意事項など
* エラー制御（ファイルの排他処理）は行っていないため、エラー発生時は適宜対応する
* 動画ファイル内の音声情報が多くエラーとなる場合、3 分（180 秒）より短い値で分割する
* 3 分の音声ファイル 1 つあたりの処理時間の目安で 30 ~ 50 秒。
    * 変換元の動画ファイルが 1 時間の場合、プログラムの実行時間はおよそ 10 ~ 15 分。
    * 実行環境のスペック、音声ファイル内の抽出文字数により前後する
* speech recognition は Google api のため、オフライン環境では実行できない。（インターネット接続環境が必要）