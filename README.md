# StartupWeekend@深圳 - RaspberryPi
## セットアップ
* MacbookとRaspberry Piを同じネットワーク下に置く必要あり(テザリング等...)
  ※ 無料WiFiだとラズパイがWebのログイン画面を通ることができず詰みます。
* オーディオ出力をアナログに切り替える必要あり(マウス操作がラク)
* SSHでRaspberry Piにログインする
```console
ssh pi@127.20.10.11 # 環境は各自/デフォルトのパスワードはraspberry
```

* GrovePi関連のセットアップ
* A1: 光センサー
* D4: カメラ
  ※ラズパイ画面を外すと入出力にエラーが出るので注意


## カバー開閉
```console
# 音声ファイルのコピー
scp ./jinglebellssms.mp3 pi@172.20.10.11:/home/pi
# remoteではsuperuser権限がないため, まずは権限のあるディレクトリにコピーする
ssh pi@172.20.10.11
sudo cp /home/pi/jinglebellssms.mp3 /GrovePi/Projects/Sensor_Twitter_Feed/jinglebellssms.mp3

# プログラム実行
python cover_open_close.py
```


## ボタンでカメラ撮影
```
apt-get install fswebcam # RaspberryPi用の汎用Webカメラモジュール
# 撮影したカメラ画像をアップロードするサーバーの設定

# プログラム実行
python button_to_camera.py
```


# 反省
* デモ前にexceptionでPythonのプロセスが落ちてしまった → 例外は一括キャッチすべき(Webアプリならレスポンスが変になるだけで済むが、ラズパイごと落ちてしまうため)  
* 光センサーの誤作動がままあった


# 今後の課題
* QRコードの解析APIへのリクエスト・値受け取り
* ビットコインキャッシュウォレットの作成, API経由での呼び出し
* 画像解析をローカル上で完結できるようにしたい
* インターネット環境悪くても送金ができるようにしたい


# 参考
https://raspberrypi.stackexchange.com/questions/7088/playing-audio-files-with-python  