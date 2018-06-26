import speedtest
import tweepy
import time

consumer_key = 'KEYHERE'
consumer_secret = 'KEYHERE'
access_token = 'KEYHERE'
access_token_secret = 'KEYHERE'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()

while(True):
    servers = []
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    results_dict = s.results.dict()
    download_Mbits = results_dict["download"] / 1048576
    upload_Mbits = results_dict["upload"] / 1048576
    print (download_Mbits)
    print (upload_Mbits)

    if(download_Mbits < SPEEDPAIDFORHERE and upload_Mbits < SPEEDPAIDFORHERE):
        api.update_status('Hey @ISPNAMEHERE , why do you charge for SPEEDPAIDFOR Mbps when current speed is ' + str(download_Mbits) + ' download Mbps and ' + str(upload_Mbits) + ' upload Mbps?!' )
    time.sleep(21600)
