# 天気自動返信ツール for Slack
  
チャンネル上またはメンションで対応する地域の今日または明日または明後日の天気を尋ねると返信してくれるbot。  
情報はlivedoorのWeather Hacksから。 
日と都市は複数選択することができる。  

(成功する反応テキスト例)  
『大阪の明日の天気を教えて』  
『大阪と東京の今日の天気は？』  
『東京の明日と明後日の天気が知りたい』  

## 環境  
MacBook Air  
Python 3.6.4  
  
## 使用したライブラリ  
tweepy (Twiiterに接続)  
random (絵文字を選ぶ)  
urllib (livedoorのWeather Hacksに接続)  
apscheduler (定期ツイートのためのスケジューラ)  
datetime (現在時刻を取得)  
sys (エラーが出た時処理を終了)  
os (カレントディレクトリを移動する時使う)
json (サイトから情報を取ってくる時使う)  
dotenv (環境変数を設定する時使う)  

## ディレクトリ構造  

```
.                     
│
├── weatherBot/ 
│     ├── texts/ 
│     │     ├── area_codes.txt  
│     │     ├── weather_emoji.txt      
│     │     ├── good_emoji.txt         
│     │     └── bad_emoji.txt  
│     │
│     ├── __init__.py  
│     ├── main.py     
│     ├── get_weather.py        
│     └── __pychache__                                   
│
├── run.py (実行ファイル)       
│                
├── get_auth.py  
│                         
├── api_setting.py
│                         
├── .env(ignore) 
│                         
├── .env.sample 
│  
├── .gitignore  
│  
├──README.md  
│  
└──__pychache__ (ignore)
```
  

## 参考
[Pythonで天気予報をLINE通知する](https://qiita.com/kutsurogi194/items/6b9c8d37b2b83fc2ce87)  
[PythonのslackbotライブラリでSlackボットを作る](https://qiita.com/sukesuke/items/1ac92251def87357fdf6)
