import json
import requests

blog_url = 'https://www.googleapis.com/blogger/v3/blogs/3564735312144269387/posts?key=AIzaSyAZxZa3vQTLS6-jiB2zBXpyp4D8_15YEoc'
counter = 0
blog_data = []
next_token  = ''

while True:

  req_url = blog_url
  if next_token != '':
    req_url = req_url + '&pageToken=' + next_token
  r = requests.get(req_url)
  print(next_token)
  resp_json = r.json()
  next_token = resp_json['nextPageToken']
  counter = counter + 1
  with open('captain'+str(counter)+'.txt', 'w') as outfile:
    json.dump(resp_json, outfile)
  if next_token == '' or next_token is None:
    break
