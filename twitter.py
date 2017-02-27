import json
from TwitterSearch import TwitterSearch, TwitterSearchException, TwitterUserOrder
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='a04bf0cda38fd380a2e89b9b54d6076729b568ce')


# def getTweets(place):
try:
        place = raw_input("Enter a twitter handle to point of interest: ")
        tuo = TwitterUserOrder(place) # create a TwitterUserOrder

        # it's about time to create TwitterSearch object again
        ts = TwitterSearch(
        consumer_key = 'jP53etLOQHrdCtMc4j2Djas2z',
            consumer_secret = '9UmpzmT1IPF6JuNzODHOyXZU19Vv1C0eYOQraQLwY04jAMGpu4',
            access_token = '746046118652416000-BZC8oHZZ75dJe8Q8fGlMigNvKy6kVwK',
            access_token_secret = 'Nfl6UpuUUdvSy60tN6p7l3l1W0GOGKpQoIbqZg78cdrtd'
        )


        def my_callback_closure(current_ts_instance): # accepts ONE argument: an instance of TwitterSearch
            queries, tweets_seen = current_ts_instance.get_statistics()
            # if queries > 0 and (queries % 60) == 0: # trigger delay every 5th query
            #     time.sleep(30) # sleep for 60 seconds

        tweetArray = []
        # start asking Twitter about the timeline
        for tweet in ts.search_tweets_iterable(tuo, callback=my_callback_closure):
            # tweetArray.append(tweet['text'])
            # if 'accessible' in tweet['text']:
                print tweet['text']
                print(json.dumps(alchemy_language.emotion(text=tweet['text'], language='english'), indent=2))

except TwitterSearchException as e: # catch all those ugly errors
        print(e)
