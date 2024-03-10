from manager_MIDI.mode import Mode
from manager_MIDI.audio import Audio

class SerialInput :
    def __init__(self):
        self.data = ""
        self.octaves = 10

        self.mode = Mode()
        self.audio = Audio(self.mode.getWavFile())

    def setNewData(self,newData):
        self.data = newData

        if self.data == b"Mode":
            self.mode.changeMode()
            self.audio.updateWavFile(self.mode.getWavFile())

        if self.data == b"Drum":
            self.audio.playSound()
        
        if self.data.isdigit():
            if (int(self.data) <= 10):
                self.octaves = 10
            else:
                self.octaves = int(self.data)

            self.audio.changePitch(self.octaves)


