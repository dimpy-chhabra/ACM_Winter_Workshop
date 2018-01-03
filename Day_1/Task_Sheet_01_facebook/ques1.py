#Create an app as a developer to obtain appID, write a Python program using this
#appID and collect your own feed information and your friends. Exhaustively grant all
#permissions to this app and then collect as much information as possible for yourself.

import urllib2
import json

access_token = 'EAA**fSfg*****aMNaIl*****SfYdMZD'

def get_page_data(page_id):
    graph_url = 'https://graph.facebook.com/v2.11/'+str(page_id)+'?fields=id,devices,birthday,posts.include_hidden(true){actions,application,coordinates,created_time,privacy,likes{pic_small},reactions{type}}&access_token='+access_token

    graph_url_1 = 'https://graph.facebook.com/me?fields=id,devices,birthday,posts.include_hidden(true){actions,application,coordinates,created_time,privacy,likes{pic_small},reactions{type}}&access_token='+access_token
   
    try:
        request = urllib2.Request(graph_url)
        response = urllib2.urlopen(request)

        try:
            return json.loads(response.read())

        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

# username or page id
#page_id = raw_input('Please enter a username or page name: ')
page_id = '161****277***8*' #given user's id
data = get_page_data(page_id)

print(data)

