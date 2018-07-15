# IoT仮想通貨ゴミ箱StartupWeekend深圳おじさん(StartupWeekend@深圳)
QRコードからビットコインアドレスを読み取らせた後にゴミを捨てると、お礼にビットコインを振り込んでくれるゴミ箱です。

# 動かし方
```
./setup.sh # これだけでは動かないかも...
vi env # Blockchainのウォレットを動かすための環境変数をセット
./start.sh
```

# 構成
ハード側:  
Raspberry Pi + Webカメラ + 光センサーで構成。  
ソフト側:  
ビットコインウォレット + QRコード読み取り + ごみ捨て検知の３プロセスで構成。  

## 個別モジュール
ビットコインウォレットのみ既存のウォレットを活用。  
それ以外の2プロセスはPython3系を使用。

## 通信
QRコード読み取りモジュール >> ゴミ捨て検知ではファイルを使用。読み取ったビットコインアドレスをファイルに吐き出す。  
ゴミ捨て検知 >> ビットコインウォレットでは、専用のラッパーを用意した上でlocalohostのAPIを叩いて通信する。  


# QRコード読み取り
## カメラ
v4l2captureモジュールを使用。(StartupWeekendのプロトタイプではfswebcamを使用)  
RaspberryPiには専用カメラモジュールが存在することもあり、Web上にラズパイで挑戦したドキュメントが少なかった点がチャレンジだった。  
使用するWebカメラによっては映像が上下反転してしまい、QRコードの認識に影響があった点がポイント。  
また、原因不明ながらWebカメラがbroken pipeエラーで起動しないことがある。より低レイヤーな言語で利用すれば原因判別がしやすかったのではないか。  

## QRコード認識
QRコード認識はzbarモジュールを使用。
画像が上下反転していると正しく認識しないことに気がつくことに時間を費やした。  
また、video.read()したバイトオブジェクトを直接zbarに読み取らせることで性能が上がると予想されるが、そのためにはvideoをグレイスケールで起動する必要がある。  
その場合に映像のサイズがよくわからないことになるため、いったんRGBで起動してからImageオブジェクトを作成、グレースケール変換をすることとした。  

# ゴミ捨て検知
ループを回す本体`reward_payer.py`と、ゴミ検知などの各モジュール`garbage_sensor.py`, `wallet/py`, `director.py`などに分けている。  
将来的にウォレットを入れ替えたり、ゴミ捨て時の演出を追加したりすべく、オブジェクトごとに分けたプログラミングを心がけた。  
この手法はハッカソンなどでも将来的にリリースを見込む場合に有効なのではないか。
技術的に難しいところは特にないが、光センサーの誤作動が多いため超音波センサーなどと合わせて運用することも考えたい。  


# WebCameraのためのライブラリ導入メモ
sudo apt-get install libzbar-dev libzbar0
wget https://linuxtv.org/downloads/v4l-utils/v4l-utils-1.14.2.tar.bz2
tar -jxvf v4l-utils-1.14.2.tar.bz2
apt-get install debhelper dh-autoreconf autotools-dev autoconf-archive doxygen graphviz libasound2-dev libtool libjpeg-dev libqt4-dev libqt4-opengl-dev libudev-dev libx11-dev pkg-config udev make gcc git

./bootstrap.sh
./configure
sudo apt-get remove libi2c-dev
make
sudo make install


# プロトタイプ(StartupWeekend@深圳) - 反省
* デモ前にexceptionでPythonのプロセスが落ちてしまった → 例外は一括キャッチすべき(Webアプリならレスポンスが変になるだけで済むが、ラズパイごと落ちてしまうため) 
* 光センサーの誤作動がままあった
* QRコードの解析APIへのリクエスト・値受け取り >> DONE
* 画像解析をローカル上で完結できるようにしたい >> DONE


# 今後の課題
* ビットコインキャッシュウォレットの作成, API経由での呼び出し
* インターネット環境悪くても送金ができるようにしたい