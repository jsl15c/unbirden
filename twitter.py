from TwitterSearch import TwitterSearch, TwitterSearchException

try:
    place = raw_input("Enter a twitter handle: ")
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
        if queries > 0 and (queries % 60) == 0: # trigger delay every 5th query
            time.sleep(30) # sleep for 60 seconds

    # start asking Twitter about the timeline
    for tweet in ts.search_tweets_iterable(tuo, callback=my_callback_closure):
            print(tweet['text'])

except TwitterSearchException as e: # catch all those ugly errors
    print(e)
