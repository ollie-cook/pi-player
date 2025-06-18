import requests

# This is how I was initially getting the access_token, but this method didn't allow me to control playback.
# I had to follow the Authorization Code flow to get a token that would allow me to control playback.
# Didn't want to lose this code so I've put it here.

# The API endpoint
url = "https://accounts.spotify.com/api/token"

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

data = {
    "grant_type": "client_credentials",
    "client_id": "07b5280e59b042e585abe712da77cce5",
    "client_secret": "d897ec38a53143ecb45ed9cd5d44fa90"
}

# A GET request to the API
response = requests.post(url, headers=headers, data=data)
responseJson = response.json()
access_token = responseJson["access_token"]