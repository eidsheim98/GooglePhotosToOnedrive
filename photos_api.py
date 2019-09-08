from oauth2client.client import OAuth2WebServerFlow
from requests_oauthlib import OAuth2Session
import requests, time, datetime, json

class Photos_API():
    def __init__(self):

        self.redirect_uri='https://localhost:8080/oauth2callback/'
        self.client_id = '351326181543-nstl8k6shh13h4p5k9ak2m1mt1gpe6o8.apps.googleusercontent.com'
        self.client_secret='f1PeZ5Haegf--XFGmxqVhtbQ'
        self.scope=['https://www.googleapis.com/auth/photoslibrary.readonly']
        self.token = ''
        self.images = []


    def __auth(self):
        oauth = OAuth2Session(self.client_id, redirect_uri=self.redirect_uri,
                              scope=self.scope)

        authorization_url, state = oauth.authorization_url(
            'https://accounts.google.com/o/oauth2/auth',
            # access_type and prompt are Google specific extra
            # parameters.
            access_type="offline", prompt="select_account")

        print('Please go to %s and authorize access.' % authorization_url)
        authorization_response = input('Enter the full callback URL')

        token = oauth.fetch_token(
            'https://accounts.google.com/o/oauth2/token',
            authorization_response=authorization_response,
            # Google specific extra parameter used for client
            # authentication
            client_secret=self.client_secret)

        token = token.get('access_token')

        self.token = token
        return token

    def get_data(self):
        headers = {'Content-Type': 'application/json;encoding=utf-8', 'Authorization': 'Bearer {}'.format(self.token)}
        url = 'https://photoslibrary.googleapis.com/v1/albums'
        r = requests.get(url, headers=headers)
        return r.json()

    def get_albums(self):
        self.__auth()
        data = self.get_data()
        albums = data['albums']
        fullrange = 0
        for i in range(len(albums)):
            album = albums[i]
            id = album['id']
            title = album['title']
            count = album['mediaItemsCount']
            print('-----------------------')
            print('Album {}'.format(i))
            print(title)
        try:
            albums_to_be_processed = input('Input number of albums to be processed, seperate with comma: ')
        except:
            albums_to_be_processed = input('Please valid numbers: ')

        if 'all' in albums_to_be_processed:
            albums_to_be_processed = list(range(0, len(albums)))
        else:
            albums_to_be_processed = albums_to_be_processed.split(',')
            albums_to_be_processed = [int(x.replace(' ', '')) for x in albums_to_be_processed]

        d = {}
        for album_to_be_processed in albums_to_be_processed:
            i = album_to_be_processed
            images = self.get_media(albums[i]['id'])
            title = albums[i]['title']
            d[title] = images
        return d, fullrange


    def get_media(self, id):
        images = []
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(self.token)}
        url = 'https://photoslibrary.googleapis.com/v1/mediaItems:search'
        data = '{"pageSize":"100","albumId": "'+ str(id) +'"}'
        r = requests.post(url, data=data, headers=headers)
        data = r.json()
        mediaitems = data['mediaItems']
        for mediaitem in mediaitems:
            id = mediaitem['id']
            filename = mediaitem['filename']
            images.append(filename)
        return images


if __name__ == '__main__':
    p = Photos_API()
    images = p.get_albums()
    print(images)