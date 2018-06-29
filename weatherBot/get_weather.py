import json
import sys
import os
import random
import urllib.parse
import urllib.request

class GetWeather:

  def __init__(self, text):

    # 本文を取得
    self.text = text
    # サイトのURLのフォーマットを取得
    self.weather_url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=%s"

    # 対応してる都市とコードの対応を格納しておく辞書
    self.area_code = {}  
    # 表示する都市とコードの対応を格納しておく辞書
    self.city = {}

    # 対応しいる日を格納する配列
    self.days = {"今日":"0", "明日":"1", "明後日":"2"}
    # 表示する日を格納する配列
    self.day = {}

    # 表示する天気、最高気温、最低気温を格納する配列
    self.weather = '分からない'
    self.min_temperature = ''
    self.max_temperature = ''

    # 天気の絵文字を格納する辞書
    self.weather_emoji ={}
    # 絵文字を格納する配列
    self.good_emoji = []
    self.bad_emoji = []

  ## 各種ファイルを開いて配列に格納する

  # 天気関連のファイル
  def open_file(self):
    try:
      # 対応している都市コードのファイル
      with open('./texts/area_codes.txt', 'r') as f:
        areas = [line.replace("\n", "").split(",") for line in f.readlines()]
      
      # 辞書型に整形
      self.area_code = dict(areas)
      
      # 天気の絵文字のファイル
      with open('./texts/weather_emoji.txt', 'r') as f:
        weather_emojis = [line.replace("\n", "").split(",") for line in f.readlines()]

      # 辞書型に整形
      self.weather_emoji = dict(weather_emojis)

      # いい時に付ける絵文字のファイル
      with open("./texts/good_emoji.txt", "r") as f:
        self.good_emoji = [line.replace("\n", "") for line in f.readlines()]
      
      # 悪い時に付ける絵文字のファイル
      with open("./texts/bad_emoji.txt", "r") as f:
        self.bad_emoji = [line.replace("\n", "") for line in f.readlines()]

    except:
      print("can't open file")
      sys.exit(1)

  ## 取得したツイートの解析

  # ツイートに含まれている都市名を取得
  def get_city_code(self):
    for name,code in self.area_code.items():
      if name in self.text:
        self.city[name] = code

  # テキストに含まれている日を取得  
  def get_day(self):
    for a_day,number in self.days.items():
      if a_day in self.text:
        self.day[a_day] = number
    # 含まれていなければ今日の天気を格納しておく
    if self.day == {}:
      self.day["今日"] = "0"

  ## 天気の情報を取得する
  def get_weather_info(self, code):
    try:
      url = self.weather_url % code
      html = urllib.request.urlopen(url)
      html_json = json.loads(html.read().decode('utf-8'))
      
    except Exception as e:
      print("Exception Error: ", e)
      sys.exit(1)
      
    return html_json

  def set_weather_info(self, weather_json, day):
    self.weather = '分からない'
    self.max_temperature = '分からなくて'
    self.min_temperature = '分からないです' + random.choice(self.bad_emoji)

    try:
      self.weather = weather_json['forecasts'][day]['telop']
      self.max_temperature = str(weather_json['forecasts'][day]['temperature']['max']['celsius']) + "℃で"
      self.min_temperature = str(weather_json['forecasts'][day]['temperature']['min']['celsius']) + "℃です" + random.choice(self.good_emoji)
    except TypeError:
      pass


  ## ツイート内容を作る    
  def make_text(self):

    self.open_file()
    self.get_city_code()
    if self.city == {}:
      reply = "対応している都市名を入れてくれないと答えれないです" + random.choice(self.bad_emoji)
      return reply

    reply = ""
    for name,code in self.city.items():
      for a_day,number in self.day.items():
        weather_json = self.get_weather_info(code)
        self.set_weather_info(weather_json, int(number))

        reply += "\n{0}の{1}の天気は{2}です{3}\n".format(name, a_day, self.weather,self.weather_emoji[self.weather])
        reply += "最高気温は{0}、最低気温は{1}\n".format(self.max_temperature, self.min_temperature)

    return reply