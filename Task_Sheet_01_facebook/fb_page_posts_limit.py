#To Get Data from a page on facebook with certain restrictions
#Facebook Page: POTUS's facebook Page

import requests

access_token = 'EAA****************PUwkbz*********7POUZB***************'
def get_page_data(page_id):
	url = 'https://graph.facebook.com/v2.11/'+str(page_id)+'/posts?access_token='+access_token+'&pretty=0&limit=10'
	data = requests.get(url)
	response = data.text
	print response

get_page_data('1220332944702810')

