"""
A simple module for playing music

Usage Examples:
    - "Play some music"
    - "Turn up!"
"""

from athena.classes.module import Module
from athena.classes.wit_task import ActiveTask
from athena.api_library import spotifyAPI

class PlaySpotifySongTask(ActiveTask):

    def __init__(self):
        super(PlaySpotifySongTask, self).__init__()

    def match(self,text):
        return self.match_and_save_groups(text,"")

    def action(self, text):
        spotifyAPI.ExecuteGenericCommand(self.wit_topic)
        #spotifyAPI.Authentication()
        #spotifyAPI.SearchDevices()
        #spotifyAPI.Shuffle()
        #spotifyAPI.PlayArtist(self.artist)

class SpotifyMusic(Module):

    def __init__(self):
        tasks = [PlaySpotifySongTask()]
        super(SpotifyMusic, self).__init__('music', tasks, priority=2)
