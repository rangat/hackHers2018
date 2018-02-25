import cred
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, render_template, request, url_for, redirect

scope = 'user-library-read'

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        usr = request.form['usr']
        print(usr)
        loginUsr('1287724819')
        return redirect(url_for('play'))

@app.route('/playlists', methods=['GET', 'POST'])
def play():
    if request.method=='GET':
        return render_template('playlist.html')

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))

def loginUsr(usr):
    username = usr
    token = util.prompt_for_user_token(username, scope, client_id=cred.SPOTIPY_CLIENT_ID, client_secret=cred.SPOTIPY_CLIENT_SECRET, redirect_uri=cred.SPOTIPY_REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.current_user_playlists(limit=10, offset=0)
        print(playlists)
    else:
        print("Can't get token for", username)

if __name__ == '__main__':
    app.run('localhost', port=8080, debug=True)