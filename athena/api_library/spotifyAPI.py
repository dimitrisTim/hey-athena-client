import sys
import spotipy
import spotipy.util as util

sp = ''
primaryDeviceID = ''
def Authentication():
    global sp
    scope = 'user-library-read user-modify-playback-state user-read-playback-state'
    username = 'Dimitris Tim'
    token = util.prompt_for_user_token(username, scope, client_id='a34825dffc9f4ed5a2c96fdab6c75b74',
                                   client_secret='675d145baf9841e1b2578373c0b0957f',
                                   redirect_uri='http://localhost/')
    if token:
        sp = spotipy.Spotify(auth=token)

def SearchArtistUri(artistName):
    results = sp.search(artistName, limit=10, offset=0, type='artist', market=None)
    artistUri = results['artists']['items'][0]['uri']
    return artistUri

def SearchDevices():
    global primaryDeviceID
    devices = sp.devices()
    primaryDeviceID = devices['devices'][0]['id']

def PlayArtist(artistName):
    uri = SearchArtistUri(artistName)
    sp.start_playback(device_id=primaryDeviceID, context_uri=uri, uris=None, offset=None)

def Shuffle():
    sp.shuffle(state=True,device_id=None)

def Pause():
    try:
        sp.pause_playback(device_id=None)
    except:
        pass

def PreviousTrack():
    sp.previous_track(device_id=None)

def NextTrack():
    sp.next_track(device_id=None)

#Authentication()
#Shuffle()
#PlayArtist("mastodon")
#Pause()
