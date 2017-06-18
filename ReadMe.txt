ReadMe.txt - Just keeping notes.

JSON format converter: https://jsonformatter.curiousconcept.com/
1) git status
2) git checkout
3) Edit files
4) git commit -a (to do them all)
5) git push (to update to the github website)

sudo systemctl daemon-reload
sudo systemctl restart bmcdo.service

systemd location is /etc/systemd/system

XRDP location: /etc/xrdp
added to xrdp.ini file: smart sizing:i:1

resources
    help
    moments
    tweet_prompts
    live_pipeline
    friendships
    statuses
    feedback
    drafts
    contacts
    media
    business_experience
    geo
    application

Then application is this:
      u'application':{
         u'/application/rate_limit_status':{
            u'reset':1477186977,
            u'limit':180,
            u'remaining':176



'{"created_at":"Sun Oct 23 19:52:21 +0000 2016","id":790279714346635264,"id_str":"790279714346635264","text":"@chipdeeps7 close 1023 1252p","source":"\\u003ca href="http:\\/\\/www.cloudhopper.com\\/" rel="nofollow"\\u003eCloudhopper\\u003c\\/a\\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":777311285138468864,"in_reply_to_user_id_str":"777311285138468864","in_reply_to_screen_name":"chipdeeps7","user":{"id":197944326,"id_str":"197944326","name":"Bryan","screen_name":"Sevsharkie7","location":null,"url":null,"description":null,"protected":false,"verified":false,"followers_count":1,"friends_count":23,"listed_count":1,"favourites_count":0,"statuses_count":129,"created_at":"Sat Oct 02 22:27:06 +0000 2010","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"C0DEED","profile_background_image_url":"http:\\/\\/abs.twimg.com\\/images\\/themes\\/theme1\\/bg.png","profile_background_image_url_https":"https:\\/\\/abs.twimg.com\\/images\\/themes\\/theme1\\/bg.png","profile_background_tile":false,"profile_link_color":"0084B4","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\\/\\/abs.twimg.com\\/sticky\\/default_profile_images\\/default_profile_6_normal.png","profile_image_url_https":"https:\\/\\/abs.twimg.com\\/sticky\\/default_profile_images\\/default_profile_6_normal.png","default_profile":true,"default_profile_image":true,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[],"user_mentions":[{"screen_name":"chipdeeps7","name":"Chip Deeps","id":777311285138468864,"id_str":"777311285138468864","indices":[0,11]}],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en","timestamp_ms":"1477252341244"}'


e = data.replace('="', "='")
f = e.replace('/"',"/'")
g = f.replace('w"\\', "w'\\")
="
/"
w"\

Here's the whole log, including error with empty tweet(?):
chip@chip:/home/chip/GarageDoor>cat log.out
Hello C.H.I.P. World! Setting up to look at the garage door.
Looking for a door to change @ May 28, 2017 23:31:42
tweeted:Looking for a door to change @ May 28, 2017 23:31:42
Door opened at 2017-05-28 23:32:43:
tweeted:Door opened at 2017-05-28 23:32:43:
May 28, 2017 23:34:45. Door open for 2.0 minutes.
tweeted:May 28, 2017 23:34:45. Door open for 2.0 minutes.
Door closed at 2017-05-28 23:37:47:
tweeted:Door closed at 2017-05-28 23:37:47:
on_data
May 28, 2017 23:47:20

g:

len(data):
0
Try failed in jsonData=json.loads(data). Went to exception path.
on_data
May 28, 2017 23:48:20
{"created_at":"Mon May 29 06:47:20 +0000 2017","id":869082714317537280,"id_str":"869082714317537280","text":"@chipdeeps7 status 170528 1147p","source":"\u003ca href=\"http:\/\/www.cloudhopper.com\/\" rel=\"nofollow\"\u003eCloudhopper\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":777311285138468864,"in_reply_to_user_id_str":"777311285138468864","in_reply_to_screen_name":"chipdeeps7","user":{"id":197944326,"id_str":"197944326","name":"Bryan","screen_name":"Sevsharkie7","location":null,"url":null,"description":null,"protected":false,"verified":false,"followers_count":1,"friends_count":24,"listed_count":1,"favourites_count":2,"statuses_count":166,"created_at":"Sat Oct 02 22:27:06 +0000 2010","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"C0DEED","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/abs.twimg.com\/sticky\/default_profile_images\/default_profile_normal.png","profile_image_url_https":"https:\/\/abs.twimg.com\/sticky\/default_profile_images\/default_profile_normal.png","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[],"user_mentions":[{"screen_name":"chipdeeps7","name":"Chip Deeps","id":777311285138468864,"id_str":"777311285138468864","indices":[0,11]}],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"nl","timestamp_ms":"1496040440526"}

g:
{"created_at":"Mon May 29 06:47:20 +0000 2017","id":869082714317537280,"id_str":"869082714317537280","text":"@chipdeeps7 status 170528 1147p","source":"\u003ca href=\"http:\/\/www.cloudhopper.com\/\" rel=\"nofollow\"\u003eCloudhopper\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":777311285138468864,"in_reply_to_user_id_str":"777311285138468864","in_reply_to_screen_name":"chipdeeps7","user":{"id":197944326,"id_str":"197944326","name":"Bryan","screen_name":"Sevsharkie7","location":null,"url":null,"description":null,"protected":false,"verified":false,"followers_count":1,"friends_count":24,"listed_count":1,"favourites_count":2,"statuses_count":166,"created_at":"Sat Oct 02 22:27:06 +0000 2010","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"C0DEED","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/abs.twimg.com\/sticky\/default_profile_images\/default_profile_normal.png","profile_image_url_https":chip@chip:/home/chip/GarageDoor>
