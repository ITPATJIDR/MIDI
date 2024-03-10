import os

class Mode :
    def __init__(self):
        beat_folder = os.path.join(os.path.dirname(__file__), '..', "Beat")
        self._Mode = ["Drum", "Bass", "Melodies"]
        self._index_Mode = 0
        self._current_Mode = self._Mode[self._index_Mode]
        self._hi_hat_Path = os.path.join(beat_folder, "hi_hat.wav")
        self._drum_Path = os.path.join(beat_folder, "drum.wav")
        self._bass_Path = os.path.join(beat_folder, "bass.wav")

    def getMode(self):
        return self._current_Mode

    def changeMode(self):
        if self._index_Mode < len(self._Mode) - 1 :
            self._index_Mode += 1
        else:
            self._index_Mode = 0

        self._current_Mode = self._Mode[self._index_Mode]

    def getWavFile(self):
        if(self._current_Mode == "Drum"):
            return self._drum_Path
        elif (self._current_Mode == "Bass"):
            return self._bass_Path
        else:
            return self._hi_hat_Path
