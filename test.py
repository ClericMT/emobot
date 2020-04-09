import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import time
import sys
from playsound import playsound
import sounddevice as sd
from scipy.io.wavfile import write
import os
import crepe
from scipy.io import wavfile

fs = 44100  # this is the frequency sampling; also: 4999, 64000
seconds = 4  # Duration of recording


myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
print("Starting: Speak now!")
playsound('metronome.wav')
sd.wait()  # Wait until recording is finished
print("finished")
write('output.wav', fs, myrecording)  # Save as WAV file

sr, audio = wavfile.read('/Users/1/Documents/Python/Crepe/evillimiter/output.wav')
time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)

# detects frequencies at 4th 5th and 6th second


#determines if the 3 notes are E, F, Bb.
#Plays different sound on whether it was correct
class Notes(object):

    #emotions
    happy = 'EF#B'
    excited = 'EBB'
    tender = 'EF#F#'
    sad = 'F#EE'
    angry = 'EEE'
    scared = 'EF#E'

    first_hz = int(frequency[150])
    second_hz = int(frequency[250])
    third_hz = int(frequency[350])
    notes = ['A','B','C']
    sequence = 'Z'
    emotional_state = 'nothing'
    loop = True
    def __init__ (self):
        pass

    #checks notes
    def first_check(self):
        if self.first_hz in range(600, 699):
            self.notes[0] = ('E')
        elif self.first_hz in range(700, 800):
            self.notes[0] = ('F#')
        elif self.first_hz in range(920, 1050):
            self.notes[0] = ('B')
        else: self.notes[0] = ('Z')
        run.second_check()
    def second_check(self):
        if self.second_hz in range(600, 699):
            self.notes[1] = ('E')
        elif self.second_hz in range(700, 800):
            self.notes[1] = ('F#')
        elif self.second_hz in range(920, 1050):
            self.notes[1] = ('B')
        else: self.notes[1] = ('Z')
    def third_check(self):
        if self.third_hz in range(600, 699):
            self.notes[2] = ('E')
        elif self.third_hz in range(700, 800):
            self.notes[2] = ('F#')
        elif self.third_hz in range(920, 1050):
            self.notes[2] = ('B')
        else: self.notes[2] = ('Z')
    #creates a unique string
    def sequencer(self):
        self.sequence = (''.join(self.notes))
    #checks the sequence and runs relative command
    def commands(self):
        if self.sequence == self.happy:
            self.emotional_state = 'happy'
            playsound('emotions/happy.wav')
        elif self.sequence == self.excited:
            self.emotional_state = 'excited'
            playsound('emotions/excited.wav')
        elif self.sequence == self.tender:
            self.emotional_state = 'tender'
            playsound('emotions/tender.wav')
        elif self.sequence == self.sad:
            self.emotional_state = 'sad'
            playsound('emotions/sad.wav')
        elif self.sequence == self.angry:
            self.emotional_state = 'angry'
            playsound('emotions/angry.wav')
        elif self.sequence == self.scared:
            self.emotional_state = 'scared'
            playsound('emotions/scared.wav')
        else:
            print('nothing')

run = Notes()

run.first_check()
run.second_check()
run.third_check()
run.sequencer()
run.commands()
print('I am ' + run.emotional_state)
