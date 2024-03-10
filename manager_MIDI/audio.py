from pydub import AudioSegment
from pydub.playback import play

class Audio:
    def __init__(self, wavFile):
        self.wavFile = wavFile
        self.sound = AudioSegment.from_file(self.wavFile, format="wav")
        self.pitch_Sound = AudioSegment.from_file(self.wavFile, format="wav")

    def updateWavFile(self, wavFilePath):
        self.wavFile = wavFilePath 
        self.sound = AudioSegment.from_file(self.wavFile, format="wav")
        self.pitch_Sound = AudioSegment.from_file(self.wavFile, format="wav")

    def changePitch(self, octaves):
        new_sample_rate = int((self.sound.frame_rate * octaves) / 9) 
        hipitch_sound = self.sound._spawn(self.sound.raw_data, overrides={'frame_rate': new_sample_rate})
        self.pitch_Sound = hipitch_sound.set_frame_rate(44100)

    def playSound(self):
        if (self.wavFile == '/home/itpat/Code/Arduino/MIDI/manager_MIDI/../Beat/bass.wav'): 
            play(self.pitch_Sound[:200])
        else:
            play(self.pitch_Sound)
