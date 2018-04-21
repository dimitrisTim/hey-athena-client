"""
A simple module for playing music

Usage Examples:
    - "Play some music"
    - "Turn up!"
"""

from athena.classes.module import Module
from athena.classes.task import ActiveTask
from athena.api_library import spotifyAPI

SpotifyCommands = [r'.*\b(get turnt|turnt|turn up|play)\b (.+)',
                   r'.*\b(?:pause|stop) (?:the|this) (?:music|spotify)\b*',
                   r'.*\b(next|switch) ?(the|this) ?(song|track)\b.*',
                   r'.*\b(previous|back) ?(song|track)\b.*',
                   r'.*\b(repeat)\b.*',
                   r'.*\b(random)\b.*',
                   r'.*\b(get turnt|turnt|turn up|play)\b (weekly discoveries)']

class PlaySpotifySongTask(ActiveTask):

    def __init__(self):
        super(PlaySpotifySongTask, self).__init__(patterns=SpotifyCommands)
        self.groups = {1: 'commandGroup'}
   
    def match(self,text): 
        return self.match_and_save_groups(text, {2: 'artist'}) 

    def action(self, text):
        self.speak('Turning up '+self.artist)
        spotifyAPI.Authentication()
        spotifyAPI.SearchDevices()
        spotifyAPI.Shuffle()
        spotifyAPI.PlayArtist(self.artist)

class SpotifyMusic(Module):

    def __init__(self):
        tasks = [PlaySpotifySongTask()]
        super(SpotifyMusic, self).__init__('music', tasks, priority=2)
