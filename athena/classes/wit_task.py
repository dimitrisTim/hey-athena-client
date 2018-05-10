"""
The "Task" class represents an action to be performed

The "ActiveTask" class uses the "match" method to trigger an action.
Generally regex patterns are supplied to do the input matching.
The "match" method can be overriden with "return match_any(text)" to
trigger an action upon matching any given regex pattern.
"""

import re

from athena import tts
from wit import Wit


class Task(object):
    speak = staticmethod(tts.speak)

    def action(self, text):
        """ Execute the task action """
        return


class ActiveTask(Task):
    def __init__(self,
                 priority=0,
                 greedy=True,
                 wit_topic="",
                # Connect to the Wit Application with the access token 
                 client= Wit('SESWFORYWQZRZPZO2IKDCMSR7BOSJ4PO')):

        # Tasks are matched/sorted with priority in modules
        self.priority = priority

        # If task is matched, stop module from matching the proceeding tasks
        self.greedy = greedy

        self.wit_topic = wit_topic
        self.client = client

    def match(self, text):
        """ Check if the task input criteria is met """
        return self.match_any(self,text)

    def match_any(self, text):
        """ Check if any patterns match """
        return True

    def match_and_save_groups(self, text, group_key_dict):
        """ Check if any patterns match,
        If so, save the match groups to self.(key name)
        """
        resp = self.client.message(text)
        self.wit_topic = resp
        return True

