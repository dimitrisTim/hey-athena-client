import sys
import spotipy
import spotipy.util as util
import operator

sp = ''
primaryDeviceID = ''
topicName = ""
topicValue = ""

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

def Play_Artist():
    artistName = topicValue
    uri = SearchArtistUri(artistName)
    sp.start_playback(device_id=primaryDeviceID, context_uri=uri, uris=None, offset=None)
    #Add return string to speak!

def Shuffle():
    sp.shuffle(state=True,device_id=primaryDeviceID)

def Stop_Music():
    try:
        sp.pause_playback(device_id=primaryDeviceID)
    except:
        pass

def Continue_Playback():
    try:
        sp.start_playback(device_id=primaryDeviceID, context_uri=None, uris=None, offset=None)
    except:
        pass

def Previous_Track():
    sp.previous_track(device_id=primaryDeviceID)

def Next_Song():
    sp.next_track(device_id=primaryDeviceID)

def Repeat_Song():
    sp.repeat(state='track', device_id=primaryDeviceID)

def ExecuteGenericCommand(TopicAndValue):
   global topicName
   global topicValue
   topicName=GetTopicWithBiggestConfidence(TopicAndValue)
   topicValue=TopicAndValue['entities'][topicName][0]['value']
   print(topicName + " " + topicValue)
   Authentication()
   SearchDevices()
   exec(topicName+'()') #Call the function of this file with reflection

def GetTopicWithBiggestConfidence(dictionary):
   topics=iter(dictionary['entities'])
   topicList=[]
   #Iterate though topics and get names
   for topic in topics:
       topicList.append(topic)
   confidenceList=[]
   #Get confidence rates of each topic
   for name in topicList:
       confidenceList.append(dictionary['entities'][name][0]['confidence'])
   #Return the topic with the max confidence
   return topicList[confidenceList.index(max(confidenceList))]
