import twitter

consumer_key = '2lKA00jF065mZvWq7SbWj3fXV'
consumer_secret = 'edcYfbHsAz7wYuP7RhZS93RXNLvPjlHhb1hD4eB5GQ3hbu5tld'
acces_token = '1096961698580246529-ntoSXDshPUyf7mqw3lCuMVgBqzX5x3'
access_secret = 'l9rYnHE1koCM8eiCZXgbuctyaS1CY4X4fN437dxAY2fue'

api = twitter.Api(consumer_key=consumer_key,
				consumer_secret=consumer_secret,
				access_token_key=acces_token,
				access_token_secret=access_secret)

print(api.VerifyCredentials())

post_update = api.PostUpdates(status='post update testing')
post_direct_message = api.PostDirectMessage(user='', text='')
get_user = api.GetUser(user='')
get_replies = api.GetReplies()
user_timeline = api.GetUserTimeline(user='')
home_timeline = api.GetHomeTimeline()
get_status = api.GetStatus(status_id='')
get statuses = api.GetStatuses(status_ids='')
destroy_status = api.DestroyStatus(status_id='')
friends = api.GetFriends(user='')
followers = api.GetFollowers()
featured = api.GetFeatured()
get_direct_message = api.GetDirectMessages()
sent_direct_messages = api.GetSentDirectMessages()
post_direct_messages = api.PostDirectMessage(user='', text='')
destroy_direct_message = api.DestroyDirectMessage(message_id='')
destroy_friendship = api.DestroyFriendship(user='')
create_friendship = api.CreateFriendship(user='')
lookup_friendship = api.LookupFriendship(user='')
verify_credentials = api.VerifyCredentials()