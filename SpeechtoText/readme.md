# Google Speech-to-Text

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
      * windows 用メモ:  
        ``` 
        1. 以下の URL から最新版の zip をダウンロード
           https://github.com/BtbN/FFmpeg-Builds/releases  
           FFmpeg-Builds-latest.zip
        2. 適当なフォルダに解凍
        3. 解凍したフォルダ内の bin に対して環境変数を設定
        4. cmd を開き、ffmpeg -version が通れば OK 
        ```
* pip
    * ffmpeg-python
    * opencv-python

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
    * 調整中
4. 結果の確認
    * 調整中

## 諸注意事項など
* 動画ファイル内の音声情報が多くエラーとなる場合、3 分（180 秒）より短い値で分割する
    * config.ini の stride の値を変更する
* 3 分の音声ファイル 1 つあたりの処理時間の目安で 30 ~ 50 秒。
    * 変換元の動画ファイルが 1 時間の場合、プログラムの実行時間はおよそ 10 ~ 15 分。
    * 実行環境のスペック、音声ファイル内の抽出文字数により前後する
