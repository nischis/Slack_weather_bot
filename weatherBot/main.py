from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from weatherBot import get_weather

@listen_to('天気')
def mention_func3(message):
  text = message.body['text']
  weather = get_weather.GetWeather(text)
  message.reply(weather.make_text())

@respond_to('天気')
def mention_func4(message):
  text = message.body['text']
  weather = get_weather.GetWeather(text)
  message.reply(weather.make_text())