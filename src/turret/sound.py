import subprocess
import os

class Sound(object):
    '''
        Class that handles sound
    '''
    
    def __init__(self):
        self.path = "/home/turret/"
        self.sounds = dict()
        self.load_sounds()
    
    def play_sound(self, index):
        self.player = subprocess.Popen(["mplayer", self.path + self.sounds[index]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        
    def load_sounds(self):
        for file in os.listdir(self.path):
            if file.endswith(".wav") or file.endswith(".mp3"):
                self.sounds[file[:file.rfind('.')]] = file

