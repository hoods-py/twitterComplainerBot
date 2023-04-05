import twitterBot

PROMISED_DOWN = 200
PROMISED_UP = 20

bot = twitterBot.InternetSpeedTwitterBot()
bot.get_internet_speed()
dl_speed = bot.download_speed
ul_speed = bot.upload_speed

if dl_speed < PROMISED_DOWN or ul_speed < PROMISED_UP:
    bot.tweet_at_provider(down_speed=dl_speed, up_speed=ul_speed)
